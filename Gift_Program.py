import time
import webbrowser
import pyttsx3
from pytube.cli import on_progress
import pytube
from os.path import expanduser
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# Credits
    #~~~~~~~~~~~~~~~ GitHub account: BUTTERBOT333 ~~~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~ Stack Overflow: BUTTERBOT333 ~~~~~~~~~~~~~~~#

# Functions -----------------
def talk(txt):
    print(txt)
    engine.say(txt)
    engine.runAndWait()
def verifyCode():
    url = input()
    url = "https://youtu.be/"+url
    try:
        pytube.YouTube(url, on_progress_callback = on_progress)
        talk("Code verified. Proceeding")
        return False, url
    except:
        talk("Im sorry but I could not varify your code. Please try again :'( ")
        return True, ""

# Start ---------------------
talk('Hello!\nThis is Butterbot333\'s bot.\nIf youre hearing this then you trusted me enough to download an exe file. Thank you!')
talk('Audio is very important in this so please get your headphones.\nType anything and hit enter to continue :)')
input(" ~ waiting... ~\n")

talk("Now, lets get to the main event!")
talk("If you recall, you were given a special authority code.")
talk("This code is special to you and you only. It not only lets you access to the program but it is also a symbol of your\nimportance to me. But dont tell anyone... its embarrassing")
talk("Now please enter said code and press enter")
true = True
while true:
    true, url = verifyCode()
talk("\nNow that we scrappped off all and any intruders")
talk("Please focus youre attention on the new window.\nPlease do NOT close this program!")
webbrowser.open(url)
true = True
while true:
    i = input("Enter SUPER CODE\n")
    if i.lower() == "happy christmas":
        true = False
pytube.YouTube(url).streams.first().download(expanduser('~/Videos'))
talk("Thank you for your time. It really means a lot")
talk("Oh, by the way, check your videos folder ;) ")
talk("You can now close and delete this program")

#ZO9sZ8ZvoKg