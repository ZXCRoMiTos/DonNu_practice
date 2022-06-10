class Vulnerability:

    def __init__(self):
        self.description = input('Напишите описание: ')
        self.rang = 0

    def set_rang(self, num):
        self.rang = num

    def up_rang(self, num=1):
        self.rang += num

    def down_rang(self, num=1):
        self.rang -= num

    def compare_with(self, other):
        difference = self.rang - other.rang
        if difference > 0:
            print('опаснее')
        elif difference < 0:
            print('безопастнее')
        else:
            print('равны')

    def __str__(self):
        print(self.description)


broken_access_control = Vulnerability()
broken_access_control.set_rang(5)

cryptographic_failures = Vulnerability()
cryptographic_failures.set_rang(4)

broken_access_control.compare_with(cryptographic_failures)
cryptographic_failures.up_rang()
cryptographic_failures.compare_with(broken_access_control)
