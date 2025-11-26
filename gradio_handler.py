import gradio as gr
from core_logic import process_upload_and_get_haiku

#esto se podria hacer en el core logic, pero realmente es para comprobar que gradio lo esta pillando bien y que gestione el mensaje de
# error por la interface
def analyze_and_get_haiku_gradio(img):
    if img is None:
        return "Por favor, sube una imagen."
    print("Imagen recibida en Gradio...")

    try:
        haiku_text = process_upload_and_get_haiku(img)
        return haiku_text

    except Exception as e:
        return f"Ha ocurrido un error inesperado: {e}"

iface = gr.Interface(
    fn=analyze_and_get_haiku_gradio,
    inputs=gr.Image(type="numpy", label="Sube una imagen para analizar"),
    outputs=gr.Textbox(label="Haiku generado (AWS Rekognition + Gemini)", lines=5),
    title="Generador de Haikus a partir de imágenes",
    description="Sube una imagen, la app reconocerá lo que ve y generara un bonito haiku."
)