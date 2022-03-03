def greet():
    print("Hello from function block");

greet()

def sayHi(name):
    print("Hi ",name);

sayHi("Isaac Home");


def showColors (*colors):
    print("My Favourite Color is : ",colors[2]);

showColors("red","Green","black")


def showEmployeeInfo(name,address, email):
    print("**** Employee Information ****")
    print("Name " + name + "\nAddress : " + address + "\nEmail : " + email);

showEmployeeInfo(name="Isaachome",address="Yangon",email="isaachome@example.com");


def showStatus(status="Offline"):
    print("She is " + status );

showStatus(status="Online");
showStatus();