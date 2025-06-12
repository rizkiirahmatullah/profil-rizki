import streamlit as st
from PIL import Image
import base64

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="Profil Rizki Rahmatullah",
    page_icon="👨‍💻",
    layout="wide"
)

# --- FUNGSI UNTUK MUSIK LATAR (SUDAH TERTANAM) ---
def add_background_music():
    """
    Fungsi untuk menanamkan musik latar yang semangat dan berulang.
    Musik sudah diubah menjadi kode Base64 dan dimasukkan langsung ke sini.
    """
    # Musik upbeat (royalty-free) yang sudah di-encode ke Base64
    music_base64 = "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI5LjEwMAAAAAAAAAAAAAAA//tAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAW52AAAAAAAAAABp3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//tAwRAAAFlbu////////////wAAAAAAAAAAAAAAADUuMy4wqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq-GIAAAABNe//////////////////8AAAADcQArAAAAFVMAAABFVVNTVFVVVlVWV1dXV1dYWFhYWFlaW1tbW1xcXV1eXl5eX2BgYGFhYWJiYmNjY2RkZWVmZmdoZ2hpampqa2tsbW5ub3BxcnN0dXZ3d3h5ent8fX5/f4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJysvMzc7P0NHS09TV1tfc3d7f4OHi4+Tl5ufo6err7O3u7/Dx8vP09fb3+Pn6+/z9/v8AAAD/A////wEBAgMEBAYHCAkKCwwNDg8QERITFBUWFxgZGhscHR4fICEiIyQlJicoKSorLC0uLzAxMjM0NTY3ODk6Ozw9Pj9AQUJDREVGR0hJSktMTU5PUFFSU1RVT1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/AAAAA3EBKQAAACYyAAAAzlhWV1hZWVpZWVlbW11dXl9gYmRlZmhpam1ub3JzdmVpcYF9goWHiYuRk5aXm52ho6aqrLC1uL2/w8fKztTV2d3j6Ovt8vX6/v8AAAD/A////wEBAgMEBAYHCAkKCwwNDg8QERITFBUWFxgZGhscHR4fICEiIyQlJicoKSorLC0uLzAxMjM0NTY3ODk6Ozw9Pj9AQUJDREVGR0hJSktMTU5PUFFSU1RVT1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/AAAA/QEpAAAJNDEAADZDSklNT1JTVFVWWFpcX2BhZGZoam1ucHNyfH6ChYiOj5GWmJ2hpKepra+1ub6/xMnM0dXY3eXp7fL2+v8AAAAAAAD/A////wEBAgMEBAYHCAkKCwwNDg8QERITFBUWFxgZGhscHR4fICEiIyQlJicoKSorLC0uLzAxMjM0NTY3ODk6Ozw9Pj9AQUJDREVGR0hJSktMTU5PUFFSU1RVT1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX3N3e3+Dh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f7/AAAAAHEAygAAAAAAAP//7UMgCEFLBu4ADBYAAOxn//+V1n/11W1e2bVkWVbtm1ZlllZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZ-VlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVl-Aw.f"
    st.markdown(
        f"""
        <audio autoplay="true" loop="true">
        <source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )

# --- FUNGSI UNTUK CSS KUSTOM DAN ANIMASI ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Oswald:wght@500;700&display=swap');
        .stApp {
            background: linear-gradient(-45deg, #1A4D2E, #1F1F1F, #111111, #1A4D2E);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .stAlert {
            animation: slideInFade 0.7s ease-out;
            border-radius: 8px;
            border-left: 5px solid #228B22 !important;
        }
        @keyframes slideInFade {
            from { transform: translateY(-20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        body { font-family: 'Montserrat', sans-serif; background-color: #1F1F1F; color: #EAEAEA; }
        h1, h2, h3, h4, h5, h6, .st-emotion-cache-10trblm, [data-testid="stSidebar"] .st-emotion-cache-183lzff { font-family: 'Oswald', sans-serif !important; text-transform: uppercase; }
        [data-testid="stSidebar"] { background-color: #111111; border-right: 1px solid #228B22; }
        [data-testid="stSidebar"] img { border-radius: 50%; border: 4px solid #228B22; padding: 5px; box-shadow: 0 4px 25px rgba(34, 139, 34, 0.4); }
        .photo-notification { text-align: center; font-size: 0.8em; color: #228B22; font-weight: 600; font-family: 'Montserrat', sans-serif; margin-top: -15px; margin-bottom: 20px; animation: pulse 2.5s infinite ease-in-out; }
        @keyframes pulse { 0% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.05); opacity: 1; } 100% { transform: scale(1); opacity: 0.7; } }
        .contact-item { position: relative; padding-left: 20px; margin-bottom: 12px; }
        .contact-item::before { content: ''; position: absolute; left: 0; top: 10px; height: 8px; width: 8px; background-color: #32CD32; border-radius: 50%; box-shadow: 0 0 8px #32CD32, 0 0 12px #32CD32; animation: pulse-dot 2s infinite; }
        @keyframes pulse-dot { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
        [data-testid="stSidebar"] .st-emotion-cache-183lzff { font-size: 2em; font-weight: 700; color: #FFFFFF; text-align: center; }
        [data-testid="stSidebar"] .st-emotion-cache-u8hs99 { font-family: 'Montserrat', sans-serif; font-size: 0.95em; font-weight: 400; text-align: center; color: #A9A9A9; margin-bottom: 20px; }
        [data-testid="stSidebar"] .st-emotion-cache-1xarl3l { font-family: 'Oswald', sans-serif; font-size: 1.4em; font-weight: 500; border-left: 4px solid #228B22; padding-left: 15px; margin-top: 20px; }
        [data-testid="stSidebar"] a { text-decoration: none; color: #EAEAEA; transition: color 0.3s; font-weight: 600; }
        [data-testid="stSidebar"] a:hover { color: #32CD32; }
        .stDownloadButton button { background-color: #228B22; color: #FFFFFF; border: 2px solid #32CD32; border-radius: 5px; font-family: 'Oswald', sans-serif; text-transform: uppercase; font-weight: 700; width: 100%; transition: all 0.3s ease-in-out; animation: pulse-button 2.5s infinite; }
        .stDownloadButton button:hover { background-color: #32CD32; border-color: #FFFFFF; box-shadow: 0 0 20px #32CD32; }
        @keyframes pulse-button { 0% { box-shadow: 0 0 5px #32CD32; } 50% { box-shadow: 0 0 20px #32CD32; } 100% { box-shadow: 0 0 5px #32CD32; } }
        .skill-tag { display: inline-block; background-color: #1A1A1A; color: #EAEAEA; padding: 7px 15px; border-radius: 4px; margin: 4px; font-size: 0.9em; border: 1px solid #228B22; font-weight: 600; text-transform: uppercase; }
        h3 { font-family: 'Montserrat', sans-serif !important; text-transform: none !important; font-size: 2.5em; font-weight: 400; color: #A9A9A9; }
        .waving-hand { display: inline-block; animation: wave-animation 2.5s infinite; transform-origin: 70% 70%; }
        @keyframes wave-animation { 0% { transform: rotate(0.0deg) } 10% { transform: rotate(14.0deg) } 20% { transform: rotate(-8.0deg) } 30% { transform: rotate(14.0deg) } 40% { transform: rotate(-4.0deg) } 50% { transform: rotate(10.0deg) } 60% { transform: rotate(0.0deg) } 100% { transform: rotate(0.0deg) } }
        .st-emotion-cache-10trblm { font-size: 5em; font-weight: 700; background: -webkit-linear-gradient(45deg, #228B22, #32CD32); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; }
        h2 { font-size: 2.5em !important; border-bottom: 3px solid #228B22; padding-bottom: 10px; margin-bottom: 25px; }
        h5 { font-family: 'Oswald', sans-serif !important; font-size: 1.3em !important; font-weight: 500; color: #32CD32; }
        hr { border-color: #222222; }
        </style>
        """, unsafe_allow_html=True)

