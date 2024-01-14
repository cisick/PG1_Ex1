# -------------------------------------------------------------------------------------------
# Aufgabe 1 (x Punkte)
# Erstellen Sie eine Funktion printUserObject mit dem Parameter userObject.
# Der Parameter enthält ein dict, welches in der Funktion addUserToList
# definiert wurde.
# Geben Sie alle Keys und Values des dicts in folgender Darstellung aus:
# Vorname: Lord
# Nachname: Kelvin
# -------------------------------------------------------------------------------------------
from datetime import datetime


def print_user_object(user_object):
    # Variante 1
    print("-----------------------------------------------")
    print("Ausgabe der 1. Variante: ")
    print("Vorname:", user_object["prename"])
    print("Nachname:", user_object["lastname"])
    print("E-mail:", user_object["e-mail"])
    print("Password:", user_object["password"])
    date = user_object["birthday"]
    date_as_string = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    print("Geburtstag", date_as_string)

    # Variante 2
    print("-----------------------------------------------")
    print("Ausgabe der 2. Variante: ")
    for key in user_object.keys():
        print(key + ":", user_object[key])


# Main-File
# In diesem Bereich nichts ändern!
list_of_user_objects = list() # []

userObject = dict()  # {}
userObject["prename"] = "Hans"
userObject["lastname"] = "Peter"
userObject["e-mail"] = "hans@peter.org"
userObject["password"] = "SehrSicher"
userObject["valid"] = True
userObject["birthday"] = datetime(2023, 12, 24)

list_of_user_objects.append(userObject)

userObject = dict()  # {}
userObject["prename"] = "Franz"
userObject["lastname"] = "Meyer"
userObject["e-mail"] = "franzi@web.de"
userObject["password"] = "aefew!"
userObject["valid"] = True
userObject["birthday"] = datetime(2000, 10, 2)

list_of_user_objects.append(userObject)

# Ab hier können Sie Ihr Programm testen

print_user_object(list_of_user_objects[0])
print_user_object(list_of_user_objects[1])

