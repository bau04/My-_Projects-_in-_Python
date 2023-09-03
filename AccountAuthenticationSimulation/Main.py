# Account Authentication Simulation
# Use only 1 for loop

# INDEX        0       1          2
userName = ["Marc", "Hanni", "Julius"]
passWord = ["Marc123", "Pham123", "Caesar123"]

currUserName = input("Enter your username: ")
currPassWord = input("Enter your password: ")

for x in range(len(userName)):  # Access the username and password using the same index "x"
    if currUserName == userName[x] and currPassWord == passWord[x]:  # input should match username and password
        print("Welcome", userName[x] + "!")
        break
else:
    print("Account Not Found")