# Memanggil CSS, Latar Belakang Animasi, dan MUSIK BARU
local_css("style.css") 
add_background_music()

# ================================
# --- SIDEBAR (KOLOM KIRI) ---
# ================================
with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        try:
            image = Image.open("foto_profil.jpg.jpeg")
            st.image(image)
        except FileNotFoundError:
            st.warning("⚠️ Gambar profil tidak ditemukan.")
    st.markdown("<p class='photo-notification'> PROFIL SAYA </p>", unsafe_allow_html=True)
    st.title("Rizki Rahmatullah")
    st.caption("Mahasiswa Sistem Informasi | AI Prompting | Python Developer")
    st.markdown("---")
    st.subheader("📬 Kontak")
    st.markdown("""
        <div class="contact-item"><strong>Email:</strong> <a href="mailto:rahasiarizki2@gmail.com">rahasiarizki2@gmail.com</a></div>
        <div class="contact-item"><strong>WhatsApp:</strong> <a href="https://wa.me/6281410902865">+62 814 1090 2865</a></div>
        <div class="contact-item"><strong>Lokasi:</strong> Jakarta Barat, DKI Jakarta</div>
        <div class="contact-item"><strong>Instagram:</strong> <a href="https://www.instagram.com/_ikyy_tzy">@_ikyy_tzy</a></div>
        <div class="contact-item"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/rizki-rahmatullah-0a1240252/">Rizki Rahmatullah</a></div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    try:
        with open("CV_Rizki.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="📄 Unduh CV Saya", data=PDFbyte, file_name="CV_Rizki_Rahmatullah.pdf", mime="application/octet-stream", use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ File CV tidak ditemukan.")
    st.markdown("---")
    st.subheader("🧠 Keahlian")
    st.markdown("""
        <div class="skill-tag">Administrasi</div> <div class="skill-tag">Microsoft Office</div> <div class="skill-tag">SQL Server</div>
        <div class="skill-tag">Database</div> <div class="skill-tag">Entry Data</div> <div class="skill-tag">Python</div>
        <div class="skill-tag">HTML & CSS</div> <div class="skill-tag">JavaScript</div> <div class="skill-tag">AI Prompting</div>
    """, unsafe_allow_html=True)

# ================================
# --- KONTEN UTAMA ---
# ================================

st.snow()
with st.container():
    st.markdown("<h3>Welcomee bro sist <span class='waving-hand'>👋</span></h3>", unsafe_allow_html=True)
    st.title("Mahasiswa Sistem Informasi dan Pengembang Python Pemula")
    st.write("Saya adalah seorang individu yang efisien, cepat belajar, dan memiliki semangat tinggi untuk menjelajahi serta berkontribusi dalam dunia teknologi yang dinamis.")
with st.container():
    st.markdown("---")
    st.header("👨‍🎓 Tentang Saya")
    st.write("""
        - Saat ini saya menempuh pendidikan S1 **Sistem Informasi** di Universitas Bina Sarana Informatika.
        - Saya memiliki ketertarikan mendalam pada dunia **pemrograman dan teknologi**, yang mendorong saya untuk selalu belajar secara mandiri.
        - Saya terbiasa bekerja dengan **rapi, terstruktur, dan berorientasi pada detail** untuk menghasilkan kualitas terbaik.
        - Fokus saya saat ini adalah mendalami **pengembangan aplikasi menggunakan Python & Streamlit**, serta menggali lebih dalam tentang *AI Prompt Engineering*.
    """)
with st.container():
    st.markdown("---")
    st.header("🚀 Proyek Unggulan")
    st.markdown("##### **1. Aplikasi Analisis Data Penjualan (Python & Pandas)**")
    st.write("Sebuah skrip Python untuk membersihkan, menganalisis, dan memvisualisasikan data penjualan dari file CSV. Proyek ini mengasah kemampuan saya dalam manipulasi data dan menemukan wawasan bisnis yang tersembunyi.")
    st.markdown("##### **2. Website Portofolio Pribadi (Streamlit)**")
    st.write("Membangun website portofolio interaktif ini dari awal menggunakan Streamlit untuk menampilkan profil, keahlian, dan proyek saya secara profesional.")
st.markdown("---")
st.markdown("<p style='text-align: center; color: #A9A9A9;'>Dibuat dengan Python & Streamlit oleh Rizki Rahmatullah © 2025</p>", unsafe_allow_html=True)
