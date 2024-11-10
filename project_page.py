import streamlit as st
import json
from streamlit_lottie import st_lottie

def projects():
    col1, col2 = st.columns(2)

    # col1.markdown("## Experience")
    with col1:
        st.markdown("""
                <style>
                .centered {
                    display: flex;
                    align-items: center;
                    height: 100%;
                    margin-top: 200px; /* Adjust this value as needed */
                }
                </style>
                <div class="centered">
                    <h2>Projects </h2>
                </div>
            """, unsafe_allow_html=True)
    path = "Animation_girl.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )

    with st.container():
        col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):

            # Displaying the title of the project
            st.title("Application d’Analyse et de Visualisation de Données")

            # Displaying the description
            st.markdown("""
            **Description:**
            Cette application utilise Streamlit pour l'analyse et la visualisation de données en utilisant des outils avancés d'intelligence artificielle et de traitement du langage naturel. Principales fonctionnalités :

            - **Analyse de Données** : Importation, traitement et analyse de données à partir de fichiers CSV .
            - **Exploration Interactive** : Interaction avec les données via LangChain et LLaMA llama3-8b-8192  pour une exploration approfondie et un accès à des insights clés.
            - **Visualisation** : Création automatique de graphiques et visualisations personnalisées pour des présentations claires et intuitives.
            - **Transformation de Données** : Nettoyage, transformation, et création de nouvelles variables pour enrichir l'analyse.
            - **Automatisation de l’IA** : Utilisation de Pandas AI pour automatiser les analyses et générer des prévisions basées sur les données.
            """)

            # Displaying the tools used
            st.markdown("""
            **Outils Utilisés :**

             **Python**,
             **Pandas AI**,
             **Streamlit**,
             **LangChain**,
             **LLaMA**,
             **Matplotlib**
            """)

            # Links for the project
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown("""**[Lien vers l'application](https://twayssa-analyser.streamlit.app/)**""")
            c2.markdown("""**[GitHub](https://github.com/anastassaoui/analytics-using-pandas-ai)**""")
            c3.markdown("""**[Communauté Streamlit](https://discuss.streamlit.io/)**""")


    with col2:
        with st.container(border=True):

            # Displaying the title of the project
            st.title("Application de Gestion d’Absences")

            # Displaying the description
            st.markdown("""
            **Description:**
            Cette application de gestion d’absences est conçue pour faciliter le suivi des présences dans les classes avec un grand nombre d'étudiants. Conçue pour une utilisation par les professeurs, elle remplace le traditionnel appel en classe par un système automatisé et sécurisé.

            - **Gestion des Absences** : Les enseignants peuvent générer un code unique que les étudiants saisissent pour enregistrer leur présence.
            - **Tableau de Bord** : Un tableau de bord intuitif permet aux enseignants de visualiser en temps réel les présences et absences, et d’exporter les données si nécessaire.
            - **Sécurité et Stockage** : Les données sont stockées de manière sécurisée dans une base de données PostgreSQL, déployée sur la plateforme cloud **Render**, assurant confidentialité, disponibilité et intégrité des informations.
            """)

            # Displaying the tools used
            st.markdown("""
            **Outils Utilisés :**

            **Python**, 
            **Flask**, 
            **Streamlit**, 
            **Tailwind CSS**, 
            **PostgreSQL**,
            **Render**
            """)

            # Links for the project
            c1, c2,c3,c4 = st.columns(4)
            c1.markdown("""**[Lien vers l'application](https://the-abs-project.onrender.com/)**""")
            c2.markdown("""**[GitHub pour l'application](https://github.com/anastassaoui/The-Abs-Project)**""")
            c3.markdown("""**[Lien vers Dashboard](https://absence.streamlit.app/)**""")
            c4.markdown("""**[GitHub pour Dashboard](https://github.com/anastassaoui/the-abs-streamlit)**""")

            # Additional information (optional if needed)
            st.markdown("""
            <p class="text-gray-400 mt-4">
            Cette application permet une gestion des présences rapide et efficace, particulièrement utile pour des classes de grande taille. Elle garantit un suivi précis et minimise les erreurs, rendant le processus d'appel beaucoup plus efficace, avec un stockage sécurisé dans le cloud via la plateforme Render.
            </p>
            """, unsafe_allow_html=True)

    
                    
                    
                


    with col1:
        with st.container(border=True):

            # Displaying the title of the project
            st.title("UNIT OPERATIONS ARE COOL")

            # Displaying the description
            st.markdown("""
            **Description:**
            Cette application en cours de développement vise à illustrer de manière interactive diverses opérations unitaires essentielles en ingénierie des procédés, comme la distillation. Elle est conçue pour aider les étudiants et les professionnels à mieux visualiser et comprendre ces processus à travers des animations et des interfaces intuitives.

            - **Illustration d'Opérations Unitaires** : Visualisation de processus tels que la distillation, la filtration, et d'autres opérations critiques en génie chimique.
            - **Animations Engageantes** : Utilisation de Lottie pour ajouter des animations interactives et pédagogiques.
            - **Interface Moderne** : Conception d'une interface utilisateur responsive et esthétique en utilisant Tailwind CSS.
            - **Q&A Intégré avec LangChain et Groq APIs** : Intégration de LangChain pour permettre aux utilisateurs de poser des questions sur les opérations unitaires et obtenir des réponses en temps réel via les APIs Groq.
            """)

            # Displaying the tools used
            st.markdown("""
            **Outils Utilisés :**

            **Python**, 
            **Streamlit**, 
            **Tailwind CSS**, 
            **Lottie**, 
            **Groq APIs**, 
            **LangChain**
            """)

            c1, c2 = st.columns(2)
            c1.markdown("""**[Lien vers l'application](https://unit-operations-are-cool.streamlit.app/)**""")
            c2.markdown("""**[GitHub pour l'application](https://github.com/anastassaoui/UNIT-OPERATIONS-ARE-COOOL)**""")


    with col2:
        with st.container(border=True):

            # Displaying the title of the project
            st.title("Pack de Jeux en VB.NET")

            # Displaying the description
            st.markdown("""
            **Description:**
            Ce projet scolaire consiste en un pack de jeux simples développés en VB.NET en utilisant le framework .NET, dans le cadre d’un apprentissage de la programmation orientée objet et du développement d'applications de bureau.

            - **Programmation Orientée Objet** : Utilisation de concepts de programmation orientée objet (POO) pour structurer et organiser le code.
            - **Framework .NET** : Développement d'applications de bureau avec le framework .NET et le langage Visual Basic.
            - **Jeux de Base** : Création de jeux simples tels que Tic Tac Toe, Hangman, et d'autres petits projets interactifs pour renforcer les compétences en développement d'applications.
            """)

            # Displaying the tools used
            st.markdown("""
            **Outils Utilisés :**

            **VB.NET**, 
            **.NET Framework**, 
            **Visual Studio**
            """)

            # Adding the GitHub link
            st.markdown("""**[GitHub](https://github.com/anastassaoui/Game-App)**""")

    with col1:
        with st.container(border=True):
            
            # Displaying the title of the project
            st.title("Approximation du Coefficient de Diffusion avec le Modèle UNIFAC")
    
            # Displaying the description
            st.markdown("""
            **Description:**
            Ce projet consiste à approximer le coefficient de diffusion en utilisant le modèle UNIFAC, un modèle largement utilisé pour prédire les interactions dans des mélanges de composants. Le projet comprend :
    
            - **Modélisation UNIFAC** : Implémentation du modèle UNIFAC pour calculer les coefficients de diffusion dans divers mélanges.
            - **Application Web avec Flask** : Développement d'une interface web avec Flask pour permettre aux utilisateurs d'entrer les caractéristiques des composants et d'obtenir une approximation en temps réel.
            - **Visualisation des Résultats** : Affichage des résultats de l'approximation sous forme de graphiques pour une analyse claire et intuitive.
            """)
    
            # Displaying the tools used
            st.markdown("""
            **Outils Utilisés :**
    
            **Python**, 
            **Flask**, 
            **UNIFAC Model**,
            **NumPy**, 
            **Matplotlib**
            """)
    
            # Adding the GitHub link
            st.markdown("""**[GitHub](https://github.com/anastassaoui/UNIFAC-V-2.0-FLASK)**""")

