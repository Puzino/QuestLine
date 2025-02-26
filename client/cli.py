from decouple import config

from auth import register

AUTH_CONFIG_NAME = config("AUTH_CONFIG_NAME")


def auth_menu():
    print("Choice what you want:\n1. Register\n2. Login")
    choice: int = int(input("Your choice?: "))
    match choice:
        case 1:
            print("Registration.")
            try:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                status = register(username, password)
                print(status)
                return
            except Exception as ex:
                print(ex)
        case 2:
            pass
        case _:
            print("Unknown choice!")


def main() -> None:
    print("Hello!\nAnd welcome to Console RPG!\n")
    while True:
        auth_menu()


if __name__ == "__main__":
    main()
