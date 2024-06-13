from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

llm = ChatOllama(model="qwen2:0.5b")

st.set_page_config(page_title="Personalized Education App", layout="wide")

# Sidebar
st.sidebar.header("Student Details")
student_name = st.sidebar.text_input("Enter your name:")
student_grade = st.sidebar.selectbox("Select your grade:", ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"))
current_subjects = st.sidebar.multiselect("Select your current subjects:", ("Math", "Science", "History", "English", "Art", "Music"))
learning_style = st.sidebar.radio("Select your learning style:", ("Visual", "Auditory", "Reading/Writing", "Kinesthetic"))
interests = st.sidebar.text_input("Enter your interests (comma-separated):")
goals = st.sidebar.text_area("What are your learning goals?")

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["Interactive Storytelling", "Gamified Challenges", "Virtual Field Trips", "Collaborative Projects"])

with tab1:
    st.header("Interactive Storytelling")
    for subject in current_subjects:
        st.button(f"Generate Story on {subject} for Grade {student_grade}")
    # Rest of the code in this tab remains the same

with tab2:
    st.header("Gamified Challenges")
    for subject in current_subjects:
        st.button(f"Generate {subject} Challenge for Grade {student_grade}")
    # Rest of the code in this tab remains the same

with tab3:
    st.header("Virtual Field Trips")
    for subject in current_subjects:
        st.button(f"Plan {subject} Field Trip for Grade {student_grade}")
    # Rest of the code in this tab remains the same

with tab4:
    st.header("Collaborative Projects")
    for subject in current_subjects:
        st.button(f"Propose {subject} Project for Grade {student_grade}")
    # Rest of the code in this tab remains the same