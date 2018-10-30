import boto3
import time
import settings
from botocore import UNSIGNED
from botocore.client import Config

def getS3Filename():
    return f"{time.time()}.jpg"

def uploadToS3(filepath, s3_filename):
    print(f"\t\tUPLOADING {filepath} TO S3...")
    # Create an S3 client
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filepath, settings.S3_BUCKETNAME, f"uncategorized/{s3_filename}")
