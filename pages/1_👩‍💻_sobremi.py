import streamlit as st
from pathlib import Path

def sobre_mi():
    st.title("Sobre mi")

    # Obtiene la ruta de la carpeta actual del script
    current_dir = Path(__file__).parent
    image_path = current_dir / "imagenes" / "Foto_perfil.jpg"


    col_foto, col_descripcion = st.columns([1, 2])

    with col_foto:
        st.image(
            str(image_path),
            caption="Ben",
            alt="Foto-perfil",
        )

    with col_descripcion:
        st.write("Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum")

    st.subheader("El pasaje estándar Lorem Ipsum, usado desde el año 1966")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
             "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute "
             "irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
             "culpa qui officia deserunt mollit anim id est laborum.")
    st.subheader("Sección 1.10.32 de Finibus Bonorum et Malorum escrito por Cicero en el 45 antes de Cristo")
    st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis "
             "et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur "
             "magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, "
             "sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem "
             "ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil "
             "molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")

if __name__ == '__main__':
    sobre_mi()