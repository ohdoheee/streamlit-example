pip install openai
pip install streamlit

import os
import openai
from PIL import Image
import streamlit as st
from openai.error import InvalidRequestError


openai.api_key = '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'
messages = []
#chatGPT
def openai_completionTurbo(prompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = prompt
    )
    return completion.choices[0].message["content"].strip()

def openai_completion(prompt):
    response = openai.Completion.create(
      #model="gpt-3.5-turbo",
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

#DALLE
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=3,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

try:
    input_text = st.text_area("텍스트를 입력하세요🙋",height=50)
    input_button = st.button("확인")
    openai_answer = openai_completion(input_text)
    if input_button and input_text.strip() != "":
            with st.spinner("로딩 중입니다⌛️"): 
                st.success(openai_answer)            
    if input_text.strip() != "":
        st.markdown(openai_answer)

    image_button = st.button("이미지 생성 중... 🎞")

    if image_button and input_text.strip() != "":
        with st.spinner("로딩 중입니다⌛️"):
            image_url = openai_image(openai_answer)
            #chatgpt_answer = openai_completion(input_text)
            #st.success(chatgpt_answer)
            print(image_url)
            st.image(image_url, caption='OpenAI에서 생성되었음')
    else:
        st.warning("텍스트를 입력하세요! ⚠")
except InvalidRequestError as e:
    print('에러!!!')
    st.markdown("It looks like this request may not follow DALL-E content policy.  \nAsk me the question again")

