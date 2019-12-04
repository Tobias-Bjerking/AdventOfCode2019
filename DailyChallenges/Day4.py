import GetInput


def check_password(password: int) -> bool:
    double = False
    ascending = True
    password = str(password)
    for x in range(1,6):
        if int(password[x]) < int(password[x-1]):
            ascending = False
        if str(password).count(password[x]) == 2:
            double = True
    return double and ascending


passwords = GetInput.get_numbered_line("../Input/Day4.txt", "-")
acceptable_passwords = []
for iter in range (passwords[1]-passwords[0]):
    if check_password(passwords[0] + iter):
        acceptable_passwords.append(passwords[0] + iter)
print(len(acceptable_passwords))