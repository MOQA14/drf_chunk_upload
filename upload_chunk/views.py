from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Upload, Chunk
from .serializers import ChunkSerializer, UploadSerializer

from django.core.files.base import ContentFile
from django.db import transaction


class StartUploadView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            video_length = int(request.data.get('video_length'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid video length'}, status=status.HTTP_400_BAD_REQUEST)
        print(video_length)

        chunk_size = (video_length // 1000)
        chunk_number = 10
        print(chunk_size)

        upload = Upload.objects.create(
            video_length=video_length
        )

        response_data = {
            'chunk_size': chunk_size,
            'upload_id': upload.id,
            'chunk_number': chunk_number
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class ChunkUploadView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            chunk_number = int(request.data.get('chunk_number'))
            upload_id = int(request.data.get('upload_id'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid chunk number or upload ID'}, status=status.HTTP_400_BAD_REQUEST)

        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        chunk_file = request.FILES['file']
        print(chunk_file.name)

        try:
            upload = Upload.objects.get(id=upload_id)
        except Upload.DoesNotExist:
            return Response({'error': 'Upload not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create chunk
        chunk = Chunk.objects.create(
            upload=upload,
            chunk_number=chunk_number,
            file=chunk_file
        )

        if chunk_number == 10:
            upload.is_completed = True

        # Update uploaded_chunks count
        upload.uploaded_chunks += 1
        upload.last_modified = timezone.now()
        upload.save()
        # test print
        print(upload.uploaded_chunks)

        return Response(ChunkSerializer(chunk).data, status=status.HTTP_201_CREATED)


class CompleteUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            upload_id = int(request.data.get('upload_id'))
            total_chunks = int(request.data.get('total_chunks'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid upload ID or total chunks'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            upload = Upload.objects.get(id=upload_id)
        except Upload.DoesNotExist:
            return Response({'error': 'Upload not found'}, status=status.HTTP_404_NOT_FOUND)

        if upload.is_completed:
            return Response({'status': 'Upload completed'}, status=status.HTTP_200_OK)

        uploaded_chunks = upload.chunks.count()
        if uploaded_chunks != total_chunks:
            return Response({'error': f'Not all chunks uploaded: {uploaded_chunks}/{total_chunks}'},
                            status=status.HTTP_400_BAD_REQUEST)

        final_file = ContentFile(b'')
        for chunk in upload.chunks.order_by('uploaded_at'):
            final_file.write(chunk.file.read())

        upload.file.save(f'upload_{upload.id}.mp4', final_file)
        upload.is_completed = True
        upload.total_chunks = total_chunks
        upload.save()

        # Clean up chunks after combining
        upload.chunks.all().delete()

        return Response(UploadSerializer(upload).data, status=status.HTTP_200_OK)


class UploadDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, upload_id, *args, **kwargs):
        try:
            upload = Upload.objects.get(id=upload_id)
        except Upload.DoesNotExist:
            return Response({'error': 'Upload not found'}, status=status.HTTP_404_NOT_FOUND)

        # counting progress
        if upload.total_chunks > 0:
            progress = (upload.uploaded_chunks / upload.total_chunks) * 100
        else:
            progress = 0

        response_data = UploadSerializer(upload).data
        response_data['progress'] = progress

        return Response(response_data, status=status.HTTP_200_OK)


class UploadChunksView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, upload_id, *args, **kwargs):
        try:
            upload = Upload.objects.get(id=upload_id)
        except Upload.DoesNotExist:
            return Response({'error': 'Upload not found'}, status=status.HTTP_404_NOT_FOUND)

        chunks = upload.chunks.all()
        return Response(ChunkSerializer(chunks, many=True).data, status=status.HTTP_200_OK)


# for test
class DeleteUploadView(APIView):
    permission_classes = [permissions.AllowAny]

    def delete(self, request, upload_id, *args, **kwargs):
        try:
            upload = Upload.objects.get(id=upload_id)
            upload.delete()
        except Upload.DoesNotExist:
            return Response({'error': 'Upload not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response('file successfully deleted', status=status.HTTP_204_NO_CONTENT)


# for test
class DeleteChunkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        try:
            if Chunk.DoesNotExist:
                return Response('no chunk found', status=status.HTTP_404_NOT_FOUND)
        except Chunk.objects.get():
            Chunk.objects.all().delete()

            return Response('chunk deleted', status=status.HTTP_204_NO_CONTENT)
