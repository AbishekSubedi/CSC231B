####################################################
## Class declarations                             ##
####################################################


class Person:
    def __init__(self, name, SSN):
        self.name = name
        self.ssn = SSN

    def sayHi(self):
        print(self.name + ' says "Hi!"')

    def saySSN(self):
        print(self.name + ' says "My SSN is ' + str(self.ssn) + '!"')


class SSN:
    def __init__(self, area_num, group_num, serial_num):
        self.area = area_num
        self.group = group_num
        self.serial = serial_num

    # def __int__(self):
    # return
    def __str__(self):
        string = f"{self.area}-{self.group}-{self.serial}"
        return string


####################################################
## Script starts                                  ##
####################################################

# person = [0, 1, 2]
# person[0] = Person("Tena Laudine", SSN(123, 45, 6789))

# person[1] = Person("Aleš Hira", SSN(321, 54, 1221))

# person[2] = Person("Zorka Maisie", SSN(555, 00, 100))

person = []
person.append(Person("Tena Laudine", SSN(123, 45, 6789)))
person.append(Person("Aleš Hira", SSN(321, 54, 1221)))
person.append(Person("Zorka Maisie", SSN(555, 00, 100)))

# person[0].sayHi()
# person[1].sayHi()
# person[2].sayHi()

# for i in range(len(person)):
#     person[i].sayHi()

for p in person:
    p.sayHi()

person[0].saySSN()
