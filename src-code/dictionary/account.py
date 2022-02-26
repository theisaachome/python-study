from turtle import clear


account = {
    "name":"Zaw Zaw",
    "email":"zawzaw@gmail.com",
    "password":"password",
    "phone":"09250832041"
}

account["isActive"]=True;

print(account);

# account.pop("password")
# account.popitem();
# del account["password"]

# del account

account.clear()
print(account);