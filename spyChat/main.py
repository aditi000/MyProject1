from Spy_details import spy
from start_Chat import start_Chat
import re
print 'Let\'s get Started'
existing=raw_input('Do you want to continue as '+spy.salutation+' '+spy.name+' Y/N:')
#validating user input
if existing.upper()=='Y':
    spy_name=spy.salutation+' '+spy.name
    start_Chat(spy.name,spy.age,spy.rating,spy.spy_is_online)
elif existing.upper()=='N':
    spy.name=raw_input('May I get your name,dear?')
    if len(spy.name)>0:
        name_pattern = '^[a-zA-Z]+\s*[a-zA-Z\s]*$'  # spy name must contain alphabet's only
        if (re.match(name_pattern, spy.name) != None):
            spy_salutation = raw_input('Hey! What should we call you(Mr./Mrs/Miss)?')
            print'Welcome, '+spy.salutation+' '+spy.name+'. We are glad to have you back with us'
            print'Okay!'+spy.name+' I\'d like to know more about you.'
            spy.age=raw_input('How young are you(age)?')
            age_pattern = '^[0-9]{1,3}$'  # only maximum 3 digit numerical value is allowed.
            if (re.match(age_pattern, spy.age) != None):
                spy.age=int(spy.age)
                if int(spy.age)>12 and int(spy.age)<50:
                    spy.rating=raw_input('Woah!Young at heart :) and What about your spy rating[Max:5.00]?')
                    rating_pattern = '^[0-9]{1,2}[.][0-9]{1}$'
                    if (re.match(rating_pattern, spy.rating) != None):
                        spy.rating = float(spy.rating)
                        if (spy.rating >= 0.0 and spy.rating <= 5.00):
                            spy.is_online = True
                            start_Chat(spy.name, spy.age, spy.rating, spy.is_online)
                            if (float(spy.rating) > 1.0) and (float(spy.rating) < 2.5):
                                print 'Hmm..!,You are not bad'
                            elif float(spy.rating) > 2.5 and float(spy.rating) < 4.0:
                                print 'You\'re pretty good at ratings. Well,appreciate that'
                            elif float(spy.rating) > 4.0 and float(spy.rating) < 5.0:
                                print'Great! You\'ve got really fantastic ratings!'

                elif int(spy.age)<12:
                    print'You\'re too young to join it now '+spy.name
                elif int(spy.age)<50:
                     print 'Hey!Golden aged! Sorry you\'re not eligible to join SpyChat!'

                else:
                    print'Enter a valid age'
    else:
         print'A spy needs to have a valid name'
