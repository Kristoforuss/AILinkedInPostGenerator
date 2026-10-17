import streamlit as st
from openai import OpenAI
import os

os.environ["HF_TOKEN"] = st.secrets["HF_TOKEN"]

st.title("AI LinkedIn Post Generator")

st.write("Write Topics to Generate")

topic = st.text_input("Enter")

if st.button("Generate Post"):
  prompt_template = f"""

  Write a LinkedIn post about {topic}

  Structure the post in the following format:

  1. A catchy intro that grabs attention
  2. A body consisting of exactly 5 sentences explaining the topic
  3. A conclusion that encourage engagement (ask a question or invite opinions)

  Keep the tone professional but engaging.
  Fromat it nicely for LinkedIn.
  """

  client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)
  response = client.chat.completions.create(

      model = "openai/gpt-oss-120b",
      messages = [
        {
          "role": "user","content": prompt_template
        }
      ]
  )
  st.write(response.choices[0].message.content)
#