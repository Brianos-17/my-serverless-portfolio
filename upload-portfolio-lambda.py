import boto3
from botocore.client import Config
import zipfile

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

build_bucket = s3.Bucket('portfoliobuild.bos.info')
portfolio_bucket = s3.Bucket('portfolio.bos.info')

# On Windows, this will need to be a different location than /tmp
build_bucket.download_file('portfolio.zip', 'c:/Users/bosullivan/portfolio.zip')

with zipfile.ZipFile('c:/Users/bosullivan/portfolio.zip') as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        target_bucket.upload_fileobj(obj, nm)
        target_bucket.Object(nm).Acl().put(ACL='public-read')