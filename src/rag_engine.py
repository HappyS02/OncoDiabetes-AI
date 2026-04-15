# 5- LLM & RAG (PDF okuma ve bilgi çekme)

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "docs")
SAVE_PATH = os.path.join(BASE_DIR, "models", "faiss_index")

def setup_rag():
    # 1. KRİTİK ÇÖZÜM: Klasörler yoksa otomatik oluştur
    os.makedirs(SAVE_PATH, exist_ok=True)
    os.makedirs(DOCS_PATH, exist_ok=True)
    
    all_documents = []
    
    # Docs klasöründeki PDF'leri oku
    for file in os.listdir(DOCS_PATH):
        if file.endswith(".pdf"):
            print(f"Okunuyor: {file}")
            loader = PyPDFLoader(os.path.join(DOCS_PATH, file))
            all_documents.extend(loader.load())
            
    # Eğer PDF yoksa sistemi boşuna yorma ve uyar
    if len(all_documents) == 0:
        print("HATA: 'docs' klasöründe hiç PDF bulunamadı! Lütfen klasöre PDF ekleyin.")
        return
    
    # Metinleri parçala
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(all_documents)
    
    # Vektörlere dönüştür ve KAYDET
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(splits, embeddings)
    vector_store.save_local(SAVE_PATH)
    
    print("✓ RAG Sistemi başarıyla hazırlandı ve kaydedildi!")

if __name__ == "__main__":
    setup_rag()