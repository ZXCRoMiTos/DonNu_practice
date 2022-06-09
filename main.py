class Vulnerability:

    vulnerabilities = {}

    def __init__(self, name, description, rang=0):
        self.name = name
        self.description = description
        self.rang = rang
        self.vulnerabilities[name] = {'description': description, 'rang': rang}

    def __str__(self):
        return f"{self.name} | {self.description}"

    def compare_with(self, *args):
        result = f'Сравнение {self.name}: \n'
        list_vulnerabilities = list(self.vulnerabilities)
        for item in args:
            try:
                if isinstance(item, int):
                    num = item - 1
                    name = list_vulnerabilities[num]
                else:
                    name = item
                try:
                    row = f'  c {name} -'
                    another_vulnerability = self.vulnerabilities.get(name)
                    difference = self.rang - another_vulnerability.get('rang')
                    if difference > 0:
                        row += ' менее опасно \n'
                    elif difference < 0:
                        row += ' более опасно \n'
                    else:
                        row += ' равны по опасности \n'
                    result += row
                except AttributeError:
                    result += f'  Нет уязвимости с именем - {name}, вы можете использовать метод show_all() \n'
            except IndexError:
                result += f'  Нет уязвимсоти с id - {item}, вы можете использовать метод show_all() \n'
        print(result)

    def show_all(self):
        num = 1
        for key, value in self.vulnerabilities.items():
            print(f'{num} | Название: {key} | Описание: {value.get("description")} | Ранг: {value.get("rang")}')
            num += 1
        print()

    def up_rang(self, num):
        self.rang += num
        self.vulnerabilities[self.name]['rang'] += num

    def down_rang(self, num):
        self.rang -= num
        self.vulnerabilities[self.name]['rang'] -= num

    @staticmethod
    def help():
        print('Методы: \n  ~ show_all() - показывает все доступные уязвимости их id, название, описание и ранг \n '
              ' ~ compare_with() - принимает на вход названия уязвимостей или их id через запятую, возвращает '
              'результат сравнения \n  ~ up_rang() - принимает на вход целое число и повышает ранг на указанное '
              'количество \n  ~ down_rang() - принимает на вход целове число и понижает ранг на указанное количество \n')


broken_access_control = Vulnerability("Broken Access Control", "Access control enforces policy such that users cannot "
                                                               "act outside of their intended permissions. Failures "
                                                               "typically lead to unauthorized information disclosure, "
                                                               "modification, or destruction of all data or performing "
                                                               "a business function outside the user's limits.", rang=5)
cryptographic_failures = Vulnerability("Cryptographic Failures", "The first thing is to determine the protection needs "
                                                                 "of data in transit and at rest. For example, "
                                                                 "passwords, credit card numbers, health records, "
                                                                 "personal information, and business secrets require "
                                                                 " protection, mainly if that data falls under privacy "
                                                                 "laws, e.g., EU's General Data Protection Regulation "
                                                                 "(GDPR), or regulations, e.g., financial data "
                                                                 "protection such as PCI Data Security Standard "
                                                                 "(PCI DSS).", rang=3)
insecure_design = Vulnerability("Insecure Design", "Insecure design is a broad category representing different "
                                                   "weaknesses, expressed as “missing or ineffective control design.” "
                                                   "Insecure design is not the source for all other Top 10 risk "
                                                   "categories. There is a difference between insecure design and "
                                                   "insecure implementation. We differentiate between design flaws "
                                                   "and implementation defects for a reason, they have different root "
                                                   "causes and remediation. A secure design can still have "
                                                   "implementation defects leading to vulnerabilities that may be "
                                                   "exploited. An insecure design cannot be fixed by a perfect "
                                                   "implementation as by definition, needed security controls were "
                                                   "never created to defend against specific attacks. One of the "
                                                   "factors that contribute to insecure design is the lack of business "
                                                   "risk profiling inherent in the software or system being developed, "
                                                   "and thus the failure to determine what level of security design "
                                                   "is required.", rang=1)

broken_access_control.help()
broken_access_control.show_all()

broken_access_control.compare_with("Cryptographic Failures", "Insecure Design")
broken_access_control.compare_with(2, 3)

broken_access_control.compare_with("test1", "test2")
broken_access_control.compare_with(4, 6)

cryptographic_failures.up_rang(2)
insecure_design.up_rang(5)
broken_access_control.compare_with(2, 3)

cryptographic_failures.compare_with(1, 3)
