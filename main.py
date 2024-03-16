from OptionPackage import voice_recorder, gif_creator, desktop_notifier,timer

def toolsMenu():
    print("1- Voice recorder")
    print("2- Gif maker")
    print("3- Notification app")
    print("4- Timer")
    print("5- Exit")

if __name__ == "__main__":
    while True:
        toolsMenu()
        userInput = input("Please select a tool or exit: ")
        if userInput == "1":
            voice_recorder.record_voice()
        elif userInput == "2":
            gif_creator.create_gif()
        elif userInput == "3":
            desktop_notifier.notify()
        elif userInput == "4":
            timer.timing()
        elif userInput == "5":
            break
        else:
            print("Invalid option!")

