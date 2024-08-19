from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    video_length = models.IntegerField(blank=True, null=True)
    start_upload = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    total_chunks = models.IntegerField(default=0, blank=True, null=True)
    uploaded_chunks = models.PositiveIntegerField(default=0, blank=True, null=True)
    available_chunk_size = models.IntegerField(default=0, blank=True, null=True)


class Chunk(models.Model):
    upload = models.ForeignKey(Upload, related_name='chunks', on_delete=models.CASCADE, blank=True, null=True)
    chunk_number = models.IntegerField(blank=True, null=True)
    file = models.FileField(upload_to='chunks/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
