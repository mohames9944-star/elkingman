import streamlit as st
import time
import random
from PIL import Image, ImageEnhance, ImageFilter

# 1. إعدادات جوجل والصفحة (ثابتة للأرشفة)
st.markdown('<meta name="google-site-verification" content="3g6rM7Q4DsBKCzNPhdOZl48?qCq96iYQ2JYslHKfswbc" />', unsafe_allow_html=True)
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# 2. تصميم CSS ملكي (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #e0e0e0; }
    .stButton>button { 
        background-color: #D4AF37; color: black; border-radius: 20px; 
        font-weight: bold; width: 100%; padding: 12px; transition: 0.4s;
    }
    .stButton>button:hover { background-color: #fff; color: #D4AF37; box-shadow: 0 0 20px #D4AF37; }
    .result-card { background: #1a1a1a; padding: 20px; border-radius: 15px; border-right: 5px solid #D4AF37; margin-top: 15px; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-family: 'Cairo', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1a1a1a; border-radius: 10px; color: white; padding: 10px 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 ELKING MAN - THE ROYAL HUB")

# إنشاء التبويبات (الأدوات)
tabs = st.tabs(["🖼️ وضوح الصور", "✂️ مصفف الشعر", "👔 منسق الملابس", "🎬 المونتاج والتحميل"])

# --- 1. أداة الصور (إزالة التشويش) ---
with tabs[0]:
    st.header("توضيح الصور وإزالة التشويش")
    img_file = st.file_uploader("ارفع صورتك للمعالجة", type=['jpg', 'png', 'jpeg'], key="img_tool")
    if img_file:
        col1, col2 = st.columns(2)
        with col1: st.image(img_file, caption="الصورة الأصلية", use_container_width=True)
        if st.button("🚀 رفع الجودة الآن"):
            img = Image.open(img_file).convert("RGB")
            img = ImageEnhance.Sharpness(img).enhance(5.5)
            img = ImageEnhance.Contrast(img).enhance(1.4)
            img = img.filter(ImageFilter.DETAIL)
            with col2:
                st.image(img, caption="النتيجة الملكية HD", use_container_width=True)
                st.success("تم تحسين الوضوح بنجاح!")

# --- 2. أداة الحلاقة (نتائج متجددة) ---
with tabs[1]:
    st.header("كتالوج الحلاقة الذكي")
    f_shape = st.selectbox("شكل وجهك:", ["بيضاوي", "مربع", "دائري", "قلب"], key="hair_tool")
    hair_db = {
        "بيضاوي": ["Modern Pompadour", "Classic Side Part", "Slick Back High Fade", "Tapered Waves"],
        "مربع": ["Buzz Cut with Line", "Crew Cut", "High and Tight", "Textured Undercut"],
        "دائري": ["High Quiff", "Faux Hawk Fade", "Side Swept Under-cut", "Spiky Top"],
        "قلب": ["Mid Length Flow", "Long Fringe", "Messy Scissor Cut", "Tapered Sides"]
    }
    if st.button("🔄 اقترح قصة جديدة"):
        res = random.choice(hair_db[f_shape])
        st.markdown(f"<div class='result-card'><h3>🤵 القصة المقترحة: {res}</h3><p>ستايل ملكي فريد يناسبك.</p></div>", unsafe_allow_html=True)

# --- 3. أداة الملابس (تنسيقات متغيرة) ---
with tabs[2]:
    st.header("منسق المظهر الشخصي")
    occ = st.text_input("المناسبة؟ (مثلاً: فرح، جيم، جامعة)", key="wear_tool")
    if st.button("🕺 نسق لي طقم اليوم"):
        tops = ["بليزر كحلي فخم", "قميص أبيض سليم فيت", "هودي أسود عصري", "جاكيت جلد أسود"]
        bottoms = ["بنطلون جينز غامق", "بنطلون قماش رمادي", "بنطلون كارغو بيج", "بنطلون أسود كلاسيك"]
        shoes = ["سنيكرز أبيض ناصع", "حذاء كلاسيك بني", "هاف بوت أسود", "سنيكرز مريح"]
        st.markdown(f"""<div class='result-card'>
            <h3>👔 ستايل الملك لـ {occ}:</h3>
            <p>• {random.choice(tops)} مع {random.choice(bottoms)} وحذاء {random.
