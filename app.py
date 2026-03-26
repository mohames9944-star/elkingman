import streamlit as st
import time
import random
from PIL import Image, ImageEnhance, ImageFilter

# 1. إثبات الملكية لجوجل (السطر اللي بعته وضعتُه هنا بشكل صحيح برمجياً)
st.markdown('<meta name="google-site-verification" content="3g6rM7Q4DsBKCzNPhdOZl48qCq96iYQ2JYslHKfswbc" />', unsafe_allow_html=True)

# 2. إعدادات الصفحة
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# 3. تصميم الستايل (الأسود والذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #e0e0e0; }
    .stButton>button { 
        background-color: #D4AF37; color: black; border-radius: 20px; 
        font-weight: bold; width: 100%; padding: 12px; transition: 0.4s;
    }
    .stButton>button:hover { background-color: #fff; color: #D4AF37; box-shadow: 0 0 20px #D4AF37; }
    .result-card { background: #1a1a1a; padding: 20px; border-radius: 15px; border-right: 5px solid #D4AF37; margin-top: 15px; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 ELKING MAN - PRESTIGE AI")

# التبويبات (الأدوات الشغالة)
tabs = st.tabs(["🖼️ وضوح الصور", "✂️ مصفف الشعر", "👔 منسق الملابس"])

# --- أداة الصور ---
with tabs[0]:
    st.header("توضيح الصور وإزالة التشويش")
    img_file = st.file_uploader("ارفع الصورة هنا", type=['jpg', 'png', 'jpeg'], key="img_final")
    if img_file:
        col1, col2 = st.columns(2)
        with col1: st.image(img_file, caption="قبل", use_container_width=True)
        if st.button("🚀 رفع الجودة"):
            img = Image.open(img_file).convert("RGB")
            img = ImageEnhance.Sharpness(img).enhance(5.5)
            img = ImageEnhance.Contrast(img).enhance(1.4)
            img = img.filter(ImageFilter.DETAIL)
            with col2:
                st.image(img, caption="بعد HD", use_container_width=True)
                st.success("تم التحسين!")

# --- أداة الحلاقة ---
with tabs[1]:
    st.header("كتالوج الحلاقة")
    f_shape = st.selectbox("شكل وجهك:", ["بيضاوي", "مربع", "دائري", "قلب"], key="hair_final")
    h_styles = ["Modern Pompadour", "Classic Slick Back", "Taper Fade", "Textured Quiff"]
    if st.button("🔄 اقتراح قصة"):
        res = random.choice(h_styles)
        st.markdown(f"<div class='result-card'><h3>🤵 القصة المقترحة: {res}</h3></div>", unsafe_allow_html=True)

# --- أداة الملابس ---
with tabs[2]:
    st.header("منسق المظهر")
    st.text_input("المناسبة؟", key="wear_final")
    if st.button("🕺 نسق لي طقم اليوم"):
        tops = ["بليزر كحلي", "قميص أبيض", "هودي أسود", "جاكيت جلد"]
        bottoms = ["جينز غامق", "قماش رمادي", "كارغو بيج", "أسود كلاسيك"]
        t, b = random.choice(tops), random.choice(bottoms)
        st.markdown(f"<div class='result-card'><h3>👔 ستايل الملك:</h3><p>{t} مع {b}</p></div>", unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align: center;'>© 2026 ELKING MAN</p>", unsafe_allow_html=True)
