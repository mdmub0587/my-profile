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

profile_pic = 'profile.png'

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

    st.markdown("<div style='border-left: 3px solid #4F8BF9; padding-left: 15px;'>", unsafe_allow_html=True)

    # Tiger Analytics
    st.markdown("""
    <div style='margin-bottom: 30px;'>
        <h4 style='color:#4F8BF9;margin-bottom:2px;'>Senior Software Engineer @ Tiger Analytics</h4>
        <p><i>📅 Mar 2024 – Present | 🏢 Hybrid</i></p>
        <ul>
            <li>Designed and developed scalable Big Data ETL pipelines with end-to-end orchestration and data quality checks using Databricks, Matillion, and Collibra.</li>
            <li>Created optimized Delta tables in Databricks using AWS S3 sources, and implemented advanced SQL and PySpark logic for performance tuning.</li>
            <li>Integrated AWS services like S3, SNS, Step Functions, and Redshift to create modular, resilient data workflows.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Thoughtworks Consultant
    st.markdown("""
    <div style='margin-bottom: 30px;'>
        <h4 style='color:#4F8BF9;margin-bottom:2px;'>Consultant - Application Developer @ Thoughtworks</h4>
        <p><i>📅 Jun 2022 – Mar 2024 | 🏠 Remote</i></p>
        <ul>
            <li>Built scalable ETL pipelines using AWS Glue, S3, and DynamoDB.</li>
            <li>Implemented alerting systems with Amazon SNS for pipeline health monitoring.</li>
            <li>Wrote optimized Presto SQL queries for business-critical insights and reporting.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Thoughtworks Graduate Consultant
    st.markdown("""
    <div style='margin-bottom: 30px;'>
        <h4 style='color:#4F8BF9;margin-bottom:2px;'>Graduate Consultant - Application Developer @ Thoughtworks</h4>
        <p><i>📅 Jun 2021 – Jun 2022</i></p>
        <ul>
            <li>Engineered an AWS-powered Data Lake with Glue, Lambda, and Lake Formation.</li>
            <li>Integrated Athena with Power BI for real-time analytics dashboards.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Thoughtworks Intern
    st.markdown("""
    <div style='margin-bottom: 30px;'>
        <h4 style='color:#4F8BF9;margin-bottom:2px;'>Intern - Application Developer @ Thoughtworks</h4>
        <p><i>📅 Mar 2021 – Jun 2021</i></p>
        <ul>
            <li>Developed scalable ETL pipelines using Airflow, Scala Spark, and Docker.</li>
            <li>Executed distributed data processing on AWS EMR for large-scale ingestion.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif section == "🧰 Skills":
    st.header("🛠️ Technical Skills")
    def skill_bar(title, percent):
        bar_html = f"""
            <div style='margin-bottom:10px;'>
                <strong>{title}</strong>
                <div style='background-color:#ddd;width:100%;border-radius:5px;'>
                    <div style='width:{percent}%;background-color:#4F8BF9;padding:5px 0;border-radius:5px;text-align:center;color:white;'>
                        {percent}%
                    </div>
                </div>
            </div>
        """
        st.markdown(bar_html, unsafe_allow_html=True)

    st.markdown("""
    <h4>📌 <span style='color:#4F8BF9'>Languages & Tools</span></h4>
    """, unsafe_allow_html=True)
    skill_bar("Python, PySpark, SQL", 95)
    skill_bar(".NET 6, Scala, JavaScript, TypeScript, GraphQL", 75)
    skill_bar("TensorFlow, Sklearn, Pandas, Numpy", 80)

    st.markdown("""
    <h4>☁️ <span style='color:#4F8BF9'>Cloud & Big Data</span></h4>
    """, unsafe_allow_html=True)
    skill_bar("AWS Suite (Glue, S3, Lambda, etc.)", 90)
    skill_bar("Databricks, Apache Airflow", 85)

    st.markdown("""
    <h4>🔄 <span style='color:#4F8BF9'>ETL & Data Tools</span></h4>
    """, unsafe_allow_html=True)
    skill_bar("Matillion, Collibra, Spark, Delta Live Tables", 80)

    st.markdown("""
    <h4>🤖 <span style='color:#4F8BF9'>AI/ML & GenAI</span></h4>
    """, unsafe_allow_html=True)
    skill_bar("GenAI, Model Training/Deployment", 75)

    st.markdown("""
    <h4>📊 <span style='color:#4F8BF9'>Frontend & Other</span></h4>
    """, unsafe_allow_html=True)
    skill_bar("React, Power BI", 70)
    skill_bar("Git, CI/CD, Data Lake, Agile", 85)

elif section == "🚀 Projects":
    st.header("🚀 Projects")

    st.subheader("Oil Storage Tank’s Volume Occupancy")
    st.write("YOLOv3-based detection model on satellite images to estimate oil tank volume.")
    st.markdown("[GitHub Link](https://github.com/mdmub0587/Oil-Storage-Tank-s-Volume-Occupancy)")

    st.subheader("Don’t Overfit! II")
    st.write("Kaggle competition with 250 rows, achieved top 5% using RFE + Logistic Regression.")
    st.markdown("[GitHub Link](https://github.com/mdmub0587/Dont-Overfit-II)")

elif section == "🎓 Education":
    st.markdown("""
        <style>
        .edu-card {
            background-color: #f8f9fa;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
        }
        .edu-card h4 {
            color: #4F8BF9;
            margin-bottom: 6px;
        }
        .edu-card img {
            float: right;
            margin-left: 10px;
            border-radius: 6px;
        }
        .edu-badge {
            background-color: #4F8BF9;
            color: white;
            padding: 3px 8px;
            border-radius: 5px;
            font-size: 0.85em;
        }
        </style>

        <div class="edu-card">
            <img src='http://cse.ticollege.org/img/tmsl-logo.png' width='60'>
            <h4>Techno Main - Salt Lake</h4>
            <p><b>B.Tech in Computer Science & Engineering</b></p>
            <p>📅 <span class="edu-badge">2017 – 2021</span> &nbsp;&nbsp; 🏆 <b>Grade:</b> <span class="edu-badge">8.78 / 10</span></p>
        </div>

        <div class="edu-card">
            <img src='https://cdn-icons-png.flaticon.com/512/1822/1822926.png' width='60'>
            <h4>Md Jan High School</h4>
            <p><b>10+2 (Higher Secondary), Science</b></p>
            <p>📅 <span class="edu-badge">2015 – 2017</span> &nbsp;&nbsp; 🏆 <b>Grade:</b> <span class="edu-badge">A+</span> &nbsp;&nbsp; 🧮 <b>Score:</b> <span class="edu-badge">86%</span></p>
        </div>

        <div class="edu-card">
            <img src='https://cdn-icons-png.flaticon.com/512/1822/1822926.png' width='60'>
            <h4>Md Islamia High School</h4>
            <p><b>10 (Secondary), Science</b></p>
            <p>📅 <span class="edu-badge">2010 – 2015</span> &nbsp;&nbsp; 🏆 <b>Grade:</b> <span class="edu-badge">A+</span> &nbsp;&nbsp; 🧮 <b>Score:</b> <span class="edu-badge">83%</span></p>
        </div>
        """, unsafe_allow_html=True)

elif section == "📜 Certifications":
    st.header("📜 Certifications")
    st.write("""
    - Applied Machine Learning – Applied AI Course (Oct 2020)
    - Applied Deep Learning Capstone – edX (Jun 2020)
    """)

elif section == "📫 Contact":
    st.header("📫 Contact Me")
    st.write("**Email:** talk2mubasir0587@gmail.com")
    st.write("**LinkedIn:** [linkedin.com/in/mdmubasir1998](https://linkedin.com/in/mdmubasir1998)")
    st.write("**GitHub:** [github.com/mdmub0587](https://github.com/mdmub0587)")

# --- Footer ---
st.markdown("---")
st.markdown("<center>Made with ❤️ in Streamlit | © 2025 Md Mubasir</center>", unsafe_allow_html=True)
