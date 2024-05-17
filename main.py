#!/user/bin/env python

import streamlit as st

st.set_page_config(layout="wide",)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #111111;
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
color: white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
color: white;
}}
h1 {{
color: white;
}}
h2 {{
color: white;
}}
a.stDownloadButton {{
  color: white !important;
  text-decoration: none;
}}
a.stDownloadButton:hover {{
  color: black !important;
}}
.img-container {{
  width: 100%;
  height: 450px;
  overflow: hidden;
}}
.img-container img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
.img-container:hover img {{
  transform: scale(1.1); 
}}
.transition {{
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
article div.box-wrapper {{
  width: 100%;
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  padding: 20px;
}}
div.box-wrapper div.box {{
  width: 33%;
  height: auto;
  overflow: hidden;
  position: relative;
  display: inline-block;
}}
div.box-wrapper div.box:hover {{
  z-index: 999;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
}}
div.box img {{
  width: 100%;
  height: auto;
}}
h3 {{
color: white;
}}
.center {{
  display: flex;
  justify-content: center;
}}
.stDownloadButton {{
  background-color: #000000;
  color: white;
  border: solid;
  border-color: #ffffff;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
}}
.stDownloadButton:hover {{
  background-color: #ffffff;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Pedro Schreier")

col1, col2 = st.columns(2)

with col1:
    #st.image("https://i.ibb.co/rpJJ5Fk/Pedro-Shooting-2-76.jpg")
    st.markdown(
        f'<div class="img-container"><img src="https://i.ibb.co/rpJJ5Fk/Pedro\
        -Shooting-2-76.jpg" style="width:90%; height:100%; \
                     object-fit:cover;"></div>',
        unsafe_allow_html=True
    )

with col2:
    st.header("Bom dia :flag-br:")
    st.subheader("Actor, Investor & Writer")
    content = """
    **Pedro Schreier** ist ein deutsch-/brasilianischer
    Schauspieler, Autor und Filmproduzent mit Sitz in Deutschland.

    """
    st.markdown(content)

    col3, col4 = st.columns(2)

    with (col3):
        st.header("Film")
        st.subheader("Rave | 2024 | Feature Film")
        content = """
        **Regie**: Nikias Chryssos, Viktor Jakovleski \
        **Produktion**: Telospictures, Friendship Films GmbH \
        **Rolle**: Security (BP)
        """
        st.markdown(content)

        st.subheader("The Survivors | 2020 | Indie")
        content = """
                **Regie**: Pedro Schreier \
                **Produktion**: Global Production Pictures \
                **Rolle**: Sam (SR)
                """
        st.markdown(content)
    with col4:
        st.header("Commercial")
        st.subheader("Hidrofugal | 2021 ")
        content = """
                **Regie**: Claas Ortmann \
                **Produktion**: Tony Petersen Film GmbH \
                **Rolle**: The Model (SR)
                """
        st.markdown(content)
        st.header("Musikvideo")
        st.subheader("Houseparty | 2021 ")
        content = """
                       **Rolle**: The Model & Dancer (SR)
                       """
        st.markdown(content)

# Offer a download button for a PDF file

pdf_url = "https://www.dropbox.com/scl/fi/yfk7kw74l8rbe9fzxb3g9/\
#Pedro-Schreier-Crew-United-Profil-626413.pdf?rlkey=7ejt3m6joi3f6f22w5f1yubwb&\
#st=1gijh59r&dl=0"
#st.markdown(f" [Download **Vita**]({pdf_url})")

# Center and style the download button
st.markdown(f"""
<div class="center">
    <a href="{pdf_url}" download="Pedro-Schreier-Crew-United-Profil-626413.pdf"\
     class="stDownloadButton">
        Download Vita
    </a>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Photos", "Videos"])

with tab1:
   st.subheader("Photos")
   st.markdown("Made in :flag-br:")
   col1, col2, col3, col4 = st.columns(4)
   with col1:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/ftDY32r/IMG\
           -0223-3.jpg" style="width:100%; height:100%; \
           object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col2:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/nQ64cxM/IMG\
           -0225-2.png" style="width:100%; height:100%; \
                 object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col3:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/mbSGZ0Q/716\
           -CFCE6-BD73-4-E76-BCCC-27-F0-\
       FC018424.jpg" style="width:100%; height:100%; \
                        object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col4:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/wp2rnHj/ef9\
           0c5d9-6bec-44a6-89b4-\
       ce1aa908e9d2-3.jpg" style="width:100%; height:100%; \
                               object-fit:cover;"></div>',
           unsafe_allow_html=True
       )

with tab2:
   st.header("Videos")
   col1, col2, col3 = st.columns(3)
   with col1:
       st.video("https://youtu.be/ByHh7jh3E9E")
   with col2:
       st.video("https://youtu.be/0DhkGtY-B84")
   with col3:
       st.video("https://youtu.be/uNpIaQk6ikg")

little = """
    www.pedroschreier.de | 2024
    """
with st.expander("Contact"):
    st.write('''
        schreierpedro@gmail.com
    ''')
st.write(little)
