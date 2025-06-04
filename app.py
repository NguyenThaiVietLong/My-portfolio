import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image


import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander
import streamlit.components.v1 as components


# Set page title
st.set_page_config(page_title="Portfolio - Việt Long", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
GA_ID = "G-XTDHDLJFN9"

def inject_ga():
    GA_ID = "G-XTDHDLJFN9"
    GA_JS = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
    </script>
    """
    st.markdown(GA_JS, unsafe_allow_html=True)

inject_ga()

# Start tracking analytics


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}

"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/main.jpg")
img_lh = Image.open("images/middle.jpg")
img_ifg = Image.open("images/contact.jpg")
#Assets for competitions
img_CPNTD = Image.open("images/CPNTD.jpg")
img_CPNTD2 = Image.open("images/CPNTD2.jpg")
img_CPNTD3 = Image.open("images/CPNTD3.jpg")
img_CPNTD4 = Image.open("images/CPNTD4.jpg")
img_CPNTD5 = Image.open("images/CPNTD5.jpg")
img_TLSV = Image.open("images/TLSV.png")
# Assets for education

img_HiStart = Image.open("images/HiStart.png")
img_sgu = Image.open("images/sgu.png")
img_PS = Image.open("images/AYP.png")
# Assets for experiences
img_FPT = Image.open("images/FPT_Telecom.png")
img_t4tek = Image.open("images/T4Tek.png")
img_smartlog = Image.open("images/smartlog.png")
# Assets for projects
img_identify = Image.open("images/identify.jpeg")
img_data = Image.open("images/data.jpeg")
img_logistics = Image.open("images/logistics.png") 
img_SGUsp = Image.open("images/SGUsp.png")
img_SGUsp2 = Image.open("images/SGUsp2.png")
img_SGUsp3 = Image.open("images/SGUsp3.png")
img_SGUsp4 = Image.open("images/SGUsp4.png")
img_SGUsp5 = Image.open("images/SGUsp5.png")
img_POSodoo = Image.open("images/POSodoo.jpg")
img_figma = Image.open("images/figma.png")

img_swm = Image.open("images/swm.png")
img_swm1 = Image.open("images/swm1.png")
img_swm2 = Image.open("images/swm2.jpg")

img_MyBao = Image.open("images/Project_MyBao.png")
img_MyBao2 = Image.open("images/Project_MyBao2.png")
img_MyBao3 = Image.open("images/Project_MyBao3.png")
img_MyBao4 = Image.open("images/Project_MyBao4.png")
img_MyBao5 = Image.open("images/Project_MyBao5.png")
img_MyBao6 = Image.open("images/Project_MyBao6.png")




# Assets for volunteering
img_XTN = Image.open("images/XTN.jpg")

# # Assets for blog
# img_qb = Image.open("images/qb.jpg")
# img_mayans = Image.open("images/mayans.jpg")
# img_outlier = Image.open("images/outlier.png")
# img_dac = Image.open("images/dac.png")
# img_raffles = Image.open("images/raffles.jpg")
# img_covid = Image.open("images/covid.jpg")
# img_gender = Image.open("images/gender.jpg")
# img_hci = Image.open("images/hci.jpg")
# img_wordcloud = Image.open("images/wordcloud.jpg")
# img_taste = Image.open("images/taste.jpg")
# img_measles = Image.open("images/measles.jpeg")
# img_bmsaew = Image.open("images/bmsaew.png")
# img_dac1 = Image.open("images/dac1.png")
# img_dac2 = Image.open("images/dac2.png")
# # # Assets for gallery
# # # 2005
# img_2005_1 = Image.open("gallery/2005_1.jpg")
# img_2005_2 = Image.open("gallery/2005_2.jpg")
# # 2006
# img_2006_1 = Image.open("gallery/2006_1.jpg")
# # 2008
# img_2008_1 = Image.open("gallery/2008_1.jpg")
# # 2009
# img_2009_1 = Image.open("gallery/2009_1.jpg")
# # 2011
# image_dict = {}
# num_images = 4
# for i in range(1, num_images + 1):
#     image_key = f"img_2011_{i}"
#     image_path = f"gallery/2011_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2012 
# image_dict = {}
# num_images = 7
# for i in range(1, num_images + 1):
#     image_key = f"img_2012_{i}"
#     image_path = f"gallery/2012_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2013
# image_dict = {}
# num_images = 11
# for i in range(1, num_images + 1):
#     image_key = f"img_2013_{i}"
#     image_path = f"gallery/2013_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2014
# image_dict = {}
# num_images = 13
# for i in range(1, num_images + 1):
#     image_key = f"img_2014_{i}"
#     image_path = f"gallery/2014_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2015
# image_dict = {}
# num_images = 48
# for i in range(1, num_images + 1):
#     image_key = f"img_2015_{i}"
#     image_path = f"gallery/2015_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2016
# image_dict = {}
# num_images = 25
# for i in range(1, num_images + 1):
#     image_key = f"img_2016_{i}"
#     image_path = f"gallery/2016_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2017
# image_dict = {}
# num_images = 4
# for i in range(1, num_images + 1):
#     image_key = f"img_2017_{i}"
#     image_path = f"gallery/2017_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2018
# image_dict = {}
# num_images = 16
# for i in range(1, num_images + 1):
#     image_key = f"img_2018_{i}"
#     image_path = f"gallery/2018_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2019
# image_dict = {}
# num_images = 20
# for i in range(1, num_images + 1):
#     image_key = f"img_2019_{i}"
#     image_path = f"gallery/2019_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2020
# image_dict = {}
# num_images = 3
# for i in range(1, num_images + 1):
#     image_key = f"img_2020_{i}"
#     image_path = f"gallery/2020_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2021
# image_dict = {}
# num_images = 14r
# for i in range(1, num_images + 1):
#     image_key = f"img_2021_{i}"
#     image_path = f"gallery/2021_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2022
# image_dict = {}
# num_images = 19
# for i in range(1, num_images + 1):
#     image_key = f"img_2022_{i}"
#     image_path = f"gallery/2022_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2023
# image_dict = {}
# num_images = 22
# for i in range(1, num_images + 1):
#     image_key = f"img_2023_{i}"
#     image_path = f"gallery/2023_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Việt Long", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Volunteering"],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    
    linkedin_url = "https://www.linkedin.com/in/vietlong/"
    github_url = "https://github.com/NguyenThaiVietLong"
    email_url = "mailto:longntv.work@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Nguyễn Thái Việt Long")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Business Analyst/Product Owner")
            st.write("👋🏻 Hi, I'm Long! I'm a business analyst graduate based in Vietnam. With prior relevant experiences in technology and teaching, I am constantly seeking opportunities to broaden my horizons and deepen my expertise as a Business Analyst, aiming to deliver more impactful and user-centric solutions.")
            st.write("💼 With a strong desire to work at a global company, I am dedicated to improving my English skills daily. I've been learning English through The Coach app and studying for the TOEIC exam to strengthen my proficiency. I believe these efforts will not only help me communicate effectively in an international environment but also support my long-term career growth.")
            st.write("🏋🏻 In addition, I enjoy exercising at the gym, running, playing footballs, traveling, playing video games, and spending time with friends in my free time!")
            st.write("👨🏼‍💻 Academic interests: SQL, Business Analysis, Data Visualization")
            st.write("💭 Ideal Career Prospects: Business Analyst, Business Data Analyst, Product Owner")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1L_lCK0hCdvliGiQAwuA6zIaPqXakZNY0/view?usp=drive_link)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_FPT)
        with text_column:
            st.subheader("Business Analyst, [FPT Telecom](https://fpt.vn/vi)")
            st.write("*December 2024 to Present*")
            st.markdown("""
            - Gathered requirements from internal teams and end-users to develop features that improved daily operations for **over 5,000** users.
            - Collaborated with **5** plus API teams to ensure seamless integration and optimal system performance.
            - Supported users directly and collected operational data to identify pain points, reported insightsto managers, and drove enhancements that reduced processing time by **30%**.
            - Managed the product lifecycle and prioritized the product backlog to ensure key features addressed user pain points and improved satisfaction.
            
            **Tools & Technologies:**
            - Documentation & Collaboration: Jira, Confluence, Draw.io
            - Systems & Platforms: Telecommunication Diagnostic Platform, Internal API Ecosystem
            - Analysis & Techniques: UAT, Priortize Product Backlog, Data Analysis
            """)
    
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_smartlog)
        with text_column:
            st.subheader("Business Analyst, [Smartlog](https://gosmartlog.com/)")
            st.write("*June 2024 to December 2024*")
            st.markdown("""
            - Collecting requirements from the implementation team, crafting functional specifications, and achieving **90%** accuracy in delivering features per customer needs.
            - Involving in large-scale projects like TTC and Nutrinest, integrating systems such as Oracle, SAP, Digifactory, and CRM to enhance operational efficiency.
            - Engaging with clients through surveys, workshops, and meetings to propose solutions and coordinate task assignments for developers, resulting in **100%** Sprint completion.
            - Developed a Control Tower system using SQL to provide executives with comprehensive company management tools, achieving **90%** alignment with stakeholder requirements.
            
            **Tools & Technologies:**
            - Documentation & Collaboration: Jira, Confluence, Draw.io
            - Systems & Integration: Warehouse Management System (WMS), External API(Oracle, SAP, Digifactory, CRM)
            - Data & Analysis Tools: SQL, Control Tower Dashboard
            - Methodologies: Agile-Scrum, Sprint Planning, User Story Mapping, Functional Specification
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_t4tek)
        with text_column:
            st.subheader("Business Analyst Intern, [T4 Tek](https://t4tek.co/vi)")
            st.write("*July 2023 to December 2023*")
            st.markdown("""
            - Gathered requirements from stakeholders, communicated effectively with the development team, and ensured on-time project delivery.
            - Developed **11** wireframes using Figma designs for a Human Resource Management (HRM) system within
            3 days, which comprehensively outlined the system's interface and pathways for user interactions.
            - Designed **11** workflow diagrams illustrating system operations and processes, facilitating stakeholder
            comprehension and effectively showcasing capabilities.
            
            **Tools & Technologies:**
            - Design & Visualization: Figma (UI wireframes), Draw.io (Workflow Diagrams), MindManager
            - Systems: Odoo (HRM Module)
            - Documentation & Task Tracking: Jira, Confluence
            """)
    
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Skill Sets")
    
    # Business Analysis Skills
    st.subheader("Business Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Documentation & Requirements**
        - Business Requirements Document (BRD)
        - Functional Requirements Specification (FRS)
        - System Requirements Specification (SRS)
        - User Stories & Use Cases
        """)
    with col2:
        st.markdown("""
        **Analysis & Design**
        - Business Process Modeling (BPMN)
        - UML Diagrams
        - Wireframing & Prototyping
        - User Experience Design
        """)

    # Technical Tools
    st.subheader("Technical Tools")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        **Documentation & Collaboration**
        - Microsoft Office Suite
        - Google Workspace
        - Confluence
        - Notion
        """)
    with col4:
        st.markdown("""
        **Design & Visualization**
        - Figma
        - Draw.io
        - Microsoft Visio
        - Balsamiq
        """)

    # Project Management
    st.subheader("Project Management")
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("""
        **Methodologies**
        - Agile/Scrum
        - Waterfall
        - Sprint Planning
        - User Story Mapping
        """)
    with col6:
        st.markdown("""
        **Tools & Platforms**
        - Jira
        - Confluence
        - Postman
        - Insomnia
        """)



    # CSS để loại bỏ padding mặc định của danh sách
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    st.subheader("Summary")
    st.write("*Summary of education from primary school till university*")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
                st.image(img_sgu)
        with text_column:
                st.subheader("Engineeer of Information System - Information Technology, [SGU](https://www.sgu.edu.vn/) (2020 - 2024)")
                st.write("Courseworks: Data Analysis, Software Project Management, Database, Database Management Systems, Software Engineering, Business Information System, Object-Oriented Analysis and Design, Python Programming")
                st.markdown("""
            - [ Member of Youth Union Executive Committee, Faculty of Information Technology](https://www.facebook.com/TuoitrekhoaCongngheThongtinSGU)
            - [Advisor of IT Talent Club](https://www.facebook.com/clbvannghexungkichITC)
            - Excellent Student Award at Faculty Level for 4 consecutive years (2020-2024)
            - Academic Scholarship recipient for 2 years
            - Multiple Certificates of Merit for outstanding activities at Faculty and University level throughout 4 years
                """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_HiStart)
        with text_column:
                st.subheader("Product BA Course - [HiStart Academy](https://www.facebook.com/profile.php?id=100092603730625) (2023)")
                st.write("Coursework: WBS, ORD - Object Relationship Diagram, Figma & UI/UX Design, Workflow Diagram, Customer Journey Map, North Star Metric")
                st.markdown(""" 
                - Understand the basics of Product Management, including Product Development, Product Marketing, Product Design, Product Operations, and Product Analytics
                """)
                
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_PS)
        with text_column:
                st.subheader("The Public Speaking Program - [Awake Your Power](https://ayp.vn/) (2023)")
                st.write("Coursework: Public Speaking, Presentation Skills, Body Language, Voice Modulation, Speech Intonation")
                st.markdown(""" 
                - Enhanced public speaking skills and confidence
                My Credential: [Certificate](https://drive.google.com/file/d/1wPpqCZUjpy4oH0y_B0R8sBnrFKRKoRLk/view?usp=sharing)
                """)
                
       
    #elif selected == "Module Reviews":
        #st.subheader("Module Reviews")
        #st.write("*Reviews for selected modules taken in university*")


