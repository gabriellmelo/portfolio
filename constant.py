import streamlit as st
from src.translates import portugues, english      


skill_col_size = 10

languages = {"English": "en", "Portuguese": "pt"}

if "lang" not in st.session_state:
    st.session_state["lang"] = "pt"  

# Função para alterar o idioma baseado na seleção
def set_language() -> None:
    if "selected_language" in st.session_state:
        st.session_state["lang"] = languages.get(st.session_state["selected_language"])

def menu():
    bar0, bar1, bar2, bar3, bar4, bar5 = st.columns([0.1, 1, 1, 1, 1, 1])
    bar1.page_link("Mainpage.py", label=get_text(st.session_state['lang'], 'page_intro'), icon="🏠")
    bar2.page_link("pages/Experience.py", label=get_text(st.session_state['lang'], 'page_experience'), icon="📚")
    bar3.page_link("pages/Portfolio.py", label=get_text(st.session_state['lang'], 'page_portfolio'), icon="🎨")
    bar4.page_link("pages/Contacts.py", label=get_text(st.session_state['lang'], 'page_contacts'), icon="🌏")
    
    with bar5:
        lang = st.session_state["lang"]
        
        lang_label = "Idioma" if lang == "pt" else "Language"
        
        lang_default = "Portuguese" if lang == "pt" else "English"
        lang_index = list(languages.keys()).index(lang_default)
        
        lang_option = st.radio(
            lang_label, 
            options=list(languages.keys()),
            index=lang_index,
            horizontal=True,
            on_change=set_language,
            key="selected_language",
            label_visibility="collapsed"
        )

def get_text(lang, key):
    return translations[lang].get(key, key)

translations = {
    'en': {
        'intro': english.info['brief'],
        'interest': 'Interest',
        'linkedin': 'Linkedin',
        'download_resume': 'Download my resume',
        'skills': 'My skills',
        'experience': 'Experience',
        'portfolio': 'Portfolio',
        'contacts': 'Contacts',
        'phone': 'Phone',
        'email': 'Email',
        'linkedin_link': 'Linkedin',
        'github_link': 'Github',
        'loading_section': 'Loading section...',
        'about_me': 'About Me',
        'select_page': 'Select a page above.',
        'name': 'Name',
        'study': 'Study',
        'location': 'Location',
        'interest': 'Interest',
        'my_skills': 'My skills',
        'page_intro': 'Introduction',
        'page_experience': 'Experience',
        'page_portfolio': 'Portfolio',
        'page_contacts': 'Contacts'
    },
    'pt': {
        'intro': portugues.texts['intro'],
        'interest': 'Interesses',
        'linkedin': 'Linkedin',
        'download_resume': 'Baixar meu currículo',
        'skills': 'habilidades',
        'experience': 'Experiência',
        'portfolio': 'Portfólio',
        'contacts': 'Contatos',
        'phone': 'Telefone',
        'email': 'Email',
        'linkedin_link': 'Linkedin',
        'github_link': 'Github',
        'loading_section': 'Carregando seção...',
        'about_me': 'Sobre mim',
        'select_page': 'Selecione uma página acima.',
        'name': 'Nome',
        'study': 'Formação',
        'location': 'Localização',
        'interest': 'Interesse',
        'my_skills': 'Minhas habilidades',
        'page_intro': 'Introdução',
        'page_experience': 'Experiência',
        'page_portfolio': 'Portfólio',
        'page_contacts': 'Contatos'
    }
}

# Definir idioma padrão no session_state
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'pt'

# URLs de publicação -------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
