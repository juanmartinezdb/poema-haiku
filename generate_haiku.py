import google.generativeai as genai
from Constants import GEMINI_API_KEY, MODEL_NAME

try:
    if not GEMINI_API_KEY:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction="Eres un poeta experto que escribe haikus (poemas de 5, 7 y 5 sílabas) en español."
    )
    print("Modelo Gemini cargado exitosamente.")
except Exception as e:
    print(f"Error al configurar Gemini: {e}")
    model = None

def get_haiku_from_labels(rekognition_response):
    if model is None:
        return "ERROR: El modelo de Gemini no está configurado."

    labels = rekognition_response.get('Labels', [])
    if not labels:
        return "No se detectaron etiquetas en la imagen."

    label_names = [label['Name'] for label in labels]
    labels_str = ", ".join(label_names)
    print(f"Etiquetas detectadas para el Haiku: {labels_str}")

    user_prompt = f"He visto una imagen que contiene: {labels_str}. Por favor, escribe un haiku original sobre esta imagen."

    try:
        response = model.generate_content(user_prompt)
        haiku = response.text.strip()
        print(f"Haiku generado: {haiku}")
        return haiku
    except Exception as e:
        print(f"Error al llamar a la API de Gemini: {e}")
        return f"Error al generar el haiku: {e}"