elif choose == "Projects":
    # Create section for Projects
    st.header("Projects")
    
    # Initialize session state for project visibility if not exists
    if 'project_visibility' not in st.session_state:
        st.session_state.project_visibility = {
            'wms': True,
            'identify': True,
            'data': True,
            'logistics': True,
            'sgu': True,
            'pos': True,
            'mybao': True
        }
        
    with st.container():
        text_column, image_column = st.columns((2,2))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("Modem Diagnostic System")
                st.write("*December 2024 to Present*")
            with col2:
                if st.button("Hide", key="mybao_toggle"):
                    st.session_state.project_visibility['mybao'] = not st.session_state.project_visibility['mybao']
            
            if st.session_state.project_visibility['mybao']:
                
                st.markdown("""
                - Automatically diagnose and fix device/network issues.
                - Configure device settings remotely
                - View real-time and historical device parameters
                - Perform remote support actions: (reset PPPoE password, kill active session, reset MAC address, upgrade firmware).
                """)
                st.image(img_MyBao2)
                st.image(img_MyBao3)
            
        with image_column:
            if st.session_state.project_visibility['mybao']:
                st.image(img_MyBao)
                st.image(img_MyBao5)
                st.image(img_MyBao4)
                  
    
    with st.container():
        text_column, image_column = st.columns((2,2))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("Warehouse Management System")
                st.write("*June 2024 to December 2024*")
            with col2:
                if st.button("Hide", key="wms_toggle"):
                    st.session_state.project_visibility['wms'] = not st.session_state.project_visibility['wms']
            
            if st.session_state.project_visibility['wms']:
                
                st.markdown("""
                - Digitize warehouse operations to reduce manual work and paperwork.
                - Enable real-time warehouse management for faster and more accurate decision-making.
                - Optimize warehouse performance by reducing order processing time and improving labor productivity.
                - Enhance inventory accuracy, minimizing mistakes in receiving and shipping.
                """)
                st.image(img_swm1)
        with image_column:
            if st.session_state.project_visibility['wms']:
                st.image(img_swm)
                st.image(img_swm2)
    
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("Identify Positive and Negative Comments on Youtube")
                st.write("*January 2024 to May 2024*")
            with col2:
                if st.button("Hide", key="identify_toggle"):
                    st.session_state.project_visibility['identify'] = not st.session_state.project_visibility['identify']
            
            if st.session_state.project_visibility['identify']:
                
                st.markdown("""
                - Developed and integrating a machine learning-based data collection system within 2 months, gathering
                and processing 100,000 data entries for a Steam-based learning model.
                - Built webscraper using BeautifulSoup4 to scrape content from [Steam](https://store.steampowered.com/)
                - Aided content creators in identifying channel issues, resulting in a 70% reduction in time spent pinpointing
                problems.
                """)
        with image_column:
            if st.session_state.project_visibility['identify']:
                st.image(img_identify)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("Data Analytics for Eccomerce Company")
                st.write("*September 2023 to January 2024*")
            with col2:
                if st.button("Hide", key="data_toggle"):
                    st.session_state.project_visibility['data'] = not st.session_state.project_visibility['data']
            
            if st.session_state.project_visibility['data']:
                
                st.markdown("""
                - Developed and trained machine learning models to forecast Contoso's profit margins, achieving accuracy
                levels exceeding 90%.
                - Conducted a thorough analysis of Contoso's financial issues, successfully identifying the root causes of
                the company's economic situation.
                - Efficiently processed over 600,000 data entries across 17 columns without data reduction, successfully
                deploying the enhanced system.
                """)
                mention(label="Streamlit App", icon="streamlit", url="https://dataanalysiscontoso.streamlit.app/",)
                mention(label="Github Repo", icon="github", url="https://github.com/NguyenThaiVietLong/DataAnalysis_Contoso",)
        with image_column:
            if st.session_state.project_visibility['data']:
                st.image(img_data)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("Logistic(Economy Express Delivery)")
                st.write("*April 2023 to October 2024*")
            with col2:
                if st.button("Hide", key="logistics_toggle"):
                    st.session_state.project_visibility['logistics'] = not st.session_state.project_visibility['logistics']
            
            if st.session_state.project_visibility['logistics']:
                
                st.markdown("""
                -  Enhanced UI/UX workflows and customer journey mapping, facilitating a comprehensive understanding
                of the entire system.
                - Improved workflow visualization and efficiency by creating and documenting BPMN processes.
                - Developed and implemented a comprehensive Software Requirements Specification (SRS) document,
                detailing both functional and non-functional requirements, user stories, display rules, and business guide-
                lines.
                """)
                mention(label="Google Drive", icon="📁", url="https://drive.google.com/drive/folders/1-IbxCGRMZ3WJUNiYLS_tCzjQjzM3LWnl?usp=sharing")
        with image_column:
            if st.session_state.project_visibility['logistics']:
                st.image(img_logistics)

    with st.container():
        text_column, image_column = st.columns((3,3))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("SGU Student Portal")
                st.write("*January 2023 to May 2023*")
                
            with col2:
                if st.button("Hide", key="sgu_toggle"):
                    st.session_state.project_visibility['sgu'] = not st.session_state.project_visibility['sgu']
            
            if st.session_state.project_visibility['sgu']:
                
                st.markdown("""
                - Developed and launched a prototype application for Saigon University (SGU) students, enhancing their academic and extracurricular engagement by providing instant access to study schedules, academic points, training points, and university event registration.
                - Implemented a Study Schedule feature, enabling over 10,000 students to efficiently manage their academic calendars and participate in university events.
                - Created a Study Points module, offering personalized academic guidance to students.
                - Integrated a Training Points tracking system, allowing students to monitor their extracurricular participation.
                """)
                mention(label="Figma App",icon ='📱', url="https://figmashort.link/G8akP4",)
                st.image(img_SGUsp3)
                st.image(img_SGUsp4)
        with image_column:
            if st.session_state.project_visibility['sgu']:
                st.image(img_SGUsp)
                st.image(img_SGUsp2)
                st.image(img_SGUsp5)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            col1, col2 = st.columns([4,1])
            with col1:
                st.subheader("POS System in Odoo")  
                st.write("*September 2022 to January 2023*")
                with col2:
                    if st.button("Hide", key="pos_toggle"):
                        st.session_state.project_visibility['pos'] = not st.session_state.project_visibility['pos']
            
            if st.session_state.project_visibility['pos']:
                
                st.markdown("""
                - Analyzed and documented user functionalities for the ODOO POS module through Use case, enabling customization of POS features for greater flexibility and satisfaction.
                - Used Activity and Sequence Diagrams to improve system understanding by 60% and integration time for new features by 50% in the ODOO POS system.
                - Crafted Class Diagrams to illustrate data processing flows and relationships, and developed Entity-Relationship Diagrams (ERDs) to meticulously map out data structures.
                """)
        with image_column:
            if st.session_state.project_visibility['pos']:
                st.image(img_POSodoo)
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        text_column,image_column,image_column2  = st.columns((2,3,3))
        with text_column:
            st.subheader("Strategies to Impress Employers - Hosted by [The Student Union of Saigon University](https://www.facebook.com/tuoitredhsaigon)")
            st.write("Achieved a top 5 position in the competition, surpassing over 100 students by excelling in product presentations, personal presentations, CV creation, and answering interview questions.")
            
        with image_column:
            st.image(img_CPNTD4)
            st.image(img_CPNTD3)
            #st.empty()
        with image_column2:
            st.image(img_CPNTD2)
            st.image(img_CPNTD5)
        
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_TLSV)
            #st.empty()
        with text_column:
            st.subheader("City-Level Student Leadership Contest 2022 - Hosted by [HCM's Vietnam National Union of Students](https://www.facebook.com/hoisinhvienVietNamHCM)")
            st.write("Awarded Top 25 Finalist out of 300 submissions")
            st.write("Our team achieved 1st place in the group competition round.")
    
