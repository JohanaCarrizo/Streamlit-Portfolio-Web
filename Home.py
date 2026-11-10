import base64
from pathlib import Path
import streamlit as st


# Función fuera del main y con caché (ideal si crece el proyecto)
@st.cache_data
def img_to_base64(path):
  with open(path, "rb") as img_file:
    return base64.b64encode(img_file.read()).decode("utf-8")


def main():
  st.set_page_config(page_title="MyPortfolio", page_icon=":camera_flash:", layout="wide", initial_sidebar_state="expanded")

  st.markdown(
      """
      <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

      html, body, [class*="css"] {
          font-family: 'Plus Jakarta Sans', sans-serif;
      }

      /* Ocultar elementos predeterminados de Streamlit */
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}

      /* Estilo de la barra lateral */
      [data-testid="stSidebar"] {
          background-color: #1e293b;
          border-right: 1px solid #334155;
      }

      /* Contenedor tipo Hero con imagen de fondo y capa oscura */
      .hero-background {
          background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), 
                            url('https://images.unsplash.com/photo-1471341971476-ae15ff5dd4ea?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D');
          background-size: cover;
          background-position: center;
          border-radius: 20px;
          padding: 5rem 2rem;
          text-align: center;
          box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
          margin-top: 1rem;
      }

      /* Marco elegante alrededor del título principal */
      .title-box {
          display: inline-block;
          border: 2px solid #38bdf8; /* Color del marco (puedes cambiarlo a verde si prefieres) */
          padding: 1.5rem 3rem;
          margin-bottom: 2rem;
          border-radius: 4px;
          background-color: rgba(15, 23, 42, 0.4);
          backdrop-filter: blur(4px);
      }
      </style>
      """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
      st.markdown(
          """
          <div class="hero-background">
              <div class="title-box">
                  <h1>Hola! <span style="color: #38bdf8; "text-align: center;">Mi nombre es</span></h1>
                  <h1 class="hero-title"> BEN KARSTEN</h1>
              </div>
          </div>
          """,
          unsafe_allow_html=True,
      )

      select = st.pills("", ["Fotógrafo Profesional", "Escenógrafo", "Arquitecto"])




if __name__ == "__main__":
  main()