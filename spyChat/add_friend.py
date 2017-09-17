from globals import friends
from termcolor import colored
# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
        'chats': []
    }
    new_friend['name'] = raw_input("Name please: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    # concatination.
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(raw_input("Are they as young as you? We would like to know their age: "))

    new_friend['rating'] = float(raw_input("What about their ratings? "))

    # users input validations
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
        new_friend['is_online'] = True
        friends.append(new_friend)
        print colored('Woah!You are showing your social activeness. Your Friend has been added','blue')
    else:
        print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided','red')

    # returning total no of friends.
    return len(friends)