elif choose == "Volunteering":
    st.header("Volunteering")
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Xuan Tinh Nguyen Campaign")
            st.write("*Dec 2022 to Jan 2023*")
            st.markdown("""
            Vice Leader
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(img_XTN)
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Hoa Phuong Do Summer Volunteer Cammpaign")
            st.write("*May 2018 to May 2019*")
            st.markdown("""
            Volunteer

            """)
        with mid:
            st.empty()
    
# elif choose == "Blog":
#     st.header("Blog")
#     selected_options = ["Overview", "Article & Essay List",
#     #"It's not pink, it's salmon" – Why I returned to my previous start-up for FREE", 
#                         "Mayans MC – Season 5 Detailed Preview",
#                         "Finding success as an outlier (Extracted Using Wordpress REST API)",
#                         "Finding success as an outlier (Formatted Version)", 
#                         "Should the statue of Sir Stamford Raffles disappear for good?",
#                         "Should the Women's Charter replace one of the existing ten objects in the module?", 
#                         "Does gender inequality still have a place in Singapore's society today?", 
#                         "Reflections on Organising an 850-participant Data Analytics Competition (Extracted Using Google Sites REST API)",
#                         "Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)",
#                         "Worsened health disparities based on ethnicity and gender due to COVID-19",
#                         "Obstacles in promoting healthy eating habits",
#                         "Role of healthcare data analytics in managing COVID-19",
#                         "Evaluating 'Chinese Privilege' in Singapore: Special Assisted Plan Schools",
#                         "Analysing usefulness of word clouds in mental health studies",
#                         "Investigating the relationship between culture and sweet-sour taste interactions",
#                         "Timing vaccination campaign to reduce measles infections"
#                         ]
#     selected = st.selectbox("Which section or write-up would you like to read?", options = selected_options)
#     st.write("Current selection:", selected)
#     if selected == "Overview":
#         st.subheader("Overview")
#         st.markdown("""
#         I must admit - I hated reading books as a kid, and in turn, I disliked writing essays or expressing my thoughts as well. However, throughout my time in university, I have gradually picked up the essence of writing, to the extent of making use of it as a destressor from my technical modules.

#         Although my writing skills were novice at best when I was a freshman, I eventually got better at it (in my opinion), even to the extent of writing content articles as a regular hobby! It is indeed an asset to pick up as many skills as possible when still young, as you never know when you may need to utilise a particular skill whenever necessary.

#         In this section, you will be able to read some of my finest write-ups from my university experiences, based on topics varying from science to politics. For those looking forward to a good read, enjoy!
#         """)

#     elif selected == "Article & Essay List":
#         st.subheader("Article & Essay List")
#         #with st.container():
#             #text_column, image_column = st.columns((3,1))
#             #with image_column:
#                 #st.image(img_qb)
#             #with text_column:
#                 #st.subheader("It's not pink, it's salmon" – Why I returned to my previous start-up for FREE")
#                 #st.write("*May 21, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/05/21/its-not-pink-its-salmon-why-i-chose-to-return-to-my-previous-start-up-for-free/)")
#                 #st.write("A personal reflection explaining why I returned to my former start-up to diversify my experiences")
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_mayans)
#             with text_column:
#                 st.subheader("Mayans MC - Season 5 Detailed Preview")
#                 st.write("*May 13, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
#                 st.write("A preview of the fifth and final season Mayans MC, along with its similarities with Sons of Anarchy")
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_outlier)
#             with text_column:
#                 st.subheader("Finding success as an outlier")
#                 st.write("*April 12, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
#                 st.write("A personal reflection of my tumultous undergraduate journey so far - and how I finally found my resolve")
#                 #st.write("[Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")       
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_raffles)
#             with text_column:
#                 st.subheader("Essays for Final Test - GES1037: A History of Singapore in Ten Objects")
#                 st.write("*April 29, 2022* | [*Essays*](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
#                 st.markdown("""
#                 Essays written within 24-hour window in Academic Year 2021/22 Semester 2:
#                 - Q4: Should the statue of Sir Stamford Raffles disappear for good?
#                 - Q6: Should the Women's Charter replace one of the existing ten objects in the module? 
#                 """)       
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_gender)
#             with text_column:
#                 st.subheader("Does gender inequality still have a place in Singapore's society today?")
#                 st.write("*April 2, 2022* | [*Term Paper*](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
#                 st.markdown("""
#                 Term paper submitted for the module GES1037: A History of Singapore in Ten Objects in Academic Year 2021/22 Semester 2
#                 """)       
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_dac)
#             with text_column:
#                 st.subheader("Reflections on Organising an 850-participant Data Analytics Competition")
#                 st.write("*February 18, 2022* | [*Article*](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
#                 st.markdown("""
#                 A personal reflection of organising a large-scale online competition over the course of 6 months - co-written with [Axel Lau](https://www.linkedin.com/in/axel-lau/)
#                 """)
#                 #st.write("[Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_covid)
#             with text_column:
#                 st.subheader("Essays for Final Assignment - GEH1049: Public Health in Action")
#                 st.write("*November 12, 2021* | [*Essays*](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")
#                 st.markdown("""
#                 Essays written in Academic Year 2021/22 Semester 1:
#                 - Q1: Worsened health disparities based on ethnicity and gender due to COVID-19
#                 - Q2: Obstacles in promoting healthy eating habits
#                 - Q3: Role of healthcare data analytics in managing COVID-19
#                 """)
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_hci)
#             with text_column:
#                 st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
#                 st.write("*April 29, 2021* | [*Final Essay*](https://github.com/harrychangjr/ges1010/blob/main/GES1010%20Final%20Essay%20A0201825N.pdf)")
#                 st.markdown("""
#                 Final essay submitted for the module GES1010: Nation-building in Singapore in Academic Year 2020/21 Semester 2
#                 """)      
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_wordcloud)
#             with text_column:
#                 st.subheader("Analysing usefulness of word clouds in mental health studies")
#                 st.write("*March 5, 2021* | [*Essay*](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20GET1030%20Individual%20Assignment%20Final.pdf)")
#                 st.markdown("""
#                 Individual assignment submitted for the module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2
#                 """)
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_taste)
#             with text_column:
#                 st.subheader("Investigating the relationship between culture and sweet-sour taste interactions")
#                 st.write("*October 31, 2020* | [*Article*](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA2.pdf)")
#                 st.write("*Are we correct to stereotype taste perceptions and preferences based on different cultures?*")
#                 st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")      
#         with st.container():
#             text_column, image_column = st.columns((3,1))
#             with image_column:
#                 st.image(img_measles)
#             with text_column:
#                 st.subheader("Timing vaccination campaign to reduce measles infections")
#                 st.write("*September 30, 2020* | [*Article*](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA1.pdf)")
#                 st.write("*Despite having a vaccine that is readily accessible, measles cases and deaths are still surging worldwide, especially in recent years. Why is this so and are there any long-term solutions to resolve this?*")
#                 st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")
#     elif selected == "Mayans MC – Season 5 Detailed Preview":
#         with st.echo(code_location="below"):
#             import streamlit as st
#             import requests
#             from bs4 import BeautifulSoup

