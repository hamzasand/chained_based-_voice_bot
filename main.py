import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1

        print("Speak something...")
        audio = r.listen(source)

        print("processing audio... (STT)")
        stt = r.recognize_google(audio)

        print("You said:", stt)

main()
