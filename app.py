import streamlit as st
from PIL import Image

# 1. إعدادات الصفحة وربط جوجل (SEO)
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# إضافة كود التحقق من جوجل لكي يظهر الموقع في نتائج البحث
st.markdown("""
    <head>
        <meta name="google-site-verification" content="pVo9HIE1AxIICKu26Vq8NPCC" />
    </head>
    """, unsafe_allow_html=True)

# 2. تصميم CSS مخصص للشكل الملكي
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
    .stButton>button:hover { background-color: #b8962e; color: white; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stSelectbox, .stTextInput, .stRadio { background-color: #1a1a1a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام تبديل اللغة
lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"])

if lang == "العربية":
    title = "👑 موقع ELKING MAN الملكي"
    desc = "منصتك المتكاملة للأناقة والذكاء الاصطناعي"
    tool1 = "🖼️ تحسين جودة الصور 8K"
    tool2 = "✂️ مصفف الشعر الذكي"
    tool3 = "👔 منسق الملابس الشخصي"
    btn_action = "تحليل الآن"
else:
    title = "👑 ELKING MAN Official Site"
    desc = "Your Ultimate AI & Style Hub"
    tool1 = "🖼️ 8K Photo Enhancer"
    tool2 = "✂️ AI Smart Barber"
    tool3 = "👔 Personal Stylist"
    btn_action = "Analyze Now"

st.title(title)
st.subheader(desc)

# الأقسام الأساسية
st.divider()
st.header(tool1)
uploaded_file = st.file_uploader("Upload / ارفع صورتك", type=['jpg', 'png', 'jpeg'])

st.divider()
st.header(tool2)
st.selectbox("Face Shape / شكل الوجه", ["Oval", "Square", "Round"])
if st.button(btn_action):
    st.info("Searching for styles... جاري البحث")

st.divider()
st.markdown("<p style='text-align: center;'>© 2026 ELKING MAN</p>", unsafe_allow_html=True)
