import speech_recognition as sr

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            with open("extracted_text.txt", "w") as text_file:
                text_file.write(text)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Error in accessing the Google service; {0}".format(e))
            return None

if __name__ == "__main__":
    audio_file_path = 'Speaker_0001_00000.wav'
    extracted_text = audio_to_text(audio_file_path)
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)



from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as text_file:
        text = text_file.read()
    sentiment_score = analyze_sentiment(text)
    if sentiment_score > 0:
        print("Positive sentiment")
    elif sentiment_score < 0:
        print("Negative sentiment")
    else:
        print("Neutral sentiment")
