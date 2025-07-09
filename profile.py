import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from datetime import datetime
import json

# --- Page config ---
st.set_page_config(page_title="Md Mubasir | Profile", page_icon="💼", layout="wide")

experience = f"{round(((datetime.today() - datetime(2021, 3, 1)).days / 365.25) * 2) / 2} years"

# Read lotti file
with open('Animation - 1752049917942.json', 'r') as f:
    lottie_coding = json.load(f)

profile_pic_url = "https://media.licdn.com/dms/image/v2/D4D03AQEUhC9qNHI9cA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1706820835384?e=1757548800&v=beta&t=aqcIetrgACnwbgoINQtz07eTKQnhz-AhKKUsWkEKi-o"  # Replace with actual image URL
profile_pic = Image.open(requests.get(profile_pic_url, stream=True).raw)


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
st.subheader("Senior Software Engineer | Big Data & AI Solutions Engineer")
st.write("📍 Kolkata, India | [LinkedIn](https://linkedin.com/in/mdmubasir1998/) | [GitHub](https://github.com/mdmub0587)")
st.markdown("---")

# with open("resume.pdf", "rb") as file:
#     st.download_button(label="📄 Download Resume", data=file, file_name="Md_Mubasir_Resume.pdf", mime="application/pdf")

# --- Content Sections ---
if section == "👤 About Me":
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(lottie_coding, height=336, key="coding")
    with col2:
        st.header("Hi, I'm Mubasir 👋")
        st.write(f"""
        Big Data & AI Solutions Engineer with approximately {experience} years of experience across 
        full-stack development, modern data engineering, and applied AI/ML. Specialized 
        in designing and implementing cloud-native, scalable ETL pipelines using Databricks, 
        AWS, Matillion, and PySpark. Proven ability to lead cross-functional teams, build 
        resilient data platforms, and deliver impactful solutions across domains. Adept at 
        leveraging GenAI, fine-tuning LLMs, and custom-training models to automate workflows 
        and accelerate data-driven decision-making. Passionate about innovating at the 
        intersection of big data systems and machine intelligence.
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
