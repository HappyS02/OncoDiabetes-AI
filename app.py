# streamlit run app.py

import streamlit as st
import os, pickle
from src.ml_model import PLOT_PATH, MODEL_PATH
from src.dl_model import predict_food
from src.agents import coordinate_agents
from src.gen_ai import get_ai_response

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="OncoDiabetes AI", page_icon="🧬", layout="wide", initial_sidebar_state="collapsed")

# BURAYA API ŞİFRENİ YAZ (Artık RAG da şifreyi buradan alacak)
MY_API_KEY = "AIzaSyD_z4-GXkmM6mls9HcKw2l3F4kOL2CJZwQ"

# --- PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%); }
    .main-title { font-size: 3.5rem; font-weight: 800; text-align: center; background: -webkit-linear-gradient(45deg, #1E3A8A, #3B82F6, #10B981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; padding-bottom: 0px; }
    .sub-title { text-align: center; color: #64748B; font-size: 1.2rem; font-weight: 500; margin-top: -10px; margin-bottom: 30px; }
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] { background: rgba(255, 255, 255, 0.65); backdrop-filter: blur(12px); border-radius: 24px; padding: 25px; border: 1px solid rgba(255, 255, 255, 0.8); box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07); }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
st.markdown('<p class="main-title">OncoDiabetes Nexus</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Yapay Zeka Destekli Yeni Nesil Onkoloji ve Diyabet Ekosistemi</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 1.5, 1.3], gap="large")

# ----- SOL KOLON: VERİ GİRİŞİ -----
with col1:
    with st.container():
        st.markdown("### 🧑‍⚕️ Hasta Profili")
        glu = st.number_input("🩸 Açlık Glukoz", 50, 300, 110, step=5)
        bmi = st.number_input("⚖️ Vücut Kitle Endeksi", 15.0, 50.0, 24.5, step=0.5)
        age = st.slider("🎂 Yaş", 18, 90, 35)
        hesapla_btn = st.button("Analizi Başlat ⚡", use_container_width=True)

# ----- ORTA KOLON: RİSK & XAI -----
with col2:
    with st.container():
        st.markdown("### 🎯 Teşhis Merkezi")
        if hesapla_btn:
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            input_data = [[1, glu, 70, 20, 80, bmi, 0.5, age]]
            risk = model.predict_proba(input_data)[0][1]
            st.session_state['risk'] = risk
            st.session_state['glu'] = glu
            
            if risk > 0.5:
                st.error("🚨 Kritik Risk")
                st.metric(label="Olasılık", value=f"%{risk*100:.1f}")
            else:
                st.success("✅ Durum Stabil")
                st.metric(label="Olasılık", value=f"%{risk*100:.1f}")
            
            st.info(coordinate_agents(risk, glu))
        elif 'risk' in st.session_state:
            st.metric(label="Son Olasılık", value=f"%{st.session_state['risk']*100:.1f}")
            st.info(coordinate_agents(st.session_state['risk'], st.session_state['glu']))

# ----- SAĞ KOLON: AI ARAÇLARI (FORM İLE KORUMALI) -----
with col3:
    with st.container():
        st.markdown("### 📸 Görsel Analiz")
        # 1. KORUMA: Resim Yükleme Formu
        with st.form("image_form"):
            pic = st.file_uploader("Fotoğraf Yükle", type=['jpg','png', 'jpeg'], label_visibility="collapsed")
            if pic:
                st.image(pic, use_container_width=True)
            submit_img = st.form_submit_button("Analiz Et 🔍")
            
        if submit_img and pic:
            with st.spinner('İnceleniyor...'):
                st.success(predict_food(pic, MY_API_KEY))

    with st.container():
        st.markdown("### 📚 Tıbbi Asistan")
        # 2. KORUMA: Chat Formu
        with st.form("chat_form"):
            soru = st.text_input("Soru Sor:", placeholder="Diyabet hastası...")
            submit_chat = st.form_submit_button("Yanıtla 💬")
            
        if submit_chat and soru:
            with st.spinner('Taranıyor...'):
                cevap = get_ai_response("PDF bilgisi", soru, MY_API_KEY)
                st.info(f"**Asistan:** {cevap}")

# --- EN ALT: ŞEFFAF XAI AÇIKLAMASI ---
if os.path.exists(PLOT_PATH) and ('risk' in st.session_state):
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🔍 Karar Mekanizması (SHAP)"):
        st.image(PLOT_PATH, width=300)