import pyttsx3
import time

password_right = "shubham11"
total = 0

voice_bot = pyttsx3.init()
voices = voice_bot.getProperty('voices')
voice_bot.setProperty('voice', voices[0].id) 
voice_bot.setProperty('rate', 150) 

while True:
    val = input("Enter password or number: ")

    if val == password_right:
        print("The password is correct, WELCOME BOSS")
        voice_bot.say("Gud job welcome boss ") # voice greetings... for.. Admin..
        voice_bot.runAndWait()
        break  ## Exit.. loop if password matches...

    else:
        if val.isdigit():  
            total += int(val)
            print(f"Speaking added {val}...")
            voice_bot.say(f"added {val}")
            voice_bot.runAndWait()
        else:
            # HANDLE... wrong attempts and numbers...
            print("The password is wrong, repeat again")
            voice_bot.say("lol Wrong password repeat again, WHO ARE YOU???") # voice greetings... for.. Admin           
            voice_bot.runAndWait()
            time.sleep(0.5)
            
print("Total of numbers entered:", total)
