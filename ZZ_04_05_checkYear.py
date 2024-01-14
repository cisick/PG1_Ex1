from datetime import datetime


# -------------------------------------------------------------------------------------------
    # Aufgabe 4:
    # Erstellen Sie eine Funktion checkYear mit dem Parameter listOfUserObjects.
    # Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten. (fertig)
    # Aufgabe 5:
    # Implementieren Sie nun die Funktion für die Aufgabe 4. Alle Benutzer seit dem
    # Jahr 2022 ihr Kennwort nicht geändert haben, werden deaktiviert, in dem der Key valid
    # den Value False erhält. (fertig)
# -------------------------------------------------------------------------------------------
def checkYear(listOfUserObjects):
    # zu 5)
    for userObject in listOfUserObjects:
        if "passwordChanged" in userObject:
            password_changed_year = userObject["passwordChanged"].year
            if password_changed_year < 2022:
                userObject["valid"] = False

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
checkYear(userList)

print("Viel Erfolg!")