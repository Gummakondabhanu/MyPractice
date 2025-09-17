import re
def is_valid_email(email):
    pattern=r'^[\w\.]+@[a-z]+\.[a-z]{2,4}$'
    return re.match(pattern,email) is not None
emails = ["test@example.com", "user.name@domain.co.in",
          "wrong-email@", "another@domain", "abc@123"]
for e in emails:
    print(f"{e}-> {'Valid' if is_valid_email(e) else 'Invalid'}")