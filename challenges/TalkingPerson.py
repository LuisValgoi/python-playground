class TalkingPerson:
    def __init__(self, name):
        self.name = name

    def tell_me_your_name(self):
        print(f'My Name is: {self.name}')


person = TalkingPerson('Luis')
person.tell_me_your_name()
