from datetime import datetime

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = True
        self.chats = []
        self.current_status_messages = None


# one default spy details
spy = Spy('Aditi', 'Mr.', 22, 4.7)

friend_one = Spy('Qadir', 'Mr', 23,4.3)
friend_two = Spy('Monika', 'Miss', 19,3.5)
friend_three = Spy('Rashika', 'Miss', 29,4.5)
friends = [friend_one, friend_two, friend_three]


class Chat:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me