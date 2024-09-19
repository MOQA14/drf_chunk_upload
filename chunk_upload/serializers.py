from rest_framework import serializers
from chunk_upload.models import Upload, Chunk


class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunk
        fields = '__all__'


class UploadSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Upload
        fields = '__all__'

    def get_progress(self, obj):
        if obj.total_chunks > 0:
            return (obj.uploaded_chunks / obj.total_chunks) * 100
        return 0
