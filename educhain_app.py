import os
import streamlit as st
from educhain import qna_engine, to_pdf, to_csv, to_json
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

st.title("Educhain Demo")

# Load OpenRouter API key from .env file
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Define OpenRouter models
openrouter_models = {
    'WizardLM': 'microsoft/WizardLM-2-8x22B',
    'Mixtral': 'mistralai/Mixtral-8x22B-Instruct-v0.1',
    'Llama3': 'meta-llama/Meta-Llama-3-70B-Instruct',
    'Deepseek': "deepseek/deepseek-chat",
    'QWEN2': "qwen/qwen-2-72b-instruct",
    'Nous-Llama': "nousresearch/hermes-2-pro-llama-3-8b",
    'Gemini-Flash': "google/gemini-flash-1.5"
}

# Function to get the selected model
def get_model(model_name):
    return ChatOpenAI(
        model=model_name,
        openai_api_key=openrouter_api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )

# Sidebar inputs
st.sidebar.header("Educhain Parameters")
topic = st.sidebar.text_input("Topic", value="Indian History")
num_questions = st.sidebar.number_input("Number of Questions", min_value=1, max_value=25, value=3)
difficulty_level = st.sidebar.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
model_name = st.sidebar.selectbox("Model", list(openrouter_models.keys()), index=3)
export_format = st.sidebar.selectbox("Export Format", ["None", "PDF", "CSV", "JSON"])

# Generate questions
if st.button("Generate Questions"):
    selected_model = get_model(openrouter_models[model_name])
    result = qna_engine.generate_mcq(
        topic=topic,
        level=difficulty_level,
        num=num_questions,
        llm=selected_model
    )

    st.write("Generated Questions:")
    for i, question in enumerate(result.questions, start=1):
        st.write(f"Question {i}:")
        st.write(question.question)
        for j, option in enumerate(question.options, start=1):
            st.write(f"{j}. {option}")
        st.write(f"Correct Answer: {question.correct_answer}")
        st.write("---")

    if export_format != "None":
        if export_format == "PDF":
            to_pdf(result, file_name="questions.pdf")
        elif export_format == "CSV":
            to_csv(result, file_name="questions.csv")
        elif export_format == "JSON":
            to_json(result, file_name="questions.json")

        st.write(f"Questions exported as {export_format}.")