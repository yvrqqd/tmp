import streamlit as st
from groq import Groq



with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages/city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages/city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages/random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")


st.text_area("Сообщение:",value="Здравствуйте, сколько стоит доставка цветов в город Екб? Нужно до завтра. Спасибо.", key="input_message")
st.button("Определить город", key="submitted")

client = Groq(
    api_key=st.secrets["groq_token"]
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=100,
    top_p=1
)

st.success(chat_completion.choices[0].message.content)