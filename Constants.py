import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')

BUCKET_SOURCE = os.environ.get('BUCKET_SOURCE')
BUCKET_DEST = os.environ.get('BUCKET_DEST')
REGION = os.environ.get('REGION')

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL_NAME = "models/gemini-2.5-flash-preview-09-2025"

FLASK_API_URL = "http://127.0.0.1:5000/api/analyze"
