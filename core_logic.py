import os
import cv2
import uuid
from aws_clients import s3, s3_client
from Constants import BUCKET_DEST, BUCKET_SOURCE
from detect_labels import detect_labels
from generate_haiku import get_haiku_from_labels

def generate_haiku_from_key(image_key):
    try:
        print(f"Procesando clave S3: {image_key}")
        response_rekognition = detect_labels(image_key)
        haiku_text = get_haiku_from_labels(response_rekognition)

        text_key = os.path.splitext(image_key)[0] + "_feedback.txt"
        s3.Object(BUCKET_DEST, text_key).put(
            Body=haiku_text,
            ContentType='text/plain'
        )
        print(f"Feedback guardado en: {BUCKET_DEST}/{text_key}")
        return haiku_text

    except Exception as e:
        print(f"Error procesando la clave: {e}")
        raise e

def upload_image(img):
    try:
        print("Codificando y subiendo imagen...")
        image_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        is_success, buffer = cv2.imencode(".jpg", image_bgr)
        if not is_success:
            raise Exception("Error al codificar la imagen")

        image_bytes = buffer.tobytes()
        image_key = f"haikuImagen_{uuid.uuid4()}.jpg"

        s3_client.put_object(
            Bucket=BUCKET_SOURCE,
            Key=image_key,
            Body=image_bytes,
            ContentType='image/jpeg'
        )
        print(f"Imagen subida a: {BUCKET_SOURCE}/{image_key}")
        return image_key

    except Exception as e:
        print(f"Error en la subida de imagen: {e}")
        raise e

#separo la carga de la imagen y el core de la aplicacion para qaue este todo encapsulado
def process_upload_and_get_haiku(img):
    try:
        image_key = upload_image(img)
        haiku = generate_haiku_from_key(image_key)
        return haiku
    except Exception as e:
        print(f"Error en el pipeline completo: {e}")
        raise e