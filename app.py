Credentials: [str, str] = {
    "username": str(input("Please provide a username > ")),
    "password": str(input("Please provide a strong password: at least 8 characters long > ")),
    "status": str(input("Would you like to activate your account: y or n > "))
}


def format_credentials() -> ():
    print("* * * Credentials * * *")
    formatted_username: str = f"@{Credentials.get('username')}"
    formatted_password_length = len(Credentials.get('password'))

    placeholder: str = ""

    for i in range(0, formatted_password_length):
        placeholder += "*"

    print(placeholder)
