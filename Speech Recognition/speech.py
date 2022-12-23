# ----------------------------------------------------------------------------------------------- #
# Module to Recognize speech and give output as text in console.
import speech_recognition

recognizer = speech_recognition.Recognizer()                         # Setting the Recognizer.

is_on = True
while is_on:

    try:

        with speech_recognition.Microphone() as mic:                 # Turning the microphone on.
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)   # Setting the duration of mic to hear.
            audio = recognizer.listen(mic)                           # Converting the heared into audio.
            text = recognizer.recognize_google(audio)                # Converting to text using google.
            text = text.lower()                                      # Making text lower case.
            print(f"{text}")                                         # Printing text.
            if text == "stop":                                       # A condition to stop program.
                print("Hello Sir closing the program.")
                is_on = False
            if text == "refresh":                                    # A condition to start from first.
                print("Hello sir starting fresh!!!")
                is_on = True

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
# ----------------------------------------------------------------------------------------------- #