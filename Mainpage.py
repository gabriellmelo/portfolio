import streamlit as st
import streamlit.components.v1 as components
from constant import *

# Definir a configuração da página como o primeiro comando Streamlit
st.set_page_config(
    page_title="Main Page",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
) 

margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    # Sidebar ------------------------------------------------------------------------
    with st.sidebar:
        st.success(get_text(st.session_state['lang'], 'select_page'))
        
    # Main page ---------------------------------------------------------------------
    st.header(get_text(st.session_state['lang'], 'about_me'), divider='rainbow')
    col1, col2, col3 = st.columns([1.3, 0.2, 1])

    with col1:
        st.write(get_text(st.session_state['lang'], 'intro'))
        # Nas informações pessoais:
        st.markdown(f"###### 😄 {get_text(st.session_state['lang'], 'name')}: {english.info['name']}")
        st.markdown(f"###### 👉 {get_text(st.session_state['lang'], 'study')}: " + (portugues.texts['formacao'] if st.session_state['lang'] == 'pt' else english.info['study']))
        st.markdown(f"###### 📍 {get_text(st.session_state['lang'], 'location')}: " + (portugues.texts['localizacao'] if st.session_state['lang'] == 'pt' else english.info['location']))
        st.markdown(f"###### 📚 {get_text(st.session_state['lang'], 'interest')}: " + (portugues.texts['interesses'] if st.session_state['lang'] == 'pt' else english.info['interest']))

        if st.session_state['lang'] == 'pt':
            with open("src/GABRIEL_MELO_CV.pdf", "rb") as file:
                pdf_file = file.read()
            button_label = "Faça o download do meu CV"
        else:
            with open("src/GABRIEL_MELO_RESUME.pdf", "rb") as file:
                pdf_file = file.read()
            button_label = "Download Resume"

        st.download_button(
            label=button_label,
            data=pdf_file,
            file_name="cv.pdf",
            mime="application/pdf"
        )

    with col3:
        st.image("src/profile.jpg", width=360)

    # Skills -------------------------------------------------------------------------
    st.subheader(f"{get_text(st.session_state['lang'], 'my_skills')} :blue[⚒️]", divider='rainbow')

    def skill_tab():
        if st.session_state['lang'] == 'pt':
            dictionary_skills = portugues.texts['skills']
        else:
            dictionary_skills = english.info['skills']

        for category, skills_list in dictionary_skills.items():
            if st.session_state['lang'] == 'pt':
                translated_category = get_text(st.session_state['lang'], category)  # aplica tradução customizada se quiser
            else:
                translated_category = category

            st.subheader(translated_category.replace('_', ' ').title())

            rows, cols = len(skills_list) // skill_col_size, skill_col_size
            skills_iter = iter(skills_list)
            if len(skills_list) % skill_col_size != 0:
                rows += 1

            for row_index in range(rows):
                columns = st.columns(skill_col_size)
                for col_index in range(skill_col_size):
                    try:
                        skill = next(skills_iter)
                        columns[col_index].button(skill, key=f"{category}_{row_index}_{col_index}")
                    except StopIteration:
                        break

    with st.spinner(text=get_text(st.session_state['lang'], 'loading_section')):
        skill_tab()