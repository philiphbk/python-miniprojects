people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Blessing", "house": "Slytherin"}
] 

people.sort(key=lambda person: person["name"])

print (people)