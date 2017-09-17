from globals import STATUS_MESSAGES
from termcolor import colored

# updated status message.
updated_status_message = None

def add_status(current_status_message):
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print colored("You don't have any status message currently \n",'red')

    # Ask user for choosing from older older messages.
    default = raw_input(colored("Do you want to select from the older status (y/n)? ",'blue'))

    if default.upper() == "N":
        new_status_message = raw_input(colored("Write the status message do you want to set? ",'blue'))

        # validating users input.
        if len(new_status_message) > 0:
            # adding new status message to the list.
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print "You did not provided any status message. Try again."
    elif default.upper() == 'Y':
        # counter for serial number of messages.
        item_position = 1

        # printing all older status messages.
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        # asking users choice.
        message_selection = int(raw_input("\nChoose from the above messages \n"))

        # validating users input.
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print colored('Your updated status message is: %s','blue') % (updated_status_message)
        else:
            print "Invalid choice. Try again."
    else:
        print colored('The choice you Entered is not valid! Press either y or n.','red')

    return updated_status_message