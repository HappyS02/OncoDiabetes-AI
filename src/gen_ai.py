# 4- Gen AI (İçerik/Diyet oluşturma)

import google.generativeai as genai

def get_ai_response(context, user_query, api_key):
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        prompt = f"Referans: {context}\nSoru: {user_query}\nKısa ve tıbbi olmayan bir dille cevapla."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata: {str(e)}"