#             def arrange_images_side_by_side(html_content):
#                 soup = BeautifulSoup(html_content, "html.parser")
#                 images = soup.find_all("img")

#                 i = 0
#                 while i < len(images) - 1:
#                     current_image = images[i]
#                     next_image = images[i + 1]

#                     current_figure = current_image.find_parent("figure")
#                     next_figure = next_image.find_parent("figure")

#                     # Check if the next image is an immediate sibling
#                     if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
#                         container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
#                         current_figure.wrap(container)
#                         next_figure.wrap(container)

#                         # Set the same height for both images and add a little margin for better centering
#                         current_image['style'] = "height: 400px; margin: auto;"
#                         next_image['style'] = "height: 400px; margin: auto;"

#                         # Update the images list
#                         images = soup.find_all("img")
#                     i += 1

#                 return str(soup)

#             def get_post_by_id(url, post_id):
#                 site_url = url.replace("https://", "").replace("http://", "")
#                 response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
#                 response.raise_for_status()
#                 return response.json()

#             url = "https://antcabbage.wordpress.com"
#             post_id = 83
#             post = get_post_by_id(url, post_id)

#             post_title = post["title"]["rendered"]
#             post_content = post["content"]["rendered"]
#             soup = BeautifulSoup(post_content, "html.parser")
#             clean_post_content = soup.get_text()
#             st.subheader(post_title)
#             st.write("May 13, 2023 | [Article](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
#             st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
#             modified_content = arrange_images_side_by_side(post_content)
#             st.markdown(modified_content, unsafe_allow_html=True)
#     elif selected == "Finding success as an outlier (Extracted Using Wordpress REST API)":
#         with st.echo(code_location="below"):
#             import streamlit as st
#             import requests
#             from bs4 import BeautifulSoup

