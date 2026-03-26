import streamlit as st
from PIL import Image

# 1. كود التحقق الخاص بجوجل (هام جداً للأرشفة)
st.markdown('<meta name="google-site-verification" content="3g6rM7Q4DsBKCzNPhdOZl48qCq96iYQ2JYslHKfswbc" />', unsafe_allow_html=True)

# 2. إعدادات الصفحة الفخمة
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# 3. تصميم CSS الملكي (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #ffffff; }
    .stButton>button { 
        background-color: #D4AF37; 
        color: black; 
        border-radius: 10px; 
        font-weight: bold; 
        width: 100%; 
        border: none;
        padding: 10px;
    }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stSelectbox, .stTextInput, .stRadio { background-color: #1a1a1a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# نظام تبديل اللغة
lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"])

if lang == "العربية":
    title, desc = "👑 موقع ELKING MAN الملكي", "منصتك المتكاملة للأناقة والذكاء الاصطناعي"
    tool1, tool2 = "🖼️ تحسين جودة الصور 8K", "✂️ مصفف الشعر الذكي"
    tool3, tool4 = "👔 منسق الملابس الشخصي", "🎬 صانع لقطات الفيديو"
else:
    title, desc = "👑 ELKING MAN Official Site", "Your Ultimate AI & Style Hub"
    tool1, tool2 = "🖼️ 8K Photo Enhancer", "✂️ AI Smart Barber"
    tool3, tool4 = "👔 Personal Stylist", "🎬 Creative Video Highlights"

st.title(title)
st.subheader(desc)

# --- محتوى الموقع ---
st.divider()
st.header(tool1)
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    st.image(Image.open(uploaded_file), width=400)
    if st.button("Enhance Now"): st.success("✅ جاري التحسين بتقنية 8K...")

st.divider()
st.header(tool2)
st.selectbox("Face Shape", ["Oval", "Square", "Round"])
if st.button("Show Styles"): st.info("✨ يتم الآن عرض أفضل القصات لوجهك...")

st.divider()
st.header(tool3)
st.text_input("Where are you going?")
if st.button("Suggest Outfit"): st.success("🤴 الستايل الملكي: بدلة كحلي وقميص أبيض.")

st.divider()
st.header(tool4)
st.text_input("Video Link")
if st.button("Create"): st.warning("⚡ جاري المونتاج التلقائي...")
