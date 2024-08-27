
userrr = "user_1"
platform = "Google"


user_pick = input("Choose a user (There's just one): ")

if user_pick == userrr:

    platform_pick = input("Choose a platform which you want to know the password of (Google or Yahoo): ")

    # Prüfe die Plattform und gib das Passwort aus
    if platform_pick.lower() == "google":
        print("Username: Google_User1\nPassword: 1234")
    elif platform_pick.lower() == "yahoo":
        print("Username: Yahoo_User1\nPassword: 5678")
    else:
        print("Sorry, we do not have information for that platform.")
else:
    print("Sorry, I don't know that user.")

print("Thank you for using one of my first programs!")
input("Press any key to close...")
