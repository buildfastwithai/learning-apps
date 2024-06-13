from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

llm = ChatOllama(model="qwen2:0.5b")

st.set_page_config(page_title="Personalized Education App", layout="wide")

# Sidebar
st.sidebar.header("Student Profile")
student_name = st.sidebar.text_input("Enter your name:")
student_grade = st.sidebar.selectbox("Select your grade:", ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"))
favorite_subjects = st.sidebar.multiselect("Select your favorite subjects:", ("Math", "Science", "History", "English", "Art", "Music"))
learning_style = st.sidebar.radio("Select your learning style:", ("Visual", "Auditory", "Reading/Writing", "Kinesthetic"))
interests = st.sidebar.text_input("Enter your interests (comma-separated):")
goals = st.sidebar.text_area("What are your learning goals?")
dark_mode = st.sidebar.checkbox("Enable dark mode")

if dark_mode:
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["Personalized Lessons", "Adaptive Quizzes", "Project Ideas", "Career Guidance"])

with tab1:
    st.header("Personalized Lessons")
    lesson_topic = st.text_input("Enter a topic you want to learn about:")
    if st.button("Generate Lesson"):
        lesson_prompt = ChatPromptTemplate.from_template("""
        Create a personalized lesson on the topic of {topic} for a {grade} grade student named {name}.
        Consider their favorite subjects ({subjects}), learning style ({learning_style}), and interests ({interests}).
        Provide examples and explanations that align with their goals: {goals}.
        """)
        
        lesson_chain = lesson_prompt | llm
        lesson_result = lesson_chain.invoke({"topic": lesson_topic, "grade": student_grade, "name": student_name, 
                                             "subjects": ", ".join(favorite_subjects), "learning_style": learning_style,
                                             "interests": interests, "goals": goals})
        st.write(lesson_result.content)

with tab2:
    st.header("Adaptive Quizzes")
    quiz_topic = st.text_input("Enter a topic for the quiz:")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=5)
    if st.button("Generate Quiz"):
        quiz_prompt = ChatPromptTemplate.from_template("""
        Create an adaptive quiz with {num_questions} questions on the topic of {topic} for a {grade} grade student.
        Adjust the difficulty based on their performance. Provide explanations for incorrect answers.
        """)
        
        quiz_chain = quiz_prompt | llm
        quiz_result = quiz_chain.invoke({"topic": quiz_topic, "grade": student_grade, "num_questions": num_questions})
        st.write(quiz_result.content)

with tab3:
    st.header("Project Ideas")
    if st.button("Generate Project Ideas"):
        project_prompt = ChatPromptTemplate.from_template("""
        Suggest 3 engaging project ideas for a {grade} grade student interested in {subjects}.
        The projects should align with their learning style ({learning_style}), interests ({interests}), and goals: {goals}.
        Provide a brief description for each project idea.
        """)
        
        project_chain = project_prompt | llm
        project_result = project_chain.invoke({"grade": student_grade, "subjects": ", ".join(favorite_subjects),
                                               "learning_style": learning_style, "interests": interests, "goals": goals})
        st.write(project_result.content)

with tab4:
    st.header("Career Guidance")
    career_interest = st.text_input("Enter a career field you're interested in:")
    if st.button("Get Career Advice"):
        career_prompt = ChatPromptTemplate.from_template("""
        Provide career guidance for a {grade} grade student interested in the field of {career}.
        Suggest relevant subjects to focus on, extracurricular activities, and skills to develop.
        Offer advice on how to explore and prepare for a career in this field.
        """)
        
        career_chain = career_prompt | llm
        career_result = career_chain.invoke({"grade": student_grade, "career": career_interest})
        st.write(career_result.content)

st.sidebar.write(f"Welcome, {student_name}! Let's personalize your learning journey!")