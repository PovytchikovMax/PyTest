class Human:
    def __init__(self, name, sex, age):
        self._name = name
        self.__sex = sex
        self._age = age

    def sayHello(self):
        print(f'Hello from {self._name} , i am {self._age} ears old!!')

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


human1 = Human("Max", 'male', 34)
print(human1.get_sex())
human1.sayHello()

human1.set_name('Alex')
print(human1.get_name())

print(human1.get_sex())

human1.set_sex('fmale')
print(human1.get_sex())
