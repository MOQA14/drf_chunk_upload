from django.contrib import admin

from .models import Upload, Chunk


# Register your models here.

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['file', 'video_length', 'uploaded_at', 'last_modified', 'is_completed']
    search_fields = ['file', 'video_length', 'uploaded_at', 'last_modified', 'is_completed']
    list_filter = ['file', 'video_length', 'uploaded_at', 'last_modified', 'is_completed']


@admin.register(Chunk)
class ChunkAdmin(admin.ModelAdmin):
    list_display = ['file', 'upload', 'uploaded_at', 'chunk_number']
    search_fields = ['file', 'upload', 'uploaded_at', 'chunk_number']
    list_filter = ['file', 'upload', 'uploaded_at', 'chunk_number']
