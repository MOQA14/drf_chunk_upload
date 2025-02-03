from django.apps import AppConfig


class ChunkUploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chunk_upload'

    def ready(self):
        import chunk_upload.signals
