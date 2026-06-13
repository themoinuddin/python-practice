# dictionaries.py
# Author: Moin Uddin

student = {
    "name": "Moin",
    "age": 19,
    "course": "BSCS"
}

print(student["name"])
print(student["age"])

student["age"] = 20
print(student)

student["city"] = "MirpurKhas"
print(student)

print(student.keys())
print(student.values())