# 🎤 Speech-Enabled Chatbot

A modern, interactive chatbot that supports both text and voice input, built with Streamlit, NLTK, and speech recognition technologies.

## ✨ Features

- **Dual Input Methods**: Accept both text and voice input
- **Speech Recognition**: Real-time speech-to-text conversion using Google's Speech Recognition API
- **Intelligent Responses**: Uses TF-IDF vectorization and cosine similarity for contextual responses
- **Web Interface**: Clean, responsive Streamlit web application
- **Natural Language Processing**: Powered by NLTK for text preprocessing and analysis

## 🚀 Technologies Used

- **Streamlit**: Web application framework
- **NLTK**: Natural language processing toolkit
- **SpeechRecognition**: Voice input processing
- **scikit-learn**: Machine learning for text similarity
- **NumPy**: Numerical computations

## 📋 Prerequisites

- Python 3.7+
- Microphone (for speech input)
- Internet connection (for Google Speech Recognition API)

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JohnHika/-Speech-Enabled-Chatbot.git
   cd -Speech-Enabled-Chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:8501
   ```

## 🎯 How to Use

### Text Input
1. Select "Text" as your input method
2. Type your message in the text box
3. Get an instant response from the chatbot

### Voice Input
1. Select "Speech" as your input method
2. Click the "Record" button
3. Speak clearly into your microphone
4. The app will transcribe your speech and provide a response

## 📂 Project Structure

```
├── app.py              # Main Streamlit application
├── chatbot.txt         # Knowledge base for chatbot responses
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔧 Configuration

- **Knowledge Base**: Edit `chatbot.txt` to customize chatbot responses
- **Speech Settings**: Modify speech recognition parameters in `app.py`
- **UI Customization**: Adjust Streamlit interface elements in `app.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- NLTK team for natural language processing tools
- Streamlit team for the web framework
- Google for Speech Recognition API

3. Choose either text or speech input and interact with the chatbot!

## Notes
- Ensure you have a working microphone for speech input.
- You can expand `chatbot.txt` with your own knowledge base.
