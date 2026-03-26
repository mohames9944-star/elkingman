import streamlit as st
import time
import random
from PIL import Image, ImageEnhance, ImageFilter

# 1. كود التحقق من جوجل وإعدادات الصفحة
st.markdown('<meta name="google-site-verification" content="3g6rM7Q4DsBKCzNPhdOZl48qCq96iYQ2JYslHKfswbc" />', unsafe_allow_html=True)
st.set_page_config(page_title="ElKing Man | الملك", page_icon="👑", layout="wide")

# 2. تصميم CSS ملكي فخم
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #e0e0e0; }
    .stButton>button { 
        background-color: #D4AF37; color: black; border-radius: 20px; 
        font-weight: bold; width: 100%; border: none; padding: 12px;
        transition: 0.4s;
    }
    .stButton>button:hover { background-color: #fff; color: #D4AF37; box-shadow: 0 0 20px #D4AF37; transform: translateY(-2px); }
    .result-card { 
        background: #1a1a1a; padding: 20px; border-radius: 15px; 
        border-right: 5px solid #D4AF37; margin-top: 15px; border-bottom: 2px solid #D4AF37;
    }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-family: 'Cairo', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 ELKING MAN - AI PRESTIGE")

tabs = st.tabs(["🖼️ وضوح الصور", "✂️ كتالوج الحلاقة", "👔 منسق الملابس", "🎬 مونتاج الروابط"])

# --- 1. قسم الصور (تحسين الحدة) ---
with tabs[0]:
    st.header("إزالة التشويش وتوضيح التفاصيل")
    img_file = st.file_uploader("ارفع صورتك للمعالجة", type=['jpg','png','jpeg'])
    if img_file:
        col1, col2 = st.columns(2)
        with col1: st.image(img_file, caption="قبل المعالجة", use_container_width=True)
        if st.button("🚀 تحسين الوضوح فوراً"):
            with st.spinner("جاري تنظيف الصورة..."):
                img = Image.open(img_file).convert("RGB")
                img = ImageEnhance.Sharpness(img).enhance(3.0)
                img = ImageEnhance.Contrast(img).enhance(1.2)
                img = img.filter(ImageFilter.DETAIL)
                time.sleep(1)
                with col2:
                    st.image(img, caption="النتيجة الملكية", use_container_width=True)
                    st.success("تم رفع جودة التفاصيل!")

# --- 2. كتالوج الحلاقة (نتائج عشوائية متجددة) ---
with tabs[1]:
    st.header("أفكار حلاقة لعام 2026")
    f_shape = st.selectbox("شكل وجهك:", ["بيضاوي", "مربع", "دائري", "طويل"])
    
    hair_ideas = {
        "بيضاوي": ["Modern Pompadour", "Classic Slick Back", "Low Taper Fade", "Textured Quiff", "Buzz Cut with Beard"],
        "مربع": ["High Skin Fade", "Crew Cut", "Undercut with Texture", "Short Fringe", "Classic Side Part"],
        "دائري": ["Spiky High Top", "Faux Hawk Fade", "Pompadour with Hard Part", "Side Swept Under-cut", "Messy Crop"],
        "طويل": ["Side Part Scissor Cut", "Man Bun", "Mid Fade with Fringe", "Wavy Shag", "Natural Curls with Taper"]
    }
    
    if st.button("🔄 فكرة حلاقة غير متوقعة"):
        res = random.choice(hair_ideas[f_shape])
        st.markdown(f"<div class='result-card'><h3>🤵 القصة المقترحة: {res}</h3><p>تم اختيار هذه القصة بناءً على ملامحك لتعطيك كاريزما وهيبة ملكية.</p></div>", unsafe_allow_html=True)

# --- 3. منسق الملابس (تنسيقات عشوائية ذكية) ---
with tabs[2]:
    st.header("منسق المظهر الذكي")
    occ = st.text_input("المناسبة (مثلاً: مقابلة، جيم، خروجة ليلية)")
    if st.button("🕺 نسق لي طقم اليوم"):
        top = ["قميص أبيض سليم فيت", "هودي أسود أوفرسايز", "بليزر كحلي فخم", "تيشيرت زيتي سادة", "جاكيت جلد أسود"]
        pants = ["بنطلون جينز غامق", "بنطلون قماش رمادي", "بنطلون كارغو بيج", "بنطلون أسود كلاسيك"]
        shoes = ["سنيكرز أبيض", "هاف بوت بني", "حذاء أسود لامع", "بوت عسكري عصري"]
        
        st.markdown(f"""<div class='result-card'>
            <h3>👔 ستايل الملك لـ {occ}:</h3>
            <p>• <b>القطعة العلوية:</b> {random.choice(top)}</p>
            <p>• <b>البنطلون:</b> {random.choice(pants)}</p>
            <p>• <b>الحذاء:</b> {random.choice(shoes)}</p>
            </div>""", unsafe_allow_html=True)

# --- 4. مونتاج الروابط (جديد وسريع) ---
with tabs[3]:
    st.header("المونتاج الذكي للروابط")
    v_url = st.text_input("ضع رابط الفيديو هنا (YouTube, TikTok, Video Link)")
    v_mode = st.multiselect("اختر العمليات:",
