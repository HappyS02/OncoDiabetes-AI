# 🧬 OncoDiabetes Nexus: Yapay Zeka Destekli Sağlık Ekosistemi

OncoDiabetes Nexus, onkoloji ve diyabet hastaları için geliştirilmiş, makine öğrenmesi ve üretken yapay zekayı tek bir modern arayüzde (Glassmorphism UI) birleştiren çok katmanlı bir sağlık asistanıdır.

## 🚀 Temel Özellikler
* **Makine Öğrenmesi (ML):** Random Forest algoritması ile hastanın güncel değerlerine göre kişiselleştirilmiş risk skorlaması.
* **Açıklanabilir Yapay Zeka (XAI):** Karar mekanizmasını "Kara Kutu" (Black Box) olmaktan çıkaran SHAP grafik entegrasyonu.
* **Görüntü İşleme (Vision AI):** Google Gemini Flash destekli akıllı kamera sistemiyle öğünlerin diyabetik analizi ve karbonhidrat hesabı.
* **Tıbbi Literatür Asistanı (RAG):** Yüklenen klinik rehberleri okuyup analiz ederek hastaya özel ve güvenilir metin tabanlı yanıtlar üreten otonom bot.
* **Otonom Ajanlar (Agentic AI):** Risk durumuna göre Diyetisyen ve Onkoloji Uzmanı rollerine bürünen yapay zeka modüllerinin kendi aralarında karar alması.

## 🛠️ Kullanılan Teknolojiler
* **Arayüz:** Streamlit (Custom CSS & Glassmorphism Design)
* **LLM & Vision:** Google Gemini API (`gemini-flash-latest`)
* **Veri Bilimi:** Scikit-Learn, Pandas, NumPy
* **Açıklanabilirlik:** SHAP (SHapley Additive exPlanations)

## ⚙️ Kurulum
1. Repoyu bilgisayarınıza klonlayın.
2. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt`
3. `app.py` içindeki `MY_API_KEY` alanına kendi Google API anahtarınızı girin.
4. Terminalden uygulamayı başlatın: `streamlit run app.py`