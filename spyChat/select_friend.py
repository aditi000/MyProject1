from globals import friends
def select_friend():
    counter=1

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % ( counter, friend['name'], friend['age'],friend['rating'])
        counter= counter+ 1
    #asking user to select a friend
    user_input= raw_input("Choose from your friends Lists")
    if user_input>=counter:
        return int(user_input)
    else:
        print'Invalid Choice. Try again'
        exit(-1)