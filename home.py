import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json


from reume_page import resume
from experience_page import experience
from upwork_page import feedbackRating
from project_page import projects
from contact_form import contact

 # Page setup
st.set_page_config(
    page_title="Anas",
    page_icon="📋",
    layout="wide",
)
def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

url1 = get_url("https://lottie.host/b1031118-99fc-47da-8103-0d692d09c1cd/6Myzvt3heg.json")
url2 = get_url("https://lottie.host/b3779c13-f63c-4d67-a9bc-af6da7de7788/n2HAJr8GlV.json")
url3 = get_url("https://lottie.host/33f398ca-7a6d-4434-97f8-4e5dbb34a625/ytJiSFcQ3s.json")  



def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
def aboutMe():
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
    
    
    col1 , col2 = st.columns([2,1])
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
        <i class="fas fa-user-astronaut header-icon"></i> Hello, I'm Anas Tassaoui!
    </h4>
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mb-10 md:pt-1">

    <p class="mb-3 text-lg md:text-xl text-white md:mt-20 cursor-pointer">
        <i class="fas fa-flask icon"></i> Welcome to my space, where process engineering meets software and AI! I'm a chemical and industrial process engineer with a passion for exploring 
        <i class="fas fa-code icon"></i> web development, <i class="fas fa-database icon"></i> data science, and <i class="fas fa-robot icon"></i> AI applications in our field.
    </p>
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 ">
    <p class="text-white cursor-pointer">
        <i class="fas fa-cogs icon"></i> Through engaging projects and simulations, I aim to blend essential process engineering principles like mass transfer and thermodynamics with modern software tools, 
        making it easier to apply and visualize complex concepts hands-on.
    </p>

    <div class="links space-x-96 md:mt-8">
        <a href="https://github.com/anastassaoui" target="_blank"><i class="fab fa-github link-icon"></i>GitHub</a>
        <a href="https://linkedin.com/in/anastassaoui" target="_blank"><i class="fab fa-linkedin link-icon"></i>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)



        
    with col2:
        st_lottie(url1, width=500, height=750)
        


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the base64 string of the image
logo_base64 = get_base64_image("Image.jpeg")

# Logo styling
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""






# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["About me", "Resume", "Experience",  "Projects", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Anas",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )
    
    
    
    
    
# Main content of the app
if nav_tab_op == "About me":
    aboutMe()

elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()

elif nav_tab_op == "Projects":
    projects()
elif nav_tab_op == "Contact":
    contact()


