import json
print("Welcome to encrytion and decrytion program")
print("press 1 for checking data")
print("press 2 to change the data")
print("press 3 to generate a key")
print("press 4 to send a message")

value = input("What do you want to do: ")

if value == "1":
    print("Display data:")
    with open("App\config.json", "r") as f:
        config = json.loads(f.read())
        print('"n" = '+config["n"])
        print('"e" = '+config["e"])
        print('"d" = '+config["d"])
        print('"dest_IP" = '+config["dest_IP"])
        print('"dest_PORT" = '+config["dest_PORT"])
        print('"my_IP" = '+config["my_IP"])
elif value == "2":
    with open("App\config.json", "r") as f:
        config = json.loads(f.read())
        
elif value == "3":
    ##generate key for encrypt
    print("Generated Key Success")
elif value == "4":
    data = input("Message: ")
    ##encrypt data and send to another user
else:
    print("There is no operation in that number pls try again")
