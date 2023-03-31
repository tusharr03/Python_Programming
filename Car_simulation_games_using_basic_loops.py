command =""
is_started=False
while True:
    command=input("> ").lower()
    if command == "start" :
        if is_started == True:
            print("Car is already started.")
        else :
            is_started=True
            print("Car Started... Ready to go")
    elif command == "stop" :
        if not is_started == True:
            print("Car is already stopped")
        else :    
            is_started=False
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
