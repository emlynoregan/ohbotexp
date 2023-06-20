# import the ohbot module
import platform

print ("Python version: " + platform.python_version())
print ("Platform: " + platform.system())

from ohbot import ohbot

# Reset Ohbot

print ("Resetting Ohbot")
ohbot.reset()

def ohbot_main():
    # Get user input, then send it to ohbot, in a loop.
    user_input = input("Ohbot says: ").lower()

    try:
        while user_input != "exit":
            if "satan" in user_input:
                eyes_red()
            else:
                eyes_white()

            ohbot.say(user_input)

            if user_input == "reset":
                ohbot.reset()
            if user_input in ["yes", "ok", "yeah", "yep", "true"]:
                nod()
            elif user_input in ["no", "nope", "nah", "false"]:
                shake()

            user_input = input("Ohbot says: ").lower()
    finally:
        ohbot.reset()
        ohbot.close()

def eyes_red():
    ohbot.setEyeColour(0,10,0)

def eyes_white():
    ohbot.setEyeColour(10,10,10)

def nod():
    ohbot.move(0,10)
    ohbot.wait(0.5)
    ohbot.move(0,0)
    # now back to centre
    ohbot.wait(0.5)
    ohbot.move(0,5)

def shake():
    ohbot.move(1,10)
    ohbot.wait(0.5)
    ohbot.move(1,0)
    ohbot.wait(0.5)
    ohbot.move(1,10)
    # now back to centre
    ohbot.wait(0.5)
    ohbot.move(1,5)

if __name__ == "__main__":
    ohbot_main()

# # Move turn ohbot's head and eyes. 
# print ("Moving Ohbot")
# ohbot.move(1,2)
# ohbot.move(3,1)

# # Wait a few seconds for the motors to move

# ohbot.wait(2)

# # Move head back to the centre and say "Hello World"
# ohbot.move(1,5,1)
# ohbot.say("Hello World")

# # Slowly increase the brightness of the eyes.

# for x in range(0,10):

#     ohbot.setEyeColour(x,x,x)
#     ohbot.wait(0.1)

#     ohbot.setEyeColour(0,0,0)
#     ohbot.wait(0.2)

    

# ohbot.move(1,5,1)
# ohbot.wait(1)

# ohbot.say("Now I am running in python you know",False)

# for x in range (0,10):
#     ohbot.move(3,x)
#     ohbot.setEyeColour(x,10-x,x)
#     ohbot.wait(0.3)

# ohbot.say("I can do the robot")


# for y in range(0,4):
#     for x in range(0,10):
#         ohbot.move(y,x)
#         ohbot.setEyeColour(y,x,10-x)
#         ohbot.wait(0.2)
        
# ohbot.reset()      
# ohbot.say("and ventriloquism",True,False)
# ohbot.setEyeColour(0,0,10)
# ohbot.wait(1)

# # close ohbot at the end.

# ohbot.close()