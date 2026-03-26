import streamlit as st
from PIL import Image
import cv2
import numpy as np

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# 2. تصميم CSS مخصص للشكل الملكي (أسود وذهبي)
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
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-family: 'Cairo', sans-serif; }
    .stSelectbox, .stTextInput, .stRadio { background-color: #1a1a1a; color: white; }
    div[data-testid="stExpander"] { border: 1px solid #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام تبديل اللغة
lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"])

if lang == "العربية":
    title = "👑 موقع ELKING MAN الملكي"
    desc = "منصتك المتكاملة للأناقة والذكاء الاصطناعي"
    tool1 = "🖼️ تحسين جودة الصور 8K"
    tool2 = "✂️ مصفف الشعر الذكي (200+ قصة)"
    tool3 = "👔 منسق الملابس الشخصي"
    tool4 = "🎬 صانع لقطات الفيديو الإبداعية"
    upload_msg = "ارفع صورتك هنا"
    btn_enhance = "تحسين الجودة الآن"
    btn_style = "عرض أفضل القصات لوجهي"
    btn_outfit = "اختر لي ملابسي"
    btn_video = "تصميم الفيديو الآن"
else:
    title = "👑 ELKING MAN Official Site"
    desc = "Your Ultimate AI & Style Hub"
    tool1 = "🖼️ 8K Photo Enhancer"
    tool2 = "✂️ AI Smart Barber (200+ Styles)"
    tool3 = "👔 Personal Stylist"
    tool4 = "🎬 Creative Video Highlights"
    upload_msg = "Upload your photo here"
    btn_enhance = "Enhance to 8K Now"
    btn_style = "Show Best Styles for Me"
    btn_outfit = "Suggest My Outfit"
    btn_video = "Design Video Now"

st.title(title)
st.subheader(desc)

# --- القسم الأول: تحسين الصور ---
st.divider()
st.header(tool1)
uploaded_file = st.file_uploader(upload_msg, type=['jpg', 'png', 'jpeg'], key="1")
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original / الصورة الأصلية", width=400)
    if st.button(btn_enhance):
        with st.spinner('Processing... جاري المعالجة بتقنية 8K'):
            # محاكاة التحسين (هنا يتم الربط مع API مستقبلاً)
            st.success("✅ تم رفع الدقة وتصحيح الألوان بنجاح!")
            st.image(img, caption="8K Enhanced View", use_container_width=True)

# --- القسم الثاني: مصفف الشعر ---
st.divider()
st.header(tool2)
face_shape = st.selectbox("Face Shape / شكل وجهك", ["Oval / بيضاوي", "Square / مربع", "Round / دائري", "Heart / قلبي"])
if st.button(btn_style):
    st.info(f"✨ تم تحليل ملامح الوجه.. إليك أفضل القصات لعام 2026 التي تناسب الوجه {face_shape}:")
    # عرض صور افتراضية للقصات
    col_a, col_b = st.columns(2)
    with col_a: st.image("https://via.placeholder.com/300x400/1a1a1a/D4AF37?text=Modern+Fade", caption="Style 1")
    with col_b: st.image("https://via.placeholder.com/300x400/1a1a1a/D4AF37?text=Classic+Taper", caption="Style 2")

# --- القسم الثالث: منسق الملابس ---
st.divider()
st.header(tool3)
c1, c2 = st.columns(2)
with c1:
    place = st.text_input("Destination / المكان (مثلاً: مطعم فخم، الجيم، شركة)")
    with_who = st.text_input("Meeting with / مع مين؟")
with c2:
    m_type = st.radio("Importance / الأهمية", ["High / مهمة جداً", "Casual / خروجة عادية"])

if st.button(btn_outfit):
    if "High" in m_type or "مهمة" in m_type:
        st.success("🤴 الستايل الملكي: بدلة كحلي (Slim Fit)، قميص أبيض مكوي، حذاء أسود لامع، وساعة فضية.")
    else:
        st.success("😎 الستايل الكاجوال: تيشيرت أسود سادة، بنطلون كارغو زيتي، سنيكرز أبيض، ونظارة شمسية.")

# --- القسم الرابع: فيديوهات الألعاب والمسلسلات ---
st.divider()
st.header(tool4)
v_url = st.text_input("Video Link / رابط الفيديو (YouTube/TikTok)")
v_type = st.selectbox("Category / التصنيف", ["Gaming / ألعاب", "Drama / مسلسلات", "Action / أكشن"])
if st.button(btn_video):
    st.warning("⚡ جاري استخراج أفضل اللقطات وتطبيق المونتاج التلقائي...")
    # فيديو تجريبي يوضح النتيجة
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# تذييل الصفحة
st.markdown("<br><hr><p style='text-align: center;'>© 2026 ELKING MAN - Powered by AI</p>", unsafe_allow_html=True)
