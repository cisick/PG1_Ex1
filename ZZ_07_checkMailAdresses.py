from datetime import datetime


# -------------------------------------------------------------------------------------------
    # Aufgabe 7:
    # Prüfen Sie, mittels der Funktion checkMailAdresses(), ob doppelte E-Mail-Adressen vorliegen.
# -------------------------------------------------------------------------------------------
def checkMailAdresses(listOfUserObjects):
    counter = 1

    for userObject in listOfUserObjects:
        for i in range(counter, len(listOfUserObjects), 1):
            if userObject["e-mail"] == listOfUserObjects[i]["e-mail"]:
                print("Diese E-Mail ist doppelt:", userObject["e-mail"])

        counter += 1

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

checkMailAdresses(userList)

print("Viel Erfolg!")