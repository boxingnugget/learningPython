###count to 10 exercise
###ask for user and pass, implement a lock, use user and pass to unlock

username = str(input("Username: "))
password = str(input("Password: "))
input1 = None
input2 = None
command = None

while command != "lock":
    command = str(input("would you like to lock?: "))
while input1 != username:
    input1 = str(input("type username: "))
while input2 != password:
    input2 = str(input("tyoe password: "))
print("unlocked")