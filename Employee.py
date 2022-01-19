import re

from Person import Person


class Employee(Person):

    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        hours = int(hours)
        if hours == 8:
            return "Happy"
        elif hours > 8:
            return "tired"
        else:
            return "Lazy"

    # def drive(self):

    # def refuel(self):

    def send_mail(self, to, subject, msg, From):
        f = open("Emails.txt", "a")
        emailbody = "From : " + From + "\n" + "To : " + to + "\n" + "Subject : " + subject + "\n" + msg + "\n"
        f.write(emailbody)

    @property  # print property value
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salaryy):
        if salaryy < 1000:
            print("Salary must be 1000 or more the defult value is 1000")
            self.__salary = 1000
        else:
            self.__salary = salaryy

    @property  # print property value
    def email(self):
        return self.__email

    @email.setter
    def email(self, emm):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, emm):
            self.__email = emm
        else:
            print("Wrong Email Format")




