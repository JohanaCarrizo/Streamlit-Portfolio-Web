import streamlit as st


def cargar_contacto():
    st.title('Contacto')
    col_info, col_form = st.columns(2)
    with col_info:
        st.write('email@example.com')
        st.write('+54 381564549')
        st.write('123 Demo Street')
        st.write('NY 156478')

    with col_form:
        with st.form('Contacto'):

            nombre = st.text_input('Nombre')
            apellido = st.text_input('Apellido')
            email = st.text_input('Email')
            mensaje = st.text_area('Mensaje')
            submitted = st.form_submit_button('Enviar')

            if submitted:
                st.write(f"Gracias {nombre} tu mensaje fue enviado!!")

if __name__ == '__main__':
    cargar_contacto()