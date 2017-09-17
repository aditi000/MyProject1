from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
from termcolor import colored
import re

def send_message():
    friend_choice = select_friend()

    original_image = raw_input(colored("Please Enter the name of the image?", 'blue'))
    pattern = '^[0-9a-zA-Z\s]+\.jpg$'
    if (re.match(pattern, original_image) != None):
        output_path = "output.jpg"
        text = raw_input(colored("What's the secret message u wan't to Convey? ",'blue'))
        Steganography.encode(original_image, output_path, text)
        new_chat = {
            "message": text,
            "Date & Time": datetime.now()
        }

        friends[friend_choice].chats.append(new_chat)

        print colored("Your secret message in the image is ready!", 'green')