class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def meau(self):
        print('meau')


Dog().walk()
Dog().bark()

Cat().walk()
Cat().meau()

