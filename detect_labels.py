import boto3
from Constants import ACCESS_KEY_ID, SECRET_KEY, BUCKET_SOURCE, REGION

rekognition_client = boto3.Session(
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION).client('rekognition')

def detect_labels(img_key):
    print(f"Detectando etiquetas para la imagen: {img_key}")
    try:
        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': BUCKET_SOURCE, 'Name': img_key}},
            MaxLabels=20,
            MinConfidence=50
        )
        print("La tarea de detección de etiquetas se ha realizado con éxito")
        return response
    except Exception as e:
        print(f"Ha ocurrido un error detectando etiquetas: {e}")
        raise Exception("Ha ocurrido un error detectando etiquetas")