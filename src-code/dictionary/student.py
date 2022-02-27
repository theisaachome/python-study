

student = {
    "name":'Thaw Thaw',
    "year":2022,
    "isScholarship":False,
    "studies":["Social Science","Communications","Business"]
}
year = student['year'];
print("She is studing in ",year);
name = student.get("name");
print("Name : ",name);

keys = student.keys();
print(keys);

student.update({"major":"Law"})

print(student);