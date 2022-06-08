class Vulnerability:

    vulnerabilities = {}

    def __init__(self, name, description, rang=0):
        self.name = name
        self.description = description
        self.rang = rang
        self.write()

    def __str__(self):
        return f"{self.name} | {self.description}"

    def write(self):
        self.vulnerabilities[self.name] = {'description': self.description, 'rang': self.rang}

    def comparison(self, name):
        try:
            another_vulnerability = self.vulnerabilities.get(name)
            if self.rang > another_vulnerability.get('rang'):
                print(self.name, 'больше!')
            elif self.rang < another_vulnerability.get('rang'):
                print(name, 'больше!')
            else:
                print(f'{self.name} и {name} равны!')
        except AttributeError:
            print(f'Нет такого имени - {name}, вы можете использовать метод show_all()')

    def show_all(self):
        for key, value in self.vulnerabilities.items():
            print(f'Название: {key} | Описание: {value.get("description")} | Ранг: {value.get("rang")}')

    def up_rang(self, num):
        self.rang += num
        self.vulnerabilities[self.name]['rang'] += num

    def down_rang(self, num):
        self.rang -= num
        self.vulnerabilities[self.name]['rang'] -= num


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
broken_access_control.show_all()
broken_access_control.comparison("Cryptographic Failures")
cryptographic_failures.up_rang(2)
cryptographic_failures.comparison("Broken Access Control")
cryptographic_failures.up_rang(1)
broken_access_control.comparison("Cryptographic Failures")
insecure_design.comparison("Broken Access Control")
broken_access_control.down_rang(4)
insecure_design.comparison("Broken Access Control")
insecure_design.comparison("Несуществующее имя")
print(insecure_design)