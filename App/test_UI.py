import json

def encryption_decryption_program():
    print("Welcome to encryption and decryption program")
    print("press 1 for checking data")
    print("press 2 to change the data")
    print("press 3 to generate a key")
    print("press 4 to send a message")
    print("press 5 to exit")

    while True:
        value = input("What do you want to do: ")

        if value == "1":
            display_data()
        elif value == "2":
            change_data()
        elif value == "3":
            generate_key()
        elif value == "4":
            send_message()
        elif value == "5":
            break
        else:
            print("Invalid operation. Please try again.")

def display_data():
    print("Display data:")
    with open("App\config.json", "r") as f:
        config = json.loads(f.read())
        for key, value in config.items():
            print(f'"{key}" = {value}')

def change_data():
    # Implement functionality to change data
    pass

def generate_key():
    # Implement key generation logic
    print("Generated Key Success")

def send_message():
    data = input("Message: ")
    # Implement encryption and sending logic

if __name__ == "__main__":
    encryption_decryption_program()


