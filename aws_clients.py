import boto3
from Constants import ACCESS_KEY_ID, SECRET_KEY

_session = boto3.Session(
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_KEY
)

s3 = _session.resource('s3')
s3_client = boto3.client('s3',
                         aws_access_key_id=ACCESS_KEY_ID,
                         aws_secret_access_key=SECRET_KEY
                         )