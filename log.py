def log():
    logs = [
         """User1 logged in,
         User2 failed login,
         User3 uploaded a file,
         User4 logged out,
         User5 updated profile"""
    ]
    for i in logs:
        yield i
log_generator = log()
for i in log_generator:
    print(i)