import streamlit as st
import requests


with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages/city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages/city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages/random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "accept": "application/json",
    "Authorization": f"Api-Key {st.secrets["token"]}",
    "x-folder-id:": "application/json"
}
data = {
  "modelUri": "string",
  "completionOptions": {
    "stream": false,
    "temperature": 0.5,
    "maxTokens": 10
  },
  "messages": [
    {
      "role": "system",
      "text": "string"
    },
    {
      "role": "user",
      "text": "string"
    }
  ]
}
response = requests.post(url, headers=headers, json=data).json()["alternatives"][0]["message"]["text"]


st.success(response)