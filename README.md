# to making this page to graphic design, we should using 'typora'

    **Chunked Upload**

    This simple django app enables users to upload large files to Django Rest Framework in multiple chunks, 
    with the ability to automatically delete uncomplete uploads if the upload is not completed.


    1 - insatll with pip:
    
    pip install something = should writing something - 1


    2 - for using automatically delete uncomplete uploads:

    INSTALLED_APPS = (
    # ...
    'django_cron',
    ) - 2


    3 - Typical usage
    
    First, a request is sent to the server, which includes the length of the file. 
    Then the server returns a response including the chunk size and an upload ID to the client.
    In the next request, the client sends the file with a predetermined chunk size to the server.


    hint = In this code, the chunk number equal to 10 ,  you can change it if you need.


    