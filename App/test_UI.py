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
            print("1: 'n'")
            print("2: 'e'")
            print("3: 'd'")
            print("4: 'dest_IP'")
            print("5: 'dest_PORT'")
            print("6: 'my_IP'")
            print("7: Exit")

            while True:
                keyChange = input("Please select key to change: ")
                if keyChange == "1":
                    change_data("n")
                elif keyChange == "2":
                    change_data("e")
                elif keyChange == "3":
                    change_data("d")
                elif keyChange == "4":
                    change_data("dest_IP")
                elif keyChange == "5":
                    change_data("dest_PORT")
                elif keyChange == "6":
                    change_data("my_IP")
                elif keyChange == "7":
                    break
                else:
                    print("Invalid operation. Please try again.")
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

def change_data(key):
    with open("App\config.json", "r") as f:
        config = json.loads(f.read())
            
        new_value = input(f"Enter the new value for {key}: ")
        try:
            config[key] = json.loads(new_value)  # Attempt to parse as JSON if applicable
        except json.JSONDecodeError:
            config[key] = new_value
        except ValueError:
            print("Invalid input. Please enter a valid value.")
    with open("App\config.json", "w") as f:
        json.dump(config, f, indent=4)  # Write back to file with indentation

    print("Data changed successfully!")

def generate_key():
    # Implement key generation logic
    print("Generated Key Success")

def send_message():
    data = input("Message: ")
    # Implement encryption and sending logic

if __name__ == "__main__":
    encryption_decryption_program()


