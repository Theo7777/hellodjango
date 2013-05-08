# Define bucket and folder for static files.
StaticStorage = lambda: S3BotoStorage(
    bucket='theoohene', 
    location='static')
