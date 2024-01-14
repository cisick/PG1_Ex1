from datetime import datetime


# -------------------------------------------------------------------------------------------
    # Aufgabe 2 (xx Punkten)
    # Implementieren Sie die Rückgabe aller aktiven Benutzer als Liste von Strings.
    # Jeder String hat dabei das Format "Nachname, Vorname".
    # Ein Benutzer ist dann Aktiv, wenn der Value zum Key "valid" True ist. (fertig)
# -------------------------------------------------------------------------------------------
def check_valid_users(list_of_user_objects):
    valid_users = list()
    for user_object in list_of_user_objects:
        if user_object["valid"]: # oder if item["valid"] == True:
            valid_users.append(user_object["lastname"] + ", " + user_object["prename"])
    return valid_users


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

valid_user_list = check_valid_users(list_of_user_objects)

for username in valid_user_list:
    print(username)

