import time
from datetime import date
import random
i = 0

while i < 5:
    wheatley = input(">" )
    if wheatley == "Hey Wheatley" or wheatley == "Hey wheatley" or wheatley == "hey wheatley":
        print("Yea Michael")
        A = input("What can I do ")
        if A == "what is the time" or A == "What is the time":
            times = (time.strftime("%H:%M:%S"))
            print("The time is " + times)

        elif A == "What is the date" or A == "what is the date":
            today = date.today()
            print(today)
        elif A == "Can you set a timer" or A == "can you set a timer":
            timer = input("Sure for how long ")
            Key_Word1 = ("hours", "hour")
            Key_Word2 = ("minutes", "minute")
            Key_Word3 = ("seconds",)
            for word in timer.split():
                if word in Key_Word1:
                    me = timer.split()
                    me1 = me[0]
                    me2 = int(me1) * 3600
                    print("Done!")
                    time.sleep(int(me2))
                if word in Key_Word2:
                    ne = timer.split()
                    ne1 = ne[0]
                    ne2 = int(ne1) * 60
                    print("Done!")
                    time.sleep(int(ne2))
                    print("Timers Up!")
                if word in Key_Word3:
                    be = timer.split()
                    be1 = be[0]
                    be2 = int(be1)
                    print("Done!")
                    time.sleep(int(be2))
                    print("Timers Up!")
                else:
                    pass
        elif A == "Can you set a reminder" or A == "can you set a reminder":
            reminder = input("Alright, for what ")
            reminder2 = input("And for what time ")
            replaced_reminder = reminder.replace('my', 'your')
            print(f"Reminder {replaced_reminder} at {reminder2} is Set!")
            remind = reminder2.split(":")
            times = (time.strftime("%H:%M:%S"))
            remindd = remind[0]
            remindd2 = remind[1]
            times1 = times.split(":")
            times2 = times1[0]
            times2_replaced = times2.replace("0", "")
            first = (int(remindd) - int(times2_replaced))
            first1 = first * 3600
            times3 = times1[1]
            if remindd2 > times3:
                minuto = (int(remindd2) - int(times3))
                final_minuto = int(minuto) * 60
                final = (int(first1) + int(final_minuto))
                time.sleep(int(final))
                print(f"Reminder {replaced_reminder} now!")
            elif remindd2 < times3:
                ninuto = (60 - int(times3))
                ninuto2 = (int(ninuto) + int(remindd2))
                ninuto3 = (int(ninuto) * 60)
                final_ninuto = int(ninuto3) + int(first1)
                time.sleep(final_ninuto)
                print(f"Reminder {replaced_reminder} now!")
        elif A == "I want to play a game" or A == "I wanna play a game":
            num = (random.randint(0, 1000))
            print("Alright, here is a game!")
            time.sleep(1)
            print("This is a guessing game, you will have 10 tries to guess the number it picks from 1-1,000")
            print("ready")
            i = 0
            while i < 10:
                guess = input("Guess: ")
                if guess == str(num):
                    print("Good Job, You Won!")
                    quit()
                elif guess < str(num):
                    print("Number is bigger")
                elif guess > str(num):
                    print("Number is smaller")
                i = i + 1
            print(f"Sorry you lost, the number was {num}")
        elif A == "I need help" or A == "Can you help me" or A == "can you help me":
            wheatls = input("With what? ")
            numb = (random.randint(1, 2))
            if numb != 1:
                print("I think")
                time.sleep(1)
                print("Yes")
            if numb != 2:
                print("I think")
                time.sleep(1)
                print("No")
#Hi



























    elif wheatley == "Bye wheatley":
        print("Bye Michael")
        exit()



