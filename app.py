# # app.py
# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# from chatBot import MyChatBot

# import logging
# logging.getLogger("streamlit.runtime").setLevel(logging.ERROR)


# # Init
# st.set_page_config(page_title="Audio Resume Chatbot", page_icon="MazBot")
# st.title(" Voice-Powered Resume Chatbot")
# st.markdown("Ask questions about *your* resume using your voice!")

# # Load the chatbot (cache to avoid reloading)
# @st.cache_resource
# def load_bot():
#     return MyChatBot()

# bot = load_bot()

# # Initialize TTS engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 160)

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info(" Listening for your question...")
#         r.adjust_for_ambient_noise(source)
#         audio_data = r.listen(source, timeout=5, phrase_time_limit=10)
#         st.success(" Received voice input. Converting to text...")
#     try:
#         text = r.recognize_google(audio_data)
#         st.success(f"You said: '{text}'")
#         return text
#     except sr.UnknownValueError:
#         st.error("Could not understand audio.")
#         return None
#     except sr.RequestError as e:
#         st.error(f"API error: {e}")
#         return None

# speaking = False

# def speak(text):
#     global speaking
#     if speaking:
#         return  # Skip if already speaking
#     try:
#         speaking = True
#         engine.stop()
#         engine.say(text)
#         engine.runAndWait()
#     except RuntimeError as e:
#         print("Speech error:", e)
#     finally:
#         speaking = False

# # Session state for chat history
# if "chat" not in st.session_state:
#     st.session_state.chat = []

# # Start chat
# if st.button("Ask a question with your voice"):
#     question = listen()
#     if question:
#         with st.spinner(" Thinking..."):
#             answer = bot.ask(question)
#         st.session_state.chat.append(("You", question))
#         st.session_state.chat.append(("Bot", answer))
#         speak(answer)

# # Display conversation
# for sender, msg in st.session_state.chat:
#     if sender == "You":
#         st.markdown(f"** You:** {msg}")
#     else:
#         st.markdown(f"** Bot:** {msg}")












# import streamlit as st
# import pyttsx3
# import speech_recognition as sr
# from chatBot import MyChatBot  # assume your chatbot logic is in chatbot.py

# import logging
# logging.getLogger("streamlit.runtime").setLevel(logging.ERROR)

# st.set_page_config(page_title="Audio Chatbot")

# # Initialize engine only once
# if "engine" not in st.session_state:
#     st.session_state.engine = pyttsx3.init()

# if "bot" not in st.session_state:
#     st.session_state.bot = MyChatBot()

# # Listen to user's speech
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("Say something...", icon="🎤")
#         audio_data = recognizer.listen(source, phrase_time_limit=10)
#         try:
#             return recognizer.recognize_google(audio_data)
#         except sr.UnknownValueError:
#             return "Sorry, I could not understand your voice."
#         except sr.RequestError:
#             return "Speech recognition service is not available."

# # Speak the bot's answer
# def speak(text):
#     try:
#         st.session_state.engine.stop()  # stop any previous speech
#         st.session_state.engine.say(text)
#         st.session_state.engine.runAndWait()
#     except RuntimeError as e:
#         st.warning(f"Speech error: {e}")

# st.title("🎙️ Voice Chatbot")

# if st.button("Speak Now"):
#     question = recognize_speech()
#     st.markdown(f"**You said:** {question}")
#     with st.spinner("Thinking..."):
#         answer = st.session_state.bot.ask(question)
#         st.success("Bot replied:")
#         st.write(answer)
#         speak(answer)

















# import streamlit as st
# import pyttsx3
# import speech_recognition as sr
# from chatBot import MyChatBot

# st.set_page_config(page_title="Voice Chatbot", layout="centered")

# def reset_engine():
#     try:
#         st.session_state.engine.stop()  # stop any current speech
#         st.session_state.engine = pyttsx3.init()  # reinitialize clean engine
#     except Exception as e:
#         st.warning(f"Reset failed: {e}")


# # # Session state setup
# if "engine" not in st.session_state:
#     st.session_state.engine = pyttsx3.init()
# if "bot" not in st.session_state:
#     st.session_state.bot = MyChatBot()
# if "processing" not in st.session_state:
#     st.session_state.processing = False


# # Function to recognize speech
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎙️ Say something...", icon="🎤")
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
#             return recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError:
#             return "I didn't hear anything. Please try again."
#         except sr.UnknownValueError:
#             return "Sorry, I couldn't understand that."
#         except Exception as e:
#             return f"Speech error: {str(e)}"


# # Function to speak the text
# def speak(text):
#     try:
#         engine = pyttsx3.init()  # create fresh engine every time
#         engine.say(text)
#         engine.runAndWait()
#         engine.stop()  # forcefully end to avoid loop issues
#     except Exception as e:
#         st.warning(f"Audio playback issue: {e}")


# # Title
# st.markdown("<h1 style='color:white;'>🎙️ Voice Chatbot</h1>", unsafe_allow_html=True)

# # Disable button during processing
# disabled = st.session_state.processing

# # if st.button("🎤 Speak Now", disabled=disabled):
# #     st.session_state.processing = True

# #     question = recognize_speech()
# #     st.markdown(f"**You said:** {question}")

# #     with st.spinner("Thinking..."):
# #         answer = st.session_state.bot.ask(question)
# #         st.success("Maaz replied:")
# #         st.markdown(f"<div style='background-color:#003300; padding:10px; border-radius:8px; color:white;'>{answer}</div>", unsafe_allow_html=True)
# #         speak(answer)

# #     st.session_state.processing = False


# if st.button("🎤 Speak Now", disabled=disabled):
#     st.session_state.processing = True
#     try:
#         reset_engine() 
#         question = recognize_speech()
#         st.markdown(f"**You said:** {question}")

#         with st.spinner("Thinking..."):
#             answer = st.session_state.bot.ask(question)
#             st.success("Maaz replied:")
#             st.markdown(f"<div style='background-color:#003300; padding:10px; border-radius:8px; color:white;'>{answer}</div>", unsafe_allow_html=True)
#             speak(answer)

#     except Exception as e:
#         st.error(f"❌ Error occurred: {e}")
#     finally:
#         st.session_state.processing = False













import streamlit as st
import pyttsx3
import speech_recognition as sr
from chatbot import MyChatBot

st.set_page_config(page_title="Voice Chatbot", layout="centered")

if "bot" not in st.session_state:
    st.session_state.bot = MyChatBot()
if "processing" not in st.session_state:
    st.session_state.processing = False

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Say something...", icon="🎤")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return "I didn't hear anything. Please try again."
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except Exception as e:
            return f"Speech error: {str(e)}"

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        st.warning(f"Audio playback issue: {e}")

st.markdown("<h1 style='color:white;'>🎙️ Voice Chatbot</h1>", unsafe_allow_html=True)

disabled = st.session_state.processing

if st.button("🎤 Speak Now", disabled=disabled):
    st.session_state.processing = True
    try:
        question = recognize_speech()
        st.markdown(f"**You said:** {question}")

        with st.spinner("Thinking..."):
            answer = st.session_state.bot.ask(question)
            st.success("Maaz replied:")
            st.markdown(
                f"<div style='background-color:#003300; padding:10px; border-radius:8px; color:white;'>{answer}</div>",
                unsafe_allow_html=True,
            )
            speak(answer)
    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
    finally:
        st.session_state.processing = False
