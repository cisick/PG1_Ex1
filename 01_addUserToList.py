# -------------------------------------------------------------------------------------------
# Aufgabe 1 (x Punkte)
# Erstellen Sie eine Funktion printUserObject mit dem Parameter userObject.
# Der Parameter enthält ein dict, welches in der Funktion addUserToList
# definiert wurde.
# Geben Sie alle Keys und Values des dicts in folgender Darstellung aus:
# Vorname: Lord
# Nachname: Kelvin
# ...
# Den Geburtstag des Users geben Sie im folgenden Format aus: yyyy-mm-dd (fertig)
# -------------------------------------------------------------------------------------------
from datetime import datetime


def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["prename"] = input("Vorname: ")
    userObject["lastname"] = input("Nachname: ")
    userObject["e-mail"] = input("E-Mail: ")
    userObject["password"] = input("Password: ")
    userObject["valid"] = True
    userObject["birthday"] = None

    listOfUserObjects.append(userObject)

# Main-File
# In diesem Bereich nichts ändern!
listOfUserObjects = list() # []

userObject = dict()  # {}
userObject["prename"] = "Hans"
userObject["lastname"] = "Peter"
userObject["e-mail"] = "hans@peter.org"
userObject["password"] = "SehrSicher"
userObject["valid"] = True
userObject["birthday"] = datetime(2023, 12, 24)

listOfUserObjects.append(userObject)

userObject = dict()  # {}
userObject["prename"] = "Franz"
userObject["lastname"] = "Meyer"
userObject["e-mail"] = "franzi@web.de"
userObject["password"] = "aefew!"
userObject["valid"] = True
userObject["birthday"] = datetime(2000, 10, 2)

listOfUserObjects.append(userObject)

# Ab hier können Sie Ihr Programm testen
