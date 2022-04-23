'''import speech_recognition as sr
import webbrowser as wb
import pyaudio
recognizer = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search youtube]')
    print('speak now')
    audio = r3.listen(source)
    print(recognizer.recognize_sphinx(audio))
    if 'youtube' in r1.recognize_google(audio):
        r1 = sr.Recognize()
        url='https://www.youtube.com/watch?v=-3am_5jMzJ4'
        with sr.Microphone() as source:
            print('Search your query')
            audio = r1.listen(source)
            try:
                get = r1.recognize_google(audio)
                print(get)
                wb.get.open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))
'''
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
