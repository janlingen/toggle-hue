import requests
from os import getenv
from dotenv import load_dotenv
import json
import speech_recognition as sr


class Hue:
    def __init__(self, ip, user):
        self.ip = ip
        self.user = user
        self.connection = "http://{}/api/{}/".format(self.ip, self.user)

    def get_lights(self):
        data = {}
        response = requests.get(self.connection + "lights")
        if response.status_code == 200:
            data = json.loads(response.text)
        return data

    def toggle_light(self, id):
        data = {}
        response = requests.get(self.connection + "lights/" + str(id))
        if response.status_code == 200:
            data = json.loads(response.text)
        if data["state"]["on"]:
            requests.put(self.connection + "lights/" +
                         str(id) + "/state", json={"on": False})
        else:
            requests.put(self.connection + "lights/" +
                         str(id) + "/state", json={"on": True})


listener = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-US")
            command = command.lower()
            if 'sarah' in command:
                command = command.replace('sarah', '')
                print(command)
                return command
            else:
                return "empty"
    except:
        return "empty"


def run_sarah(hue):
    command = take_command()
    print(command)
    if 'light' in command:
        hue.toggle_light(1)
        hue.toggle_light(2)
    else:
        print('Please say the command again.')


if __name__ == "__main__":
    load_dotenv()
    IP = getenv("IP")
    HUE_USER = getenv("HUE_USER")
    hue = Hue(IP, HUE_USER)
    while True:
        run_sarah(hue)
