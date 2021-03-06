from add_status import add_status
from add_friend import add_friend
from select_friend import select_friend
from send_message import send_message
from read_message import read_message
from read_chat_history import read_chat_history
#chat function defined
def start_Chat(name,age,rating,status):
    from globals import current_status_message
    if not(age>12 and age<50):
        error_message="Invalid age. Please Try again"
        print error_message
    else:
        welcome_message="Authentication complete. Welcome\n" \
                      "Name : " + name + "\n" \
                      "Age: " + str(age) + "\n" \
                      "Rating: " + str(rating) + "\n" \
                      "Online: " + str(status) + "\n" \
                      "Proud to have you onboard"
        print welcome_message

        #displaying show menu
        show_menu=True
        while show_menu:
            menu_choice="What do you want to do? \n " \
                       "1. Add a status update \n " \
                       "2. Add a friend \n " \
                       "3. Send a secret message \n " \
                       "4. Read a secret message \n " \
                       "5. Read Chats from a user \n " \
                       "6. Close Application \n"
            flag=True
            while flag:
                try:
                    result = int(raw_input(menu_choice))
                    flag = False
                except Exception:
                    print "Invalid choice. Try again."
                else:
                    # validating users input
                    if(result==1):
                        current_status_message=add_status(current_status_message)
                    elif(result==2):
                        number_of_friends=add_friend()
                        print 'You have %d friends'%(number_of_friends)
                    elif (result == 3):
                        send_message()
                    elif(result==4):
                        #select_friend()
                        read_message()
                    elif(result==5):
                        read_chat_history()
                    elif(result==6):
                        #Close application
                        show_menu=False
                    else:
                        print 'Wrong Choice,Try again'