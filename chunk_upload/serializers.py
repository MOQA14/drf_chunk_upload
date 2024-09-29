from rest_framework import serializers
from chunk_upload.models import Upload, Chunk


class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunk
        fields = '__all__'


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = '__all__'