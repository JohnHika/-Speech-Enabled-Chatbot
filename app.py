import streamlit as st
import speech_recognition as sr
import nltk
import random
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resources
try:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
except Exception as e:
    st.error(f"Error downloading NLTK data: {e}")

# Load knowledge base
try:
    with open('chatbot.txt', 'r', errors='ignore') as f:
        raw = f.read().lower()
except FileNotFoundError:
    st.error("chatbot.txt file not found. Please ensure the file exists.")
    st.stop()
except Exception as e:
    st.error(f"Error reading chatbot.txt: {e}")
    st.stop()

try:
    sent_tokens = nltk.sent_tokenize(raw)
    lemmer = nltk.stem.WordNetLemmatizer()
except Exception as e:
    st.error(f"Error initializing NLTK components: {e}")
    st.stop()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def Normalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def generate_response(user_input):
    sent_tokens.append(user_input)
    tfidf_vec = TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = tfidf_vec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]
    sent_tokens.pop()
    if score == 0:
        return "I'm sorry, I didn't understand that."
    else:
        return sent_tokens[idx]

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

# Streamlit App
st.title("🎤 Speech-Enabled Chatbot")
input_type = st.radio("Choose your input method:", ["Text", "Speech"])
user_input = ""

if input_type == "Text":
    user_input = st.text_input("Type your message:")
elif input_type == "Speech":
    if st.button("Record"):
        user_input = recognize_speech()
        st.write(f"🗣️ You said: {user_input}")

if user_input:
    response = generate_response(user_input)
    st.markdown(f"💬 **Bot**: {response}")
