#Q1
foods = ["Orange", "Apple", "Banana", "Strawberry", "Grape", "Blueberry", ["Carrot", "Cauliflower", "Pumpkin"], "Passionfruit", "Mango", "Kiwifruit"]
print(foods[0])
print(foods[2])
print(foods[9])
print(foods[0:3])
print(foods[7:10])
print(foods[6][2])

#Q2
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for item, subitem in mailing_list:
    print(f"{item}: {subitem}")

#Q3
names = []
while len(names) < 3:
        name = input("Enter a name: ")
        names.append(name)
for item in names:
    print(f"{item}") 

#Q4
letters = []
wordlist = []
user_string = input("Enter a string:")
wordlist.extend(user_string.split())
print(len(wordlist))
print(wordlist)
for item in wordlist:
        letters.extend(item)

print(len(letters))
print(letters)

