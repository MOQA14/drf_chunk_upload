ChunkUpload
General Description

ChunkUpload is a project designed for uploading videos in chunks. This project receives videos without considering their size and stores them chunk by chunk in the database. A default chunk size is set, but you can modify it based on your needs.
Prerequisites

To use this project, follow these steps:

    Download and install the ChunkUpload package from PyPI:

    bash

pip install ChunkUpload

Add upload_chunk to the INSTALLED_APPS list in your Django project’s settings file (settings.py):

python

    INSTALLED_APPS = [
        ...,
        'upload_chunk',
    ]

Usage

    After completing the above steps, the project is ready, and you can upload your videos in chunks.
    The default chunk size can be found in the settings, which you can adjust according to your requirements.

Author

    moqa14

Development Team

    Nadimibox

Additional Information

For improving the quality of the project and contributing, feel free to contact me.