#             def arrange_images_side_by_side(html_content):
#                 soup = BeautifulSoup(html_content, "html.parser")
#                 images = soup.find_all("img")

#                 i = 0
#                 while i < len(images) - 1:
#                     current_image = images[i]
#                     next_image = images[i + 1]

#                     current_figure = current_image.find_parent("figure")
#                     next_figure = next_image.find_parent("figure")

#                     # Check if the next image is an immediate sibling
#                     if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
#                         container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
#                         current_figure.wrap(container)
#                         next_figure.wrap(container)

#                         # Set the same height for both images and add a little margin for better centering
#                         current_image['style'] = "height: 400px; margin: auto;"
#                         next_image['style'] = "height: 400px; margin: auto;"

#                         # Update the images list
#                         images = soup.find_all("img")
#                     i += 1

#                 return str(soup)

#             def get_post_by_id(url, post_id):
#                 site_url = url.replace("https://", "").replace("http://", "")
#                 response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
#                 response.raise_for_status()
#                 return response.json()

#             url = "https://antcabbage.wordpress.com"
#             post_id = 72
#             post = get_post_by_id(url, post_id)

#             post_title = post["title"]["rendered"]
#             post_content = post["content"]["rendered"]
#             soup = BeautifulSoup(post_content, "html.parser")
#             clean_post_content = soup.get_text()
#             st.subheader(post_title)
#             st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
#             st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
#             modified_content = arrange_images_side_by_side(post_content)
#             st.markdown(modified_content, unsafe_allow_html=True)
        
        
#     elif selected == "Finding success as an outlier (Formatted Version)":
#         st.subheader("Finding success as an outlier (Formatted Version)")
#         st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
#         st.write("*The content of this article was manually copied and pasted from the original site, along with manually embeedded media and captions for formatting purposes*")
#         st.markdown("""
#         > Outlier – a person or thing differing from all other members of a particular group or set.

#         This was what one of my recent interviewers defined himself as, when I asked him more about his experiences before working at his current position. He elaborated that he has been working at his current company for over 20 years upon graduation, an achievement he takes pride in which also exemplifies his undying passion for his job. This is something that most employees do not normally do, as it is common to switch job environments after every few years to revitalize their careers.

#         The conversation that I had with him really hit me that day – because in some way, I would also define myself as an outlier, especially in my university life. Having originally intended to graduate this semester, I would say that I have experienced many ups and downs throughout these past 4 years. From my many mistakes that have resulted in tumultuous phases, to particular happy moments and achievements that I should have cherished more dearly, perhaps it was indeed fate that has shaped me to who I am today.

#         Blessed with the privilege of good academics throughout junior college, I originally intended to pursue a degree in chemical engineering, particularly due to my initial fascination for pharmaceuticals and how they could enhance our bodies. During my national service, however, a new course for pharmaceutical science was launched in my school, and given my interest back then, I took a leap of faith and applied for a switch before I formally commenced my university education. 

#         Fast forward to my first semester, and I gradually realized that I had made one of the biggest mistakes of my life. I discovered that I was merely blinded by the potential career prospects of this new degree, which has yet to prove itself with a tenured track record. Without seriously considering the pros and cons, I would dare say that I foolishly embarked on this journey without prior preparation and research, resulting in me eventually flunking that semester altogether.

