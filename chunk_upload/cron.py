from django_cron import CronJobBase, Schedule
from django.utils import timezone
from .models import Upload
import os
import glob


class DeleteIncompleteUploadsCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'UploadChunk.delete_incomplete_uploads_cron_job'  # unique code

    def do(self):
        twenty_four_hours_ago = timezone.now() - timezone.timedelta(hours=24)
        incomplete_uploads = Upload.objects.filter(
            uploaded_chunks__lt=10, last_modified__lt=twenty_four_hours_ago
        )

        for upload in incomplete_uploads:
            upload_path = f'temporary_chunks/{upload.id}/*'

            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

                chunk_files = glob.glob(f'{upload_path}/*')

            for chunk_file in chunk_files:
                if os.path.isfile(chunk_file):
                    os.remove(chunk_file)
            upload.delete()
