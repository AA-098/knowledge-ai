import streamlit as st
import wikipedia
import re

st.set_page_config(
    page_title="Knowledge AI",
    page_icon="🌌",
    layout="wide"
)

# ---------- SMART QUESTION CLEANER ----------
def clean_query(query):
    query = query.lower()
    query = re.sub(r"what is|who is|define|tell me about|explain|in space|in the universe|\?", "", query)
    return query.strip()

# ---------- DARK UI ----------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0a0f2c, #000000);
    color: white;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.main-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.title {
    font-size: 52px;
    font-weight: bold;
    background: -webkit-linear-gradient(#00d4ff, #6f00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 16px;
    color: #00d4ff;
    letter-spacing: 3px;
    margin-bottom: 40px;
}

.stTextInput > div > div > input {
    background-color: #0f172a;
    color: white;
    border-radius: 20px;
    border: 1px solid #00d4ff;
    padding: 15px;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
}

.stButton > button {
    background-color: #0f172a;
    color: #00d4ff;
    border-radius: 20px;
    border: 1px solid #00d4ff;
    padding: 10px 25px;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #00d4ff;
    color: black;
}

.result-box {
    background-color: #0f172a;
    padding: 25px;
    border-radius: 20px;
    margin-top: 30px;
    box-shadow: 0 0 25px rgba(111, 0, 255, 0.5);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">Knowledge AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">SMART EDUCATION ASSISTANT</div>', unsafe_allow_html=True)

# ---------- INPUT ----------
user_input = st.text_input("Ask anything about science, space, history...")

if st.button("🚀 Search"):
    if user_input:
        try:
            cleaned_query = clean_query(user_input)

            search_results = wikipedia.search(cleaned_query)

            if search_results:
                try:
                    summary = wikipedia.summary(search_results[0], sentences=6)
                except wikipedia.exceptions.DisambiguationError as e:
                    summary = wikipedia.summary(e.options[0], sentences=6)

                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader(f"🌍 {search_results[0]}")
                st.write(summary)
                st.markdown('</div>', unsafe_allow_html=True)

            else:
                st.warning("No relevant information found. Try different keywords.")

        except Exception as e:
            st.error(f"Unexpected error: {e}")
    else:
        st.warning("Please enter a question.")

st.markdown('</div>', unsafe_allow_html=True)