#         "But you have all the potential in the world"  said some of my peers and mentors, who were then envious of me being in this prestigious course. Regardless of whether I was merely being motivated to complete a particular task, or that someone genuinely identified the potential in me, I eventually realized that this quote alone made me hate a lot about myself back then, especially whenever I flunked. I would often feel an overwhelming sense of disappointment whenever I felt that I fell short of my own (high) expectations, which were imposed by this "potential" I thought I had. 

#         In a way, I was humbled by the experience. Thinking that the competition in junior college was tough enough, having the opportunity to meet different varieties of students changed the game for me. Working and interacting with many youths who came from different backgrounds – including student entrepreneurs, future researchers and national athletes, I realized that they were much more driven, passionate and hardworking at their craft than me, and for the right reasons. Unlike me, it was clear that they had long term plans in mind to hone their skills in order to pursue their ideal careers in the future.

#         And so, after taking my second semester off with a leave of absence, I decided to embark on another journey, this time restarting as a data science undergraduate. Knowing that this would delay my graduation and my tuition fees would be higher for my extended final year, I prayed that the journey would be smoother this time round. Although this was definitely not the case due the vastly different disciplines between the 2 degrees, I was privileged to be able to experience a certain degree of success over the next 2 years, even though my academic results signified otherwise. With my expectations being lowered this time round, I felt that at the very least, I was enjoying myself more in whatever I was pursuing.

#         Unfortunately, I made the mistake of succumbing to peer pressure once again, this time pursuing too many commitments that I eventually could not handle, resulting in dire consequences both in my academics and interpersonal relationships. Being blinded by greed and ego once more, I knew that I had to take a step back and reflect on what really went wrong, having made the same life mistake multiple times now, which was what I have been doing throughout this semester.

#         This was when I truly understood who I really am – one who merely wants to experience life without any comparison to others. I have discovered that the only real critic that I need to value is myself, and develop the self-awareness of whether I am truly enjoying whatever I am doing, or at least fully commit to the purpose of my actions. Not saying that I should downright ignore constructive criticism and opinions against me, but rather question myself from time to time whether their opinions really matter at any particular moment. In addition, self-care is also what I am trying to prioritize, where I should learn to take breaks when necessary.

#         As Israel Adesanya said after his most recent bout against Alex Pereira, a mixed martial artist who he lost to 3 times (in both MMA and kickboxing) beforehand to regain the UFC Middleweight Championship:

#         > "I hope every one of you — behind the screen and in this arena — can feel this level of happiness, just one time in your life. But guess what, you will never feel this level of happiness if you don't go for something in your own life. When they knock you down, when they try and sh*t on you… and try and put their foot on your neck. If you stay down, you will never ever get that resolve. Fortify your mind!"

#         > **Israel Adesanya**""")
#         with st.container():
#             col1, col2, col3 = st.columns((1,3,1))
#             with col1:
#                 st.empty()
#             with col2:
#                 st.video("https://www.youtube.com/watch?v=ZNoODFgTq3c")
#             with col3:
#                 st.empty()
#         st.markdown("""
#         Likewise, I have learnt not to harp on my mistakes for too long, otherwise this would impede me in the long run, and I would never be able to bounce back from what I have done. It is indeed important to forgive yourself and try to strive for the better, even though others may doubt so.

#         So who am I – really? To answer this, I would compare myself to 2 characters that I have enjoyed following on television. The first would be Alex Moran, the protagonist of sitcom Blue Mountain State. His character is that of a second-string quarterback for the majority of the show, only aiming to be an "Average Joe" after he graduates from college. The second would be Orange Cassidy, a professional wrestler whose gimmick is based on being the "King of Sloth Style", otherwise only trying to win when necessary, but doesn't bother otherwise.
#         """)
#         with st.container():
#             col1, col2, col3 = st.columns((1,3,1))
#             with col1:
#                 st.empty()
#             with col2:
#                 st.image(img_bmsaew, caption = "From left to right: Alex Moran (played by Darin Brooks in Blue Mountain State), Orange Cassidy", width=600, )
#             with col3:
#                 st.empty()
#         st.markdown("""
#         Drawing inspiration from these two characters, I would say I have now lowered the expectations that I have set for myself, and have learnt to be more appreciative for the opportunities that I have instead. It's not wrong to be surrounded by driven and passionate people in your circle, but at the end of the day, I feel it's not worth putting in exceptional efforts if that means sacrificing your own personal well-being.

#         And back to my self-reflection this semester: even though I'm not graduating within the next few weeks, it was still satisfying to live as though I was – with minimal commitments, barely dropping by physical lessons, and even finishing a final paper within one-third of the allocated duration before leaving early. It was indeed a breath of fresh air that I needed to rebuild myself for the better in the long run. It felt lonely at times, but when you can find happiness and contentment in being alone, what's there to stop you from enjoying yourself in better scenarios?

#         Throughout this time, it was only recently that I finally figured out what my career goals are. Many may have realized this way before me – but it's okay, because everyone takes their own time to figure their lives out gradually. Given my unorthodox undergraduate life, I would say I'm more than grateful to be more clear about what I want in the end. I wish I graduated now, but perhaps this was a blessing in disguise.

#         > "Success is not defined by either wealth or status. Success is about relations, friends, family and your belief in stewardship. Those will bring you to many places."

#         Those were the parting words from my boss in national service. Although his intentions are good, I would say that I define success a bit differently – being content with whatever you have at the present moment. 

#         With that being said, I've learnt that there's nothing wrong being an outlier – in fact, we are all outliers in our own right, because we are the protagonists in our own story that makes us unique. As my GP teacher in junior college once said, you need to develop yourself with an interesting story and cannot be boring – and I hope whatever that I have written here illustrates an engaging narrative that can be enjoyed by all.

#         To end off, I'd like to dedicate this write-up to those graduating soon, as well as others like myself, who had an unconventional journey during university for one reason or another. Even with multiple mishaps along the way, I believe that everyone can eventually find their own success as an outlier.
#         """)
#     elif selected == "Should the statue of Sir Stamford Raffles disappear for good?":
#         st.subheader("Should the statue of Sir Stamford Raffles disappear for good?")
#         st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
#         st.markdown("""
#         Sir Stamford Raffles is often credited as the true founder of modern Singapore,
#         having "transformed Singapore from an obscure fishing village to a great seaport and
#         modern metropolis". To commemorate his legacy, a statue of Raffles was erected by the
#         Singapore government to acknowledge British colonialism as part of the country's history.
#         As we are now living in the post-colonial era, however, many citizens do not see the need
#         to commemorate this, especially since most of them did not live in the colonial era. Thus,
#         I would agree with the standpoint that the Raffles statue should be taken down for good.

