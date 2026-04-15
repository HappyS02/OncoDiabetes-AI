import google.generativeai as genai

# Tırnak içine yeni aldığın şifreyi yazmayı unutma
genai.configure(api_key="AIzaSyD_z4-GXkmM6mls9HcKw2l3F4kOL2CJZwQ") 

print("Senin anahtarına tanımlı modeller:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)