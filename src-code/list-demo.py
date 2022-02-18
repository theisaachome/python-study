task = ["Wake up 5 am","Do Cardio","Shower","Breakfast"];

students =["Aung Aunng","Zaw Zaw","Maw Maw","Thaw Thaw"];

myList = list(("Item 1","Item 2","Itemm 3"));


newList = students[1:3];


# in the keyword

search="James"
employee = ["John","James","Mark","Luke"];
if search in employee:
    print(employee[employee.index(search)] + " is here in the office today.");
else:
    print("Sorry  He is not here.");


# change the second item
emails=["aung@email.com","zaw@gmail.com","naw@gmail.com"];
# print(emails);
emails[0]="aung@gmail.com";
# print(emails);


# 
toBuyItems=["apple", "banana", "cherry", "orange", "kiwi", "mango"];
toBuyItems[1:3]=["blackcurrant","watermelon"];
# print(toBuyItems);

# add item to the end of the list

emails.append("new@gmail.com");
# print(emails);

# insert method

toBuyItems.insert(30,"New Item ");
print(toBuyItems);