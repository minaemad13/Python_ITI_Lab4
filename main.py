from Employee import Employee

a=Employee("Mina",100,"happy",700,1,"fiat","mena@emad.com",101000,2000)
a1=Employee("Mina",100,"happy",100,1,"fiat","menmad.com",1000,2000)
a2=Employee("Mina",100,"happy",100,1,"fiat","menm@ad.com",500,2000)
right_emp=Employee("Mina",100,"happy",100,1,"fiat","menm@ad.com",1000,2000)

print(right_emp.buy(5))
print(right_emp.eat(3))
print(right_emp.sleep(10))
print(right_emp.work(10))
right_emp.send_mail("mena@gmail.com","test","Hello Test","menaemad@gmail.com")

