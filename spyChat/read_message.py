from Spy_details import Chat,friends
from select_friend import select_friend
from termcolor import colored
from steganography.steganography import Steganography
def read_message():
    sender = select_friend()

    output_path = raw_input(colored("Enter the name of the file In which secret Text is Hidden ?",'blue'))
    try:
        secret_text = Steganography.decode(output_path)
    except ValueError:
        print colored("No secret message is coded in the image!!", 'red')
        exit()

    secret_text = str(secret_text)
    if secret_text == 'None':
        print colored("No secret message is coded in the image!!",'red')
    else:
        if len(secret_text)>100:
            print colored("Either your friend is talkative or your friend loves to annoy others with bundle of words.",'red')
            choice = raw_input(colored("If u want to Delete ur friend choose:--> 'Y' , If not choose:--> 'N' ",'blue'))
            if choice == "Y":
                del [sender]                              # deleted.
                print colored("Now your Friend is no More in Your Friend List",'green')
                print colored("Select your choice shown Below..",'blue')
            else:
                print colored(secret_text,'blue')

        else:
            new_chat = Chat(secret_text, False)
            friends[sender].chats.append(new_chat)
            print colored("Your secret message has been saved!",'green')