#         Firstly, the statue should be taken down due to the possible standpoint that citizens
#         recognise Sang Nila Utama as the true founder of modern Singapore, instead of Sir
#         Stamford Raffles. While Raffles had first landed in Singapore in 1819 that helped shape
#         Singapore to what it is today, Sang Nila Utama had already stepped foot in the country
#         as early as 1299, founding the nation as the Kingdom of Singapura back then. It is
#         important to recognise the story behind how the Malay prince first landed on the land
#         known as Temasek before renaming the land as Singapura. This is especially true
#         considering that the indigenous people in the country were Malays, and it would be a
#         better idea to credit more of Singapore's history to its geographical neighbours rather than
#         to British colonialism. The introduction of the Singapore Bicentennial in 2019 also
#         acknowledges this, citing that not many Singaporeans knew about the existence of Sang
#         Nila Utama, believing that Raffles was the true founder instead. Given that the Singapore
#         government would want its citizens to better understand Singapore's history especially
#         before 1819, it would be in its best interest to remove the statue instead, to avoid overacknowledging
#         Raffles' influence in Singapore's history.
        
#         Secondly, the statue should be taken down to avoid misinterpretations that
#         Singapore is still being influenced by British colonialism. While Singapore is no longer a
#         British colony, it still establishes a diplomatic relationship with the United Kingdom,
#         forming various trade and political partnerships between the two countries in the process.
#         Furthermore, Singapore is also a part of the Commonwealth, where many of the member
#         nations are former British colonies. Member nations of this political association enjoy
#         exclusive diplomatic partnerships with one another to boost each other's economies.
#         However, having the Raffles statue being erected still in Singapore may give an
#         impression that the country still acknowledges the former British empire as its benefactor.
#         This is certainly not the case in today's context, especially if Singapore wishes to be seen
#         as an independent nation, it should be recognised as an equal to a country such as the
#         United Kingdom, and not as an underling of the latter. As such, removing the statue would
#         help to avoid that misconception.

#         Thirdly, by removing the statue of Raffles, I believe that this would truly signify
#         Singapore's growth from an economic beneficiary in the colonial era to an economic
#         powerhouse in the modern world today. As mentioned in the article attached to this
#         question, Singapore has transformed into a global trading port, experiencing volumes of
#         economic growth every year. While Singapore used to benefit as a trading hub in the past
#         largely due to British rule, the country can now take the next step and help its
#         neighbouring countries to prosper economically together through mutually beneficial
#         trade partnerships. Singapore's status as an independent and prospering nation can
#         indeed potentially promote the economic growth of the entire Southeast Asian region as
#         well, filling in the shoes of its previous colonial ruler. Thus, removing the statue could be
#         a symbol of Singapore finally emerging from its previous colonial ruler, in order to step up
#         as a strong economic power moving forward.

#         To sum up, while Raffles did set the precedent for Singapore to eventually prosper
#         as an economic trading port, it is not necessary for his statue to remain erected in our
#         soil. To many of our ancestors, the colonial era may signify long bouts of hardships and
#         poverty, especially under the rule of the British, which may contribute to local sentiments
#         that the statue is not necessary. Furthermore, almost all Singaporean citizens in our
#         society today did not actually live in the colonial era, making it difficult for them to
#         personally relate to Raffles and his rule back in the 1800s. Therefore, I believe that it is
#         indeed essential for the statue to be eventually removed, so that we can move forward
#         from being recognised as merely a former British colony and write the next chapter in our
#         history as a growing economic power.
#         """)
#     elif selected == "Should the Women's Charter replace one of the existing ten objects in the module?":
#         st.subheader("Should the Women's Charter replace one of the existing ten objects in the module?")
#         st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
#         st.markdown("""
#         In 1961, the Women's Charter was passed in Singapore Parliament, with the
#         intention to improve and protect the legal rights of women in Singapore. While it was
#         initially designed to ensure greater equality in legal matters such as marriage and
#         housing, this Act has left behind a legacy by inspiring more similar initiatives to be set up
#         in Singapore, including the formation of AWARE to further promote gender equality. Given
#         how the roles of the two genders have evolved throughout the course of our history, I
#         strongly support the idea of including the Women's Charter as one of the ten featured
#         objects in the future iterations of this module.

#         For starters, we should first understand why this Act was introduced in the first
#         place. During the colonial era in Singapore, females were confined to the role of
#         housewife and caregiver, given the traditional religious and socio-cultural norms at that
#         point of time. An example of this would be the membership system in the Singapore
#         Recreation Club, with females only being allowed to register as members in 1956 (73
#         years after the club's founding) to participate in its various sporting and social activities,
#         which were initially only catered to men. In contrast, males were seen to be the more
#         dominant gender especially due to the prevalence of polygamy, reiterating the stance that
#         women were indeed inferior to men at that point of time. Later in the colonial era, the
#         British government introduced the Chinese Protectorate, which mainly focused on
#         protecting women from illegal prostitution. While this only served to preserve the basic
#         human rights of women in the country, this was an acknowledgement that more can be
#         done for women to be treated more equally to men. In a sense, introducing the Women's
#         Charter could be seen as a step forward from the Chinese Protectorate, as it no longer
#         merely focuses on basic human rights of women, but rather to introduce more legal rights
#         in favour of women, especially in important aspects such as housing, marriage and
#         children.

#         While the introduction of the Women's Charter was indeed successful in eventually
#         banning polygamy by the 1960s, there was a declining interest in sustaining this women's
#         rights movement afterwards, as its introduction had already achieved its main purpose
#         and there was no incentive to further promote gender equality at that point of time. As a
#         result, an all-male Parliament was eventually formed from 1970 to 1984, with patriarchal
#         policies being introduced once again. These included the announcement of a quota to
#         restrict female medical students, as well as the compulsory offering of home economics
#         as a subject for lower secondary girls. Such acts eventually led to the formation of
#         AWARE in 1985, which set to undo such discriminatory policies against women and
#         promote greater gender equality once again. The introduction of AWARE was indeed a
#         big success, making use of its vision to provide support on various problems largely faced
#         by women, including domestic violence, sexual assault, single parenthood and workplace
#         harassment. As such, I believe that the Women's Charter, as well as its accompanying
#         history of emphasising the importance of gender equality in the long run, should indeed
#         be an object for this module, so that students recognise its value especially in today's
#         ever-changing society.

