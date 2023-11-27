import random

file = open("/Users/magewade/Desktop/Python/Intermediate/line.txt", "r")
content = file.readlines()
print(random.choice(content))
file.close()



file = open("/Users/magewade/Desktop/Python/Intermediate/numbers.txt", "r")
result = 0
for line in file:
    result += int(line.strip())
print(result)
file.close()


with open('/Users/magewade/Desktop/Python/Intermediate/logfile.txt', 'r') as f:
    user_time = {}

    for line in f:
        username, login_time, logout_time = line.strip().split(', ')
        if login_time and logout_time:
            login_minutes = int(login_time[:2]) * 60 + int(login_time[3:])
            logout_minutes = int(logout_time[:2]) * 60 + int(logout_time[3:])

            time_spent = logout_minutes - login_minutes

            user_time[username] = time_spent

with open('/Users/magewade/Desktop/Python/Intermediate/output.txt', 'w') as f:
    for username, time_spent in user_time.items():
        if time_spent >= 60: 
            f.write(f'{username}\n')
        

