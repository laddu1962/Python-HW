# Tuples - Exercise 1
tupleList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new_list = [item for item in tupleList if item]
print(new_list)

# Dictionaries - Exercise 1
d=dict()
for x in range(1,21):
    d[x]=x**2
print(d)


# Dictionaries - Exercise 2
room_items = {"item1": {"Name": "Lamp", "colour": "Red"},
              "item2": {"Name": "Table", "Colour": "Brown", "Type": 0},
              "item3": {"Name": "Lamp", "Colour": "Red"},
              "item4": {"Name": "Chair", "Colour": "Green", "Type": 1}}

result = {}

for key, value in room_items.items():
    if value not in result.values():
        result[key] = value

print(result)

# Dictionaries - Exercise 3

player = {'Health': 20, 'Weapons': 0}
inventory = 0


text = """Hello minions welcome to your worst nightmare!
At Starbucks 0174! Filled with people. 
Then suddenly everyone turns into monsters"""


text3 = """"The staff room has items which can be used as weapons!
The items in the room are...."""

test4 = "chose 2 items to defend yourself"

print(text)
print(text3)

staff_room = {'broomstick': 5, 'butter Knife': 10, 'cup': 3, 'pumpkin spic latte': 30}
print(staff_room)

print(test4)

for k, val, in staff_room.itmes():
    print("You have picked up", k, "it has", val, "damage")


inventory = inventory + staff_room.pop(input())