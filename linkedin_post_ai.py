import streamlit as st
from openai import OpenAI
import os

os.environ["ORCAROUTER_API_KEY"] = st.secrets["ORCAROUTER_API_KEY"]

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

 from openai import OpenAI

client = OpenAI(
    base_url="https://api.orcarouter.ai/v1",
    api_key="ORCAROUTER_API_KEY",
)

response = client.chat.completions.create(
    model="orcarouter/auto",
    messages=[{"role": "user", "content": prompt_template}],
)

print(response.choices[0].message.content)
#
