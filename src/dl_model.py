# 2- Deep Learning (Yemek tanıma)

import google.generativeai as genai
from PIL import Image

def predict_food(image_file, api_key):
    genai.configure(api_key=api_key)
    try:
        # En stabil, kotası en geniş sürüm
        model = genai.GenerativeModel('gemini-flash-latest') 
        img = Image.open(image_file)
        response = model.generate_content(["Bu yemeğin adını ve karbonhidrat değerini kısaca yaz.", img])
        return response.text
    except Exception as e:
        return f"Hata: {str(e)}"