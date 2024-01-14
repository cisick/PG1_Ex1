# -------------------------------------------------------------------------------------------
    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList? (fertig)
        # Ein Dictionary?
    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss. (fertig)
    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit. (fertig)
# -------------------------------------------------------------------------------------------
from datetime import datetime

def addUserToList(listOfUserObjects):
    userObject = dict() # {}
    # zu 2)
    userObject["username"] = input("Bitte geben Sie den Benutzernahmen ein: ")
    userObject["password"] = input("Bitte geben Sie das Password ein: ")
    userObject["valid"] = True
    # zu 3)
    userObject["passwordChanged"] = datetime.now()
    userObject["e-mail"] = "lord@kelvin.org"

    listOfUserObjects.append(userObject)

# -------------------------------------------------------------------------------------------
    # In dem folgenden Bereich nehmen Sie keine Änderungen vor!
    # Testdaten:
# -------------------------------------------------------------------------------------------
userList = list()

user = dict()
user["username"] = "peter.meyer"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "jule@meyer.de"

userList.append(user)

user = dict()
user["username"] = "franz.huber"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "hubi@gmx.de"

userList.append(user)

user = dict()
user["username"] = "julia.meyer"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "jule@meyer.de"

userList.append(user)

user = dict()
user["username"] = "otto.schulze"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "otto@schulze.de"

userList.append(user)

user = dict()
user["username"] = "gerd.mueller"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "otto@schulze.de"

userList.append(user)

user = dict()
user["username"] = "lui.hansel"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "lui@hansel.de"

userList.append(user)

# -------------------------------------------------------------------------------------------
    # Ab hier können Sie Ihre Lösungen testen:
# -------------------------------------------------------------------------------------------

print("Viel Erfolg!")