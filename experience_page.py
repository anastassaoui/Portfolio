import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests



def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

url1 = get_url("https://lottie.host/01168c02-1c9e-493e-85f2-343c86c43950/fkBauqcPOH.json")
url2 = get_url("https://lottie.host/c8ce4ada-d2f8-42f8-ab21-689abf4e9aae/3yeact3Hyb.json")
url3 = get_url("https://lottie.host/ec9a9ff6-561d-40c4-9d73-1d10cadb1773/IsBsAaSi64.json")
url4 = get_url("https://lottie.host/d4cbdfc3-631d-4868-a579-414c0f7c15ba/aTaSBPnHZE.json")
url5 = get_url("https://lottie.host/ba08f5b8-8d62-4c39-9cd9-80b3b7c2ed13/EYPiFLUScU.json")

def experience():
    st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">',
    unsafe_allow_html=True
)

        #############tailwind stuff##############################################
    tailwind_cdn = """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
        <style>
            /* Center the table header and cell content */
            .css-1q8dd3e.e1ewe7hr3 th, .css-1q8dd3e.e1ewe7hr3 td {
                text-align: center !important;
            }
        </style>
    """
    st.markdown(tailwind_cdn, unsafe_allow_html=True)
    ########################################################################### 
    col1,col2 =st.columns(2)

    with col1:
    
        st.markdown("""
    <style>
        .icon { 
            color: #00aced; /* Adjust color for a sharper look */
            font-size: 1.3em; /* Larger icons for prominence */
            padding-right: 0.2em; /* Space between icon and text */
        }
        .header-icon {
            font-size: 2em; /* Larger header icon */
            padding-right: 0.3em;
        }
        .link-icon {
            color: #0073e6;
            padding-right: 0.5em;
            font-size: 1.2em;
        }
        .links {
            margin-top: 20px; /* Add space between text and links */
        }
    </style>

    <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer hover:underline md:-mb-12 md:mt-20 md:text-6xl md:mb-2">
    <i class="fas fa-user-cog header-icon md:text-3xl"></i> Experience
     <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 ">

    </h4>
        """, unsafe_allow_html=True)
        
        
    path = "Animation_exp.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url1, width=400, height=400)
    with st.container():
        col1, col2 = st.columns([3, 2])
    col1.markdown(""" 
        ### Stagiaire en Ingénierie des Procédés –– CIMAT Ben Ahmed (Juillet 2024)
        
        - **Projet de fin d'année** : Origine des Émissions HCl et Méthodes de Captation
        - **Description** : Analyse des sources d’émissions de HCl et exploration des méthodes de réduction et de captation des émissions dans le processus de production du ciment.
    """)

    col2.markdown("""
  
    """)

    with st.container():
        col1, col2 = st.columns([3, 2])
    col1.markdown(""" 
        ### Stagiaire en Optimisation de Processus –– OCP Khouribga - Laboratoire (Août 2024)
        
        - **Projet de fin d'année** : Optimisation et Calcul de Work Index d’un Broyeur (Ball Mill)
        - **Description** : Calcul du Work Index pour améliorer l'efficacité énergétique du broyeur à boulets dans le cadre du traitement des matières premières.
    """)

    col2.markdown("""
 
    """)

