import speech_recognition as sr
import webbrowser as wb
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = recognizer.listen(source)

        print(recognizer.recognize_sphinx(audio))
        if 'youtube' in recognizer.recognize_google(audio):
            recognizer = sr.Recognize()
            url='https://www.youtube.com/watch?v=-3am_5jMzJ4'
            with sr.Microphone() as source:
                print('Search your query')
                audio = recognizer.listen(source)
                try:
                    get = recognizer.recognize_google(audio)
                    print(get)
                    wb.get.open_new(url+get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
