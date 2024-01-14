from datetime import datetime


# -------------------------------------------------------------------------------------------
    # Aufgabe 3 (xx Punkte)
    # Implementieren Sie die Eingabe eines Benutzernamens durch den Anwender.
    # Ist der Benutzername in der Liste der Benutzer vorhanden, arbeiten Sie
    # mit dem gefundenen Objekts weiter. Andernfalls geben Sie eine Fehler-
    # meldung aus. Der Benutzername entspricht der E-Mail-Adresse. (fertig)
# -------------------------------------------------------------------------------------------
def changePassword(listOfUserObjects):
    username = input("Geben Sie den Benutzernamen ein: ")
    user = None

    for userObject in listOfUserObjects:
        if userObject["e-mail"] == username:
            user = userObject
            break

    if user == None:
        print("Unbekannter Benutzer")
        return

    # -------------------------------------------------------------------------------------------
    # Aufgabe 4 (xx Punkte)
    # Der Benutzer wird nun zur Eingabe eines neuen Passworts aufgefordert.
    # Das Passwort darf nicht von einem anderen Benutzer in der Liste ver-
    # wendet werden. Wird ein doppeltes Passwort vergeben, muss ein neues
    # Passwort eingegeben werden. Die Eingabe des Passworts wiederholt sich
    # so lange, bis das neue Passwort erfolgreich gesetzt wird.
    # -------------------------------------------------------------------------------------------

    user["password"] = input("Geben Sie das neue Passwort ein: ")
    for userObject in listOfUserObjects:
        if (userObject["password"] == user["password"] and userObject["e-mail"] != user["e-mail"]):
            print("Passwort bereits vorhanden.")

            while userObject["password"] == user["password"]:
                user["password"] = input("Geben Sie das neue Passwort ein: ")


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
changePassword(listOfUserObjects)

