from datetime import datetime


# -------------------------------------------------------------------------------------------
    # Aufgabe 6:
    # Erstellen Sie eine Funktion setValid mit dem Parameter listOfUserObjects.
    # Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten.(fertig)
    # Gehen Sie alle Benutzer der Liste des Parameter durch. Jeder Benutzer, welcher
    # deaktivert wurde (siehe Aufgabe 5) erhält ein neues Passwort. Das Passwort gibt der
    # Anwender über einen input ein. Zudem wird der Value für den valid-Key auf True gesetzt. (Fertig)
# -------------------------------------------------------------------------------------------
def setValid(listOfUserObjects):
    for userObject in listOfUserObjects:
        if "valid" in userObject:
            if userObject["valid"] == False:
                userObject["password"] = input("Geben Sie ein neues Password ein: ")
                userObject["valid"] = True

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