import streamlit as st
from PIL import Image
import cv2
import numpy as np

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# تصميم CSS مخصص للشكل الفخم (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #ffffff; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stSelectbox, .stTextInput { background-color: #1a1a1a; }
    </style>
    """, unsafe_allow_stdio=True)

# نظام تبديل اللغة
lang = st.sidebar.radio("Choose Language / اختر اللغة", ["العربية", "English"])

if lang == "العربية":
    title = "👑 موقع ELKING MAN الملكي"
    desc = "منصتك المتكاملة للأناقة والذكاء الاصطناعي"
    tool1 = "🖼️ تحسين جودة الصور 8K"
    tool2 = "✂️ مصفف الشعر الذكي"
    tool3 = "👔 منسق الملابس الشخصي"
    tool4 = "🎬 صانع لقطات الفيديو الإبداعية"
else:
    title = "👑 ELKING MAN Official Site"
    desc = "Your Ultimate AI & Style Hub"
    tool1 = "🖼️ 8K Photo Enhancer"
    tool2 = "✂️ AI Smart Barber"
    tool3 = "👔 Personal Stylist"
    tool4 = "🎬 Creative Video Highlights"

st.title(title)
st.subheader(desc)

# --- القسم الأول: تحسين الصور ---
st.divider()
st.header(tool1)
uploaded_file = st.file_uploader("Upload Image / ارفع صورتك", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original / الصورة الأصلية", use_column_width=True)
    if st.button("Enhance to 8K / تحسين الجودة الآن"):
        with st.spinner('Processing... جاري المعالجة'):
            # هنا يتم استدعاء نموذج AI (مثل Real-ESRGAN)
            st.success("تم تحسين الصورة بنجاح! (محاكاة)")
            st.image(img, caption="8K Enhanced", use_column_width=True)

# --- القسم الثاني: مصفف الشعر ---
st.divider()
st.header(tool2)
st.write("اكتشف أكثر من 200 قصة شعر تناسب وجهك")
face_shape = st.selectbox("Face Shape / شكل وجهك", ["Oval / بيضاوي", "Square / مربع", "Round / دائري"])
if st.button("Show Styles / عرض القصات"):
    st.info(f"عرض أفضل 200 قصة تناسب الوجه {face_shape}...")
    # عرض صور افتراضية للقصات
    st.image("https://via.placeholder.com/150", caption="Style 1")

# --- القسم الثالث: منسق الملابس ---
st.divider()
st.header(tool3)
col1, col2 = st.columns(2)
with col1:
    place = st.text_input("Where are you going? / رايح فين؟")
    with_who = st.text_input("With whom? / مع مين؟")
with col2:
    meeting_type = st.radio("Meeting Type / نوع المقابلة", ["Official / مهمة", "Casual / شبابية"])

if st.button("Suggest Outfit / اختر لي ملابسي"):
    if "مهمة" in meeting_type or "Official" in meeting_type:
        st.success("الخيار الأفضل: بدلة سليم فيت كحلي، قميص أبيض، حذاء بني جلد.")
    else:
        st.success("الخيار الأفضل: تيشيرت أوفرسايز، بنطلون جينز فاتح، سنيكرز أبيض.")

# --- القسم الرابع: فيديوهات الألعاب والمسلسلات ---
st.divider()
st.header(tool4)
video_url = st.text_input("Paste Link (YouTube/TikTok) / ضع الرابط هنا")
content_type = st.selectbox("Design Type / نوع التصميم", ["Games / ألعاب", "Series / مسلسلات"])
if st.button("Create Highlights / صمم اللقطات"):
    st.warning("جاري تحليل الفيديو واستخراج أجمل اللقطات وتنسيقها...")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") # فيديو تجريبي
