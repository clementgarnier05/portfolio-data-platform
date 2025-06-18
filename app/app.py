import streamlit as st
from constant import *  # Assure `constant.py` inclut `info`, `linkedin_link`, `github_links` et `menu` modifié via radio

# Configure la page
st.set_page_config(page_title="Portfolio Clément Garnier", page_icon="🏠", layout="wide", initial_sidebar_state="expanded")

# Colonnes pour marges
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    # Barre de navigation via radio
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choisissez une page:",
        ["Introduction", "Expérience", "Portfolio", "Contacts"]
    )
    st.sidebar.markdown("---")

    # Page sélectionnée
    if page == "Introduction":
        st.header("À propos de moi", divider='rainbow')
        col1, _, col3 = st.columns([1.3, 0.2, 1])
        with col1:
            st.write(info['brief'])
            st.markdown(f"###### 😄 Nom : {info['name']}")
            st.markdown(f"###### 👉 Formation : {info['study']}")
            st.markdown(f"###### 📍 Localisation : {info['location']}")
            st.markdown(f"###### 💼 Poste actuel : {info['current_role']}")
            st.markdown(f"###### 📚 Intérêts : {info['interest']}")
            st.markdown(f"###### 👀 LinkedIn : [{linkedin_link}]({linkedin_link})")
            # Téléchargement du CV
            with open("src/CV_Garnier_Clement.pdf", "rb") as file:
                pdf_file = file.read()
            st.download_button(
                label="📄 Télécharger mon CV",
                data=pdf_file,
                file_name="CV_Garnier_Clement.pdf",
                mime="application/pdf"
            )
        with col3:
            st.image("src/portrait.jpeg", width=360)

    elif page == "Expérience":
        st.header("Mon Expérience", divider='rainbow')
        for exp in info.get('experiences', []):
            st.subheader(exp['role'])
            st.write(f"**Entreprise** : {exp['company']}")
            st.write(f"**Période** : {exp['period']}")
            st.write(exp['details'])
            st.markdown("---")

    elif page == "Portfolio":
        st.header("Mes Projets", divider='rainbow')
        for proj in info['projects']:
            st.subheader(proj['title'])
            st.write(f"**Contexte / Objectif** : {proj['description']}")
            st.write(f"**Technologies** : {', '.join(proj['technos'])}")
            if proj.get('demo'):
                st.markdown(proj['demo'])
            if github_links.get(proj['repo']):
                if st.button(f"Voir le code - {proj['title']}"):
                    st.markdown(f"[GitHub]({github_links[proj['repo']]})")
            st.markdown("---")

    else:  # Contacts
        st.header("Contact", divider='rainbow')
        st.write(f"- 📞 {info['phone']}")
        st.write(f"- ✉️ {info['email']}")
        st.write(f"- 🔗 [LinkedIn]({linkedin_link})")
        st.write(f"- 🔗 [GitHub]({github_links.get('main', '')})")