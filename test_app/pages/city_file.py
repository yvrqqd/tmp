import streamlit as st
import requests
import pandas as pd
import time



st.session_state["data"] = pd.DataFrame()
st.session_state["ans"] = []

with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages/city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages/city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages/random_greeting.py", label="Рандомное поздравление", icon="1️⃣")

st.info("Квота синхронных запросов 100 в час, поэтому на обработку файла из задания ее не хватит. Перед его загрузкой опробуйте другие ендпоинты.")

st.write("Загрузите файл в том же формате, что был у предоставленного. Первая строка пропускается")
st.code(''',message
0,Привет! Я хочу заказать букет роз доставить в Питер сегодня до 15:00. Можно у вас такое оформить?
1,"Привет, хочу заказать доставку цветов в Новосибирск, сколько это будет стоить?"
2,"Здравствуйте, сколько стоит доставка цветов в г. Екатеринбурге?"
3,"Здравствуйте, сколько стоит доставка цветов в город Екб? Нужно до завтра. Спасибо."''')

uploaded_file = st.file_uploader("Выберите файл")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df.drop(df.index[0], inplace=True)
  st.session_state["data"]=df

for i in range(st.session_state["data"].shape[0]):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "accept": "application/json",
        "Authorization": f"Api-Key {st.secrets['token']}",
        "Content-Type": "application/json"
    }

    body = {
    "modelUri": "gpt://b1gfl2975iijeg2iqtc0/yandexgpt-lite/latest",
    "completionOptions": {
        "stream": False,
        "temperature": 0.05,
        "maxTokens": 5
    },
    "messages": [
        {
        "role": "system",
        "text": "В запросе есть упоминание конкретного города, оно может быть в сокращенной форме и с ошибками. Твоя задача - определить город и написать его название в полной форме. В ответе ничего, кроме наименования упомянутого города быть не должно. Если сообщение содержит вопрос или предложение, в ответе также должен быть только город"
        },
        {
        "role": "user",
        "text": st.session_state["data"].iloc[i].values[1]
        }
    ]
    }
    response = requests.post(url, headers=headers, json=body).json()
    try:
        city = response.get("result","").get("alternatives","")[0].get("message","").get("text","")
        cols = st.columns([2, 5])
        cols[0].code(city)
        cols[1].write(st.session_state["data"].iloc[i].values[1])
        st.session_state["ans"].append(city)
    except:
        st.error("Квота закончилась")
        break
    time.sleep(1)

if len(st.session_state["ans"]) > 0:
    df2 = st.session_state["data"].head(len(st.session_state["ans"]))
    df2['Answer'] = st.session_state["ans"]
    csv_string = df2.to_csv(index=False)
    st.download_button('Download CSV', csv_string, 'text/csv')
