import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# --- Page config ---
st.set_page_config(page_title="Md Mubasir | Profile", page_icon="💼", layout="wide")

# --- Load assets ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_1pxqjqps.json")
profile_pic_url = "https://media.licdn.com/dms/image/v2/D4D03AQEUhC9qNHI9cA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1706820835384?e=1757548800&v=beta&t=aqcIetrgACnwbgoINQtz07eTKQnhz-AhKKUsWkEKi-o"  # Replace with actual image URL
profile_pic = Image.open(requests.get(profile_pic_url, stream=True).raw)

# --- Apply Default Dark Mode Style ---
# st.markdown(
#     """
#     <style>
#     body, .stApp {
#         background-color: #0e1117;
#         color: #FAFAFA;
#     }
#     .css-18e3th9 {
#         background-color: #0e1117;
#     }
#     .css-1d391kg, .css-1v3fvcr, .css-1cpxqw2 {
#         background-color: #262730;
#     }
#     [data-testid="stSidebar"] > div:first-child {
#         background-color: #1e1e1e;
#         color: #FAFAFA;
#     }
#     [data-testid="stSidebar"] label, .stRadio > div > label {
#         color: #FAFAFA !important;
#         font-weight: 600;
#         font-size: 1rem;
#     }
#     .stRadio > div > div {
#         background-color: #333 !important;
#         border-radius: 0.5rem;
#         padding: 0.5rem;
#     }
#     .stRadio > div > div:hover {
#         background-color: #444 !important;
#     }
#     .stRadio > div > div span, .stRadio > div label span, .stSidebar span {
#         color: #FAFAFA !important;
#         font-weight: 600;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# --- Sidebar ---
st.sidebar.image(profile_pic, width=120)
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "👤 About Me",
    "💼 Experience",
    "🧰 Skills",
    "🚀 Projects",
    "🎓 Education",
    "📜 Certifications",
    "📫 Contact"
])
# --- Header ---
st.title("👨‍💼 Md Mubasir")
st.subheader("Senior Software Engineer | Big Data Engineer | AWS Expert")
st.write("📍 Kolkata, India | [LinkedIn](https://linkedin.com/in/mdmubasir1998/) | [GitHub](https://github.com/mdmub0587)")
st.markdown("---")

# with open("resume.pdf", "rb") as file:
#     st.download_button(label="📄 Download Resume", data=file, file_name="Md_Mubasir_Resume.pdf", mime="application/pdf")

# --- Content Sections ---
if section == "👤 About Me":
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(lottie_coding, height=300, key="coding")
    with col2:
        st.header("Hi, I'm Mubasir 👋")
        st.write("""
        Highly experienced Big Data Engineer with expertise in designing, building, and optimizing data engineering solutions on AWS. 
        Skilled in AWS Glue, Apache Airflow, PySpark, and Databricks. Proven track record of building scalable, efficient ETL pipelines.
        Passionate about leveraging cloud technologies to drive business insights.
        """)

elif section == "💼 Experience":
    st.header("💼 Work Experience")

    st.subheader("Senior Software Engineer @ Tiger Analytics")
    st.write("Mar 2024 – Present | Hybrid")
    st.write("AWS Big Data Engineer | PySpark | Databricks | Matillion")

    st.subheader("Consultant - Application Developer @ Thoughtworks")
    st.write("Jun 2022 – Mar 2024 | Remote")
    st.write("""
    - Built ETL pipelines with AWS Glue, S3, and DynamoDB
    - Added alert systems using SNS
    - Created Presto queries to drive business decisions
    """)

    st.subheader("Graduate Consultant - Application Developer @ Thoughtworks")
    st.write("Jun 2021 – Jun 2022")
    st.write("""
    - Developed AWS Data Lake using Glue, Lambda, Lake Formation
    - Connected Athena with Power BI for business reporting
    """)

    st.subheader("Intern - Application Developer")
    st.write("Mar 2021 – Jun 2021")
    st.write("""
    - Built scalable ETL using Airflow, Spark, and Docker
    - Deployed on EMR for large-scale processing
    """)

elif section == "🧰 Skills":
    st.header("🛠️ Technical Skills")
    st.write("""
    - Python, SQL, PySpark, Scala
    - AWS: Glue, Lambda, S3, Athena, EMR
    - Databricks, Matillion, Airflow
    - Power BI, Presto, Docker
    """)

elif section == "🚀 Projects":
    st.header("🚀 Projects")

    st.subheader("Oil Storage Tank’s Volume Occupancy")
    st.write("YOLOv3-based detection model on satellite images to estimate oil tank volume.")
    st.markdown("[GitHub Link](https://github.com/mdmub0587/Oil-Storage-Tank-s-Volume-Occupancy)")

    st.subheader("Don’t Overfit! II")
    st.write("Kaggle competition with 250 rows, achieved top 5% using RFE + Logistic Regression.")
    st.markdown("[GitHub Link](https://github.com/mdmub0587/Dont-Overfit-II)")

elif section == "🎓 Education":
    st.header("🎓 Education")

    st.subheader("Techno Main - Salt Lake")
    st.write("Bachelor of Technology - BTech, Computer Science Engineering (2017 - 2021)")
    st.write("Grade: 8.78/10")

    st.subheader("Md Jan High School")
    st.write("10+2 (Higher Secondary), Science (2015 - 2017)")
    st.write("Grade: A+, Score: 86%")

elif section == "📜 Certifications":
    st.header("📜 Certifications")
    st.write("""
    - Applied Machine Learning – Applied AI Course (Oct 2020)
    - Applied Deep Learning Capstone – edX (Jun 2020)
    """)

elif section == "📫 Contact":
    st.header("📫 Contact Me")
    st.write("**Email:** mdmubasir@example.com")
    st.write("**LinkedIn:** [linkedin.com/in/mdmubasir1998](https://linkedin.com/in/mdmubasir1998)")
    st.write("**GitHub:** [github.com/mdmub0587](https://github.com/mdmub0587)")

# --- Footer ---
st.markdown("---")
st.markdown("<center>Made with ❤️ in Streamlit | © 2025 Md Mubasir</center>", unsafe_allow_html=True)
