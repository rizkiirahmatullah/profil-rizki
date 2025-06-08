import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Fungsi untuk memuat animasi Lottie dari URL
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Atur halaman
st.set_page_config(page_title="Profil Rizki", page_icon="👋", layout="wide")

# ================================
# --- SIDEBAR ---
# ================================
with st.sidebar:
    # Pastikan nama file dan lokasi file gambar benar
    try:
        image = Image.open("foto_profil.jpg.jpeg")
        st.image(image, width=200)
    except:
        st.warning("❗ Gambar 'foto_profil.jpg.jpeg' tidak ditemukan.")

    st.title("Rizki Rahmatullah")
    st.caption("Mahasiswa Sistem Informasi | AI Prompting | Python Developer")
    st.markdown("---")
    
    st.subheader("📬 Kontak")
    st.markdown("""
- 📧 [Email](mailto:rahasiarizki2@gmail.com)  
- 📱 WhatsApp: +62 814 1090 2865  
- 📍 Jakarta Barat, DKI Jakarta  
- 🔗 [Instagram](https://www.instagram.com/_ikyy_tzy)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/rizki-rahmatullah-0a1240252/)
""")

    st.markdown("---")
    st.subheader("🧠 Keahlian")
    st.markdown("""
- Administrasi  
- Microsoft Office  
- SQL Server & Manajemen Database  
- Entry Data  
- Kerja Remote  
- Python Basic  
- HTML, CSS, JavaScript  
- AI Prompt Engineering
""")

# ================================
# --- HEADER UTAMA ---
# ================================
with st.container():
    st.subheader("Halo, saya Rizki 👋")
    st.title("Mahasiswa Sistem Informasi dan Pengembang Python Pemula")
    st.write(
        "Saya dapat bekerja secara efisien, cepat belajar, dan semangat tinggi menjelajah dunia teknologi."
    )

# ================================
# --- ANIMASI LOTTIE ---
# ================================
with st.container():
    st.markdown("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Tentang Saya")
        st.write(
            """
            Saya adalah mahasiswa S1 Sistem Informasi di Universitas Bina Sarana Informatika.
            Saya menyukai dunia pemrograman dan teknologi, terbiasa bekerja rapi dan belajar mandiri.
            """
        )
    



# ================================
# --- FOOTER ---
# ================================
with st.container():
    st.markdown("---")
    st.markdown("💼 Dibuat dengan  oleh **Rizki Rahmatullah** - 2025")
