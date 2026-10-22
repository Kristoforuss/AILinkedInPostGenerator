import streamlit as st
from openai import OpenAI
import os

os.environ["ORCAROUTER_API_KEY"] = st.secrets["ORCAROUTER_API_KEY"]

st.title("AI LinkedIn Post Generator")

st.write("Write Topics to Generate")

topic = st.text_input("Enter")

if st.button("Generate Post"):
    
    # Pastikan user sudah mengisi topik
    if not topic:
        st.warning("Mohon masukkan topik terlebih dahulu.")
    else:
        prompt_template = f"""
        Write a LinkedIn post about {topic}

        Structure the post in the following format:

        1. A catchy intro that grabs attention
        2. A body consisting of exactly 5 sentences explaining the topic
        3. A conclusion that encourage engagement (ask a question or invite opinions)

        Keep the tone professional but engaging.
        Format it nicely for LinkedIn.
        """

        # Inisialisasi client
        client = OpenAI(
            base_url="https://api.orcarouter.ai/v1",
            api_key="ORCAROUTER_API_KEY", # Pastikan untuk mengganti ini dengan API Key asli Anda
        )

        # 3. Menambahkan indikator loading agar UI lebih interaktif (Opsional)
        with st.spinner("Generating your LinkedIn post..."):
            
            response = client.chat.completions.create(
                model="orca/orcaverify-text1.0-free",
                messages=[{"role": "user", "content": prompt_template}],
            )
            
            # 4. Tampilkan hasil langsung ke UI Streamlit
            hasil_post = response.choices[0].message.content
            st.markdown(hasil_post)
