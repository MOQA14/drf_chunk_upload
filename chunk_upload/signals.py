from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings
from .models import *  # مدل موردنظر را ایمپورت کن

@receiver(post_delete, sender=Chunk)
def delete_file_on_model_delete(sender, instance, **kwargs):
    """هنگام حذف رکورد از دیتابیس، فایل مربوطه را هم حذف می‌کند"""
    if instance.file:  # فرض بر این است که فیلد فایل در مدل `file` نام دارد
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
