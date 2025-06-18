import streamlit as st
def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("🏠_Mainpage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/1_📚_Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/2_🎨_Portofolio.py", label="Portofolio", icon="🎨")
    bar4.page_link("pages/3_🌏_Contacts.py", label="Contacts", icon="🌏")
    st.write("")

info = {
     'name': 'Clément Garnier',
     'brief': 'Data Engineer passionné...',
     'study': 'Ingénieur IMT Nord Europe (2025)',
     'location': 'France',
     'current_role': 'Alternant Data Engineer @ Decathlon',
     'interest': 'Big Data, ETL, Streaming',
     'phone': '+33 6 01 19 31 65',
     'email': 'clementgarnier@free.fr',
     'skills': ['Python','AWS','Spark','SQL'],
     'projects': [
         {
             'title': 'Pipeline ETL AWS → Data Lake',
             'description': 'Centralisation des données ventes Decathlon...',
             'technos': ['Python', 'AWS Glue', 'Redshift', 'Airflow', 'Docker'],
             'repo': 'etl-aws-pipeline',
             'demo': ''
         },
     ]
 }
linkedin_link = 'https://www.linkedin.com/in/clementgarnier2/'
github_links = {
     'etl-aws-pipeline': 'https://github.com/ton-user/etl-aws-pipeline',
     'segmentation': 'https://github.com/ton-user/tableau-segmentation',
     'streaming': 'https://github.com/ton-user/kafka-streaming',
     'main': 'https://github.com/ton-user'
 }