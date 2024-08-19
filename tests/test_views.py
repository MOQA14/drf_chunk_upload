import pytest
from django.core.files.base import ContentFile
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from upload_chunk.models import Upload, Chunk


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_start_upload_view(api_client):
    url = reverse('start_upload')
    data = {'video_length': 10000}
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert 'chunk_size' in response.data
    assert 'upload_id' in response.data
    assert 'chunk_number' in response.data


@pytest.mark.django_db
def test_chunk_upload_view(api_client):
    # Create an initial upload object
    upload = Upload.objects.create(video_length=10000)

    url = reverse('chunk_upload')
    data = {
        'chunk_number': 1,
        'upload_id': upload.id,
    }
    file_data = {'file': ContentFile(b'This is a test chunk', 'chunk1.dat')}
    response = api_client.post(url, data, format='multipart', files=file_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert 'chunk_number' in response.data


@pytest.mark.django_db
def test_complete_upload_view(api_client):
    upload = Upload.objects.create(video_length=10000)
    url = reverse('complete_upload')
    data = {
        'upload_id': upload.id,
        'total_chunks': 10,
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'id' in response.data


@pytest.mark.django_db
def test_upload_detail_view(api_client):
    upload = Upload.objects.create(video_length=10000)
    url = reverse('upload_detail', args=[upload.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'id' in response.data
    assert 'progress' in response.data


@pytest.mark.django_db
def test_upload_chunks_view(api_client):
    upload = Upload.objects.create(video_length=10000)
    chunk = Chunk.objects.create(upload=upload, chunk_number=1, file=ContentFile(b'Test chunk', 'chunk1.dat'))

    url = reverse('upload_chunks', args=[upload.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


'''@pytest.mark.django_db
def test_delete_upload_view(api_client):
    upload = Upload.objects.create(video_length=10000)

    url = reverse('delete_upload', args=[upload.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Upload.objects.count() == 0


@pytest.mark.django_db
def test_delete_chunk_view(api_client):
    upload = Upload.objects.create(video_length=10000)
    chunk = Chunk.objects.create(upload=upload, chunk_number=1, file=ContentFile(b'Test chunk', 'chunk1.dat'))

    url = reverse('delete_chunk')
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Chunk.objects.count() == 0
'''