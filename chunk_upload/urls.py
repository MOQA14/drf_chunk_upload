from django.urls import path
from .views import *

#Nadimibox -> Need Edit
urlpatterns = [
    path('upload/start/', StartUploadView.as_view(), name='upload'),
    path('upload/chunk/', ChunkUploadView.as_view(), name='chunk-upload'),
    path('upload/complete/', CompleteUploadView.as_view(), name='complete-upload'),
    #path('upload/<int:upload_id>/', UploadDetailView.as_view(), name='upload-detail'),
    #path('upload/<int:upload_id>/chunks/', UploadChunksView.as_view(), name='upload-chunks'),
    #path('upload/delete/<int:upload_id>', DeleteUploadView.as_view(), name='delete-upload'),
    path('chunk/delete/<int:upload_id>', DeleteChunkView.as_view(), name='delete-chunk'),
]