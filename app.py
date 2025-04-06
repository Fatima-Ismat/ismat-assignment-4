# from dotenv import load_dotenv
# import streamlit as st
# import requests
# import os

# load_dotenv()




# print("Current working directory:", os.getcwd())
# print("API_KEY from env:", os.getenv("HUGGINGFACE_API_KEY"))


# # --- UI Design ---
# st.set_page_config(page_title="Fatima's Vibe Generator ✨", page_icon="💫")
# st.title("✨ Fatima's Vibe Generator")
# st.markdown("Write your mood or challenge and receive a gentle push from the universe 🌌")

# # --- Input ---
# user_input = st.text_input("🌱 What’s on your mind today?")

# # --- HuggingFace API setup ---
# API_KEY = "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"
# # os.getenv("HUGGINGFACE_API_KEY")
# API_URL = "https://api-inference.huggingface.co/models/facebook/opt-350m"

# def generate_message(prompt):
#     if not API_KEY:
#         return {"error": "API Key not found. Please set HUGGINGFACE_API_KEY in your environment."}

#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     payload = {"inputs": f"Motivate me based on this: {prompt}"}
#     response = requests.post(API_URL, headers=headers, json=payload)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "API call failed."}

# # --- Button to trigger AI ---
# if st.button("💌 Send me good vibes"):
#     if user_input.strip() == "":
#         st.warning("Please write something first 💭")
#     else:
#         with st.spinner("Talking to the universe... 🌠"):
#             result = generate_message(user_input)
#             if "error" in result:
#                 st.error(result["error"])
#             else:
#                 ai_output = result[0]["generated_text"]
#                 st.success("💬 Here's your vibe:")
#                 st.markdown(f"> {ai_output.strip()}")
#                 result = generate_message(user_input)
# st.write(result)


# # --- Footer ---
# st.markdown("---")
# st.markdown("Made with ❤️ by Ismat Fatima | Future perfume queen 👑")



from dotenv import load_dotenv
import streamlit as st
import requests
import os

# Load environment variables
load_dotenv()

# Debugging (optional)
print("Current working directory:", os.getcwd())
print("API_KEY from env:", os.getenv("HUGGINGFACE_API_KEY"))

# --- UI Design ---
st.set_page_config(page_title="Fatima's Vibe Generator ✨", page_icon="💫")

# --- Sidebar ---
st.sidebar.title("Vibe Generator Settings 💫")
tone = st.sidebar.selectbox("Select the tone for the vibe:", ("Motivational", "Calm", "Inspirational"))
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Ismat Fatima | Future perfume queen 👑")

# --- Main UI ---
st.title("✨ Fatima's Vibe Generator")
st.markdown("Write your mood or challenge, and receive a gentle push from the universe 🌌")

# --- Input ---
user_input = st.text_input("🌱 What’s on your mind today?")

# --- HuggingFace API setup ---
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/gpt2"  # Use a lighter model


def generate_message(prompt, tone):
    if not API_KEY:
        return {"error": "API Key not found. Please set HUGGINGFACE_API_KEY in your environment."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": f"{tone} vibe for this: {prompt}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed."}

# --- Button to trigger AI ---
if st.button("💌 Send me good vibes"):
    if user_input.strip() == "":
        st.warning("Please write something first 💭")
    else:
        with st.spinner("Talking to the universe... 🌠"):
            result = generate_message(user_input, tone)
            if "error" in result:
                st.error(result["error"])
            else:
                ai_output = result[0]["generated_text"]
                st.success("💬 Here's your vibe:")
                st.markdown(f"> {ai_output.strip()}")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by Ismat Fatima | Future perfume queen 👑")
