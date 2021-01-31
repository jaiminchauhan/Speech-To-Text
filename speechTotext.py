import speech_recognition as sr


def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)
        print("Done...\n")

    try:
        text = r.recognize_google(audio)
        print("you said..... :", text)
    except Exception as e:
        print(e)


get()
