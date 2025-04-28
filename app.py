from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-pro")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.json
    caso = data.get('caso', '')
    respuesta_usuario = data.get('respuesta_usuario', '')

    
    prompt = f"""
    Actúa como un experto en la norma ISO 45001. Tu tarea será:

    1. Proporcionar tu propia respuesta profesional al siguiente caso de estudio, basándote estrictamente en la norma ISO 45001.
    
    Caso de estudio:
    {caso}

    2. Luego compara tu respuesta con la propuesta del usuario:
    
    Respuesta del usuario:
    {respuesta_usuario}

    3. Analiza qué tan correcta es la respuesta del usuario:
    - ¿En qué coincide con la norma y con tu respuesta?
    - ¿En qué se equivoca o qué puede mejorar?
    - ¿Qué partes están bien justificadas y cuáles no?

    4. Finalmente, otorga una nota sobre 10 puntos basada en la adherencia a los principios de ISO 45001.

    Organiza tu respuesta de forma clara bajo los siguientes apartados:
    - Respuesta oficial basada en ISO 45001
    - Comparación con la respuesta del usuario
    - Correcciones y mejoras sugeridas
    - Nota final sobre 10
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"respuesta_ia": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
