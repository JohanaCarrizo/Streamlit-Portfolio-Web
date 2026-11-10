import streamlit as st

def cargar_proyectos():
    st.title('Proyectos')

    filtros = ["Todos", "Fotografía Callejera", "Naturaleza", "Experimental"]

    seleccion = st.pills("Filtros", filtros, default="Todos")

    if seleccion == "Todos":
        cargarFotoCallejeras()
        cargarFotoNaturaleza()
        cargarFotoExperimental()
    elif seleccion == "Fotografía Callejera":
        cargarFotoCallejeras()
    elif seleccion == "Naturaleza":
        cargarFotoNaturaleza()
    elif seleccion == "Experimental":
        cargarFotoExperimental()


def cargarFotoCallejeras():
    link_fotos = [
        "https://images.unsplash.com/photo-1794133294970-282c39f2961b?q=80&w=1528&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://images.unsplash.com/photo-1792778654289-69e281749be4?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://images.unsplash.com/photo-1790805574749-2b690b77cac1?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"
    ]

    # Recorremos la lista de 3 en 3 para armar filas
    num_columnas = 3
    for i in range(0, len(link_fotos), num_columnas):
        fila_fotos = link_fotos[i:i + num_columnas]
        cols = st.columns(num_columnas)

        for j, link in enumerate(fila_fotos):
            with cols[j]:
                st.image(link, width=400)


def cargarFotoNaturaleza():
    link_fotos = [
        "https://images.unsplash.com/photo-1793793349453-cca52afd48f1?q=80&w=736&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://images.unsplash.com/photo-1791752462600-e3ef63bce539?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://plus.unsplash.com/premium_photo-1793811568151-49b68013a38e?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"]

    num_columnas = 3
    for i in range(0, len(link_fotos), num_columnas):
        fila_fotos = link_fotos[i:i + num_columnas]
        cols = st.columns(num_columnas)

        for j, link in enumerate(fila_fotos):
            with cols[j]:
                st.image(link, width=400)


def cargarFotoExperimental():
    link_fotos = [
        "https://plus.unsplash.com/premium_photo-1764287051799-2b34e76f7e84?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://images.unsplash.com/photo-1792965347276-fa67d1e548d7?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "https://images.unsplash.com/photo-1793375729506-3c7e169bdafd?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"]

    num_columnas = 3
    for i in range(0, len(link_fotos), num_columnas):
        fila_fotos = link_fotos[i:i + num_columnas]
        cols = st.columns(num_columnas)

        for j, link in enumerate(fila_fotos):
            with cols[j]:
                st.image(link, width=400)








if __name__ == '__main__':
    cargar_proyectos()