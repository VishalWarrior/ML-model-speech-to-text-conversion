from textblob import TextBlob
import speech_recognition as sr

def record_audio_and_analyze_sentiment():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Extracted Text:")
            print(text)
            # Perform sentiment analysis
            blob = TextBlob(text)
            sentiment = blob.sentiment
            print("Sentiment Analysis:")
            print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print("Error in accessing the Google service; {0}".format(e))

if __name__ == "__main__":
    record_audio_and_analyze_sentiment()
