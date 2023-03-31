command =""
while True:
    command=input("> ").lower()
    if command == "start" :
        print("Car Started... Ready to go")
    elif command == "stop" :
        print("Car Stopped")
    elif command == "help" :
        print('''
        start-> to start the car
        stop-> to stop the car
        quit-> to quit from game
        ''')
    elif command == "quit":
        break
    else :
        print("Sorry I don't Understand...what you have written")
