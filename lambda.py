people = [
    {"name":"Harry","house":"Gryddinfor"},
    {"name":"Cho","house":"Ravenclaw"},
    {"name":"Draco","house":"Slytherin"}
]

# def f(person):
#     return person["name"]
# people.sort(key=f)
# print(people)

#Optimized
def f(person):
     return person["name"]
people.sort(key=lambda person: person["name"])
print(people)