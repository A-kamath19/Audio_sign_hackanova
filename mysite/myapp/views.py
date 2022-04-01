from django.shortcuts import render
import pyttsx3
import speech_recognition as sr
from translate import Translator
import string
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.
gifs = ['A', 'address', 'ahmedabad', 'all', 'any questions', 'are you angry', 'are you busy', 'are you hungry', 'assam', 'august', 'B', 'banana',
'banaras', 'banglore', 'basketball', 'be careful', 'blood pressure', 'bridge', 'brother' ,'brown', 'C', 'cat', 'chess', 'christmas', 'church', 'cilinic', 'cold',
'D', 'dasara' , 'december', 'diabetes', 'did you finish homework', 'do you have money', 'do you want something to drink', 'do you watch TV',
'dont worry', 'during', 'E', 'F', 'father', 'flower is beautiful', 'G', 'good afternoon', 'good morning', 'good question', 'grapes', 'H', 'hello', 'hindi', 'hindu',
'horse', 'hyderabad', 'i am a clerk', 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre', 'i had to say something but I forgot', 'i like pink colour',
'i love to shop', 'job', 'july', 'june', 'karnataka', 'kerala', 'kilogram', 'krishna', 'L', 'lets go for lunch', 'lose', 'M', 'malayalam', 'mango', 'marathi', 'may', 'mile', 'mother',
'mumbai', 'muslim', 'nagpur', 'national anthem', 'nice to meet you', 'open the door', 'P', 'pakistan', 'please call me later', 'police station', 'post office', 'prime minister',
'pune', 'punjab', 'red', 'saturday', 'shall I help you', 'shall we go together tommorow', 'shop', 'sign language interpreter', 'sister', 'sit down', 'stand up', 'T', 'take care',
'temple', 'there was traffic jam', 'through', 'thursday', 'toilet', 'tomato', 'trophy', 'tuesday', 'urdu', 'usa', 'village', 'wednesday', 'what is the problem', 'what is todays date',
'what is your father do', 'what is your name', 'whats up', 'where is the bathroom', 'where is the police station', 'white', 'win', 'Y', 'you are wrong', 'Z']

def home(request):
    return render(request, 'home.html')

def contactUs(request):
    return render(request, 'contactUs.html')

@xframe_options_exempt
def list(request):
    return render(request, 'list.html')

@xframe_options_exempt
def output(request):
    return render(request, 'output.html')

def frequent(request):
    return render(request, 'frequent.html')

def text_to_speech(request):
    text = request.POST.get('search')
    print(text)
    if text is None:
        text = "Welcome! Please write your text to convert it into speech"
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    # get details of all voices available
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 150)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    # play the speech
    engine.runAndWait()
    return render(request, 'text_to_speech.html')


def speech_to_sign(request):
    lang = request.POST.get('list')
    text = " "
    boolean = False
    out = []
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        try:
            if lang is None:
                output = "Record the text you want to say!"
            else:
                print(lang)
                output = r.recognize_google(audio, language=str(lang))
                translator = Translator(from_lang=lang, to_lang="en-IN")
                output = translator.translate(str(output))
                output = output.lower()

                for c in string.punctuation:
                    output = output.replace(c, "")

                translator1 = Translator(from_lang="en-IN", to_lang=lang)
                text = translator1.translate(output)
                print("You said " + str(output))
        except sr.UnknownValueError:
            output = "Could not understand audio"
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)
        if output != "Record the text you want to say!" and output not in gifs:
            boolean = True
            for i in range(len(output)):
                if output[i] != " ":
                    out.append(output[i])
            output = out
        return render(request, 'speech_to_sign.html', {'data': output, 'lang': text, 'boolean': boolean})


def speech_to_letter(request):
    data = request.POST.get('record')
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        try:
            if data is None:
                output = "Record the letter you want to say!"
            else:
                output = r.recognize_google(audio)
                print("You said " + output)
        except sr.UnknownValueError:
            output = "Could not understand audio"
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)

        data = output
        return render(request, 'speech_to_letter.html', {'data': data})


def text_to_sign(request):
    lang = request.POST.get('list')
    inp = request.POST.get('myInput')
    if lang is None:
        inp = "Select a language and enter the text"
    else:
        translator = Translator(from_lang=lang, to_lang="en-IN")
        inp = translator.translate(str(inp))
        inp = inp.lower()

    for c in string.punctuation:
        inp = inp.replace(c, "")
    print(inp)
    return render(request, 'text_to_sign.html', {'intake': inp})


