birthdays_dictionary = {
    "Aleksandar" : "01/01/2000",
    "Sanja" : "02/02/2000",
    "Marija" : "03/03/2000",
    "Ana" : "04/04/2000"
}

print("Dobredojdovte do recniot za rodendeni. Nie gi znaeme rodendenite na: ")
print("\n".join(birthdays_dictionary.keys()))
print("Koj rodenden e potrebno da se prebara?")
name_search = input()
name_birthday = birthdays_dictionary[name_search]

print(f"Rodendenot na {name_search} e na {name_birthday}")