#         With regards to which current object should be replaced in favour of the Women's
#         Charter, however, I believe that the Sound Blaster should be removed as an object of the
#         module. Given the more economic nature of the topic, I feel that the idea of discussing a
#         Singaporean invention does not fit as well as the other objects, especially when this is a
#         module offered by the Department of History in the National University of Singapore.
#         If we were to look back at all the other objects that were taught in this module, be
#         it an artefact from the pre-colonial era (Singapore Stone), a club established during the
#         colonial era (Singapore Recreation Club), or modern objects such as the Kallang Roar
#         and the movie 'I Not Stupid', what they have in common is that they have played a
#         significant role in Singapore's history, and have contributed in forging the Singaporean
#         identity in the process. Looking at the 'I Not Stupid' movie for example, it has established
#         a legacy of revamping the current educational system, proving that such filmmaking can
#         be influential in establishing Singapore's history as a progressing society if done right.
#         While I recognise and applaud the efforts of Sim Wong Hoo and how his innovation
#         of the Sound Blaster technology had contributed to our economy, I feel that this invention
#         is not unique enough to be recognised as an 'object' of Singapore's history. Such
#         advancements in technology are less distinguishable between the different countries in
#         our global economy, especially with many people around the world possibly having the
#         misconception that these inventions largely only occur in larger countries such as the
#         USA and China. In summary, this invention does not seem as impactful in influencing
#         Singapore's history compared to the other objects, which explains my decision to exclude
#         this object in favour of the Women's Charter if possible.
#         Singapore's history compared to the other objects, which explains my decision to exclude
#         this object in favour of the Women's Charter if possible.

#         To conclude, the story of the Women's Charter and the subsequent formation of
#         AWARE should indeed be included as an object in this module. This has taught us the
#         importance of supporting the movement of gender equality, as well as the consequences
#         of not sustaining such movements in the long run. I believe that this is an important lesson
#         that Singaporeans can learn from, especially with the rising prevalence of women in our
#         local workforce, including those in professional, managerial, executive and technical
#         professions, which is a testament of the changing gender roles in our society today.

#         *For context, this module is offered by the Department of History, Faculty of Arts and Social Sciences at the National University of Singapore. The ten objects that exemplify Singapore's rich history are:*
#         1. Singapore Stone
#         2. White Sand
#         3. Abdullah's Story
#         4. Singapore Recreation Club
#         5. Old Ford Factory
#         6. Majulah Singapura
#         7. Block 45, Stirling Road
#         8. Kallang Roar
#         9. Sound Blaster
#         10. I Not Stupid
#         """)
#     elif selected == "Does gender inequality still have a place in Singapore's society today?":
#         st.subheader("Does gender inequality still have a place in Singapore's society today?")
#         st.write("April 2, 2022 | [Term Paper](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
#         st.markdown("""
#         On April 24, 2021, a new resolution was passed for women in the Singapore
#         Recreation Club (SRC) to be entitled with the same rights and privileges as male
#         members. With this new resolution, women now have voting rights, and can be elected
#         to the club's management committee. On top of this, they may assume the membership
#         of either their spouse or their male next-of-kin. This news was announced after several
#         failed attempts to amend the club's constitution over the course of its 137 year history
#         since its founding.

#         This made me wonder: as one of Singapore's most well-established clubs, what
#         took it so long to amend this constitution and allow for female members to have equal
#         rights? Furthermore, to what extent was gender inequality prevalent over the course of
#         Singapore's history? Therefore, this term paper intends to explore the history of gender
#         inequality in Singapore, and whether it still has a place in our society today.
#         For starters, we first need to understand the history of SRC. Originating as a
#         crickets' club for Eurasian players in 1883, the club gradually expanded to allow for more
#         sports including football and hockey to be played, with various matches held against
#         fellow clubs such as the Penang and Malacca Recreation Clubs. However, SRC
#         membership was initially restricted to Eurasian males, with memberships only being made
#         open to non-Europeans from 1955 onwards. Furthermore, European females were only
#         formally allowed as guests in 1927, before subscription memberships were open to
#         women of all races by 1956 as well, about one year after memberships were open to non-
#         Eurasian men. With drinking as a main social activity and occasional tea parties as SRC's
#         non-sport social activities, it was no surprise that the club had only catered to men, which
#         reinforced the stereotype against women as stay-at-home caregivers who did not enjoy
#         such activities, especially before World War II.

#         From a more macro perspective, the above-mentioned restriction of women's
#         enjoyment of such activities was also representative of the attitude towards women in
#         colonial Singapore. With Singapore under British rule, women were "subjected to sociocultural
#         and religious pressures to conform to the roles of wife and mother and to lead a
#         more secluded life". This had contrasted with men, whose gender was viewed to be more
#         dominant based on the traditions of different cultures in Singapore. In addition, men were
#         allowed to have multiple female partners, solidifying the perspective that women were
#         inferior to men at that point of time.

#         From the 1950s however, there was an increase in female leaders emerging in
#         Singapore's politics, leading the charge to pursue gender equality in the country. For
#         instance, the establishment of the Women's Charter by the Singapore government in
#         1961 had aimed to provide equal rights to both genders. Clauses in the Charter include
#         the compulsory registration of all marriages as well as providing women with the rights to
#         their own housing, marriage and children if applicable. This was a big improvement from
#         the Chinese Protectorate that was established during the colonial era, which mainly
#         targeted at tackling the illegal prostitution of women. This showed that the local
#         government did try to push for women to be treated as equals to men, instead of merely
#         taking care of their basic human needs.

#         In terms of job opportunities, more Singaporean women are seeking full-time
#         employment by either pursuing higher education or entering the workforce, especially
#         over the recent years. This breaks the traditional norm of women as stay-at-home
#         caregivers, as more women aim to live independently as well. This is evident in the rise
#         of the female labour force participation rate from 60.8% in 2018 to 61.2% in 2020.
#         Furthermore, the increase in Professionals, Managers, Executives and Technicians from
#         50% in 2010 to 59% in 2020 amongst female employees shows that women, just like
#         men, are capable of upskilling themselves and contributing meaningfully to the Singapore
#         economy when given the opportunity. While a pay gap still exists between employed
#         males and females in Singapore, the inclusion of more women especially in higher
#         positions within the local workforce has helped to decrease this gender pay gap, paving
#         the way towards gender equality based on the employment aspect.

#         To answer the question that I posed earlier: I believe that gender inequality should
#         not have a place in Singapore's society today. While there is still more that can be done
#         to ensure equal opportunities for both men and women in the long run, we have to
#         recognise that the local government today is indeed trying to advocate for women's rights
#         in Singapore. Its efforts in setting up the Women's Charter and encouraging more women
#         to take up higher positions in the workforce, for example, have likewise spurred similar
#         initiatives amongst external organisations. This includes the founding of organisations
#         such as AWARE for women to seek assistance against physical and emotional abuse, as
#         well as the recent news of allowing women to take up management committee positions
#         as well as have voting rights in SRC.

#         As mentioned by Law and Home Affairs Minister Shanmugam in February 2021,
#         perhaps one way to promote gender equality more in Singapore is for employees of both
#         genders to be entitled to equal parental leave, as observed in certain European countries.
#         This would grant men the opportunity to experience the caregiver role as normally
#         experienced by their spouses. In fact, encouraging such role reversals between both
#         genders would allow mutual understanding of each other's roles, strengthening internal
#         familial ties in the process.

# At the end of the file, before any other code
