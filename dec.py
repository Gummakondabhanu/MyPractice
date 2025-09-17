user_authenticated = True
def authenticate(func):
    def wrapper():
        if user_authenticated:
            func()
        else:
            print("Access Denied!")
    return wrapper
@authenticate
def deposit():
    print("Depositing money...")
@authenticate
def withdraw():
    print("Withdrawing money...")
deposit()
withdraw()
user_authenticated = True
deposit()   # Output: Depositing money...
withdraw()  # Output: Withdrawing money...
