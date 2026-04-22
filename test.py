import google.generativeai as genai

# Tırnak içine yeni aldığın şifreyi yazmayı unutma
genai.configure(api_key="API_KEY") 

print("Senin anahtarına tanımlı modeller:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
