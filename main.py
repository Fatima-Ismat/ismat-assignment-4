# from dotenv import load_dotenv
# import streamlit as st
# import requests
# import os

# load_dotenv()

# # --- Page Setup ---
# st.set_page_config(page_title="Perfume Muse by Ismat Fatima 💖", page_icon="🌸")
# st.title("🌸 Perfume Muse by Ismat Fatima")
# st.markdown("Enter a mood or perfume name, and let the AI paint a poetic fragrance story for you ✨")

# # --- User Input ---
# user_input = st.text_input("💐 Describe your scent or mood:")

# # --- HuggingFace API ---
# API_KEY = os.getenv("HUGGINGFACE_API_KEY")
# API_URL = "https://api-inference.huggingface.co/models/facebook/opt-350m"

# def get_fragrance_story(prompt):
#     if not API_KEY:
#         return {"error": "API Key not found. Please set HUGGINGFACE_API_KEY in your .env file."}
#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     payload = {"inputs": f"Write a poetic perfume story for this: {prompt}"}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json() if response.status_code == 200 else {"error": "API call failed."}

# # --- Generate Response ---
# if st.button("💫 Generate Perfume Story"):
#     if user_input.strip() == "":
#         st.warning("Please enter a scent or mood! 🌷")
#     else:
#         with st.spinner("Blending the notes... 🧪"):
#             result = get_fragrance_story(user_input)
#             if "error" in result:
#                 st.error(result["error"])
#             else:
#                 story = result[0]["generated_text"]
#                 st.success("Here’s your fragrance story ✨")
#                 st.markdown(f"> {story.strip()}")

# # --- Footer ---
# st.markdown("---")
# st.markdown("Created with 🌸 by Fatima | Your future fragrance queen 👑")

from dotenv import load_dotenv
import streamlit as st
import requests
import os

load_dotenv()

# --- Page Setup ---
st.set_page_config(page_title="Perfume Muse by Ismat Fatima 💖", page_icon="🌸")
st.title("🌸 Perfume Muse by Ismat Fatima")
st.markdown("Enter a mood or perfume name, and let the AI paint a poetic fragrance story for you ✨")

# --- Sidebar Mood Selector ---
with st.sidebar:
    st.title("🎀 Mood Options")
    selected_mood = st.selectbox("Choose a mood to inspire your perfume:", 
                                 ["Romantic", "Fresh", "Mystic", "Bold", "Calm", "Sensual"])

# --- User Input ---
user_input = st.text_input("💐 Describe your scent or mood:")

# --- HuggingFace API ---
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/gpt2"  # Use a lighter model

# st.write("🔑 API_KEY:", API_KEY="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")


def get_fragrance_story(prompt):
    if not API_KEY:
        return {"error": "API Key not found. Please set HUGGINGFACE_API_KEY in your .env file."}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": f"Write a {selected_mood.lower()} poetic perfume story for this: {prompt}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"error": "API call failed."}

# --- Generate Response ---
if st.button("💫 Generate Perfume Story"):
    if user_input.strip() == "":
        st.warning("Please enter a scent or mood! 🌷")
    else:
        with st.spinner("Blending the notes... 🧪"):
            result = get_fragrance_story(user_input)
            if "error" in result:
                st.error(result["error"])
            else:
                story = result[0]["generated_text"]
                st.success("Here’s your fragrance story ✨")
                st.markdown(f"> {story.strip()}")

# --- Footer ---
st.markdown("---")
st.markdown("Created with 🌸 by Ismat Fatima | Your future fragrance queen 👑")
