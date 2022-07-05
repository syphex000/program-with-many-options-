import time
import pyautogui


def thegodpart(): 
    print("[1] For Single Phrase!")
    print("[2] For Multiple Phrase!")
    print("[3] autoclicker!")
    a = int(input("[?]: "))
    if a == 1:
        k = input("Enter The Word You Wand to Spam?:")
        count = int(input("How Many Times Do You Want To Spam? "))
        print("You Have 5 Seconds, Place The Mouse Cursor on The Chat Box Where You Type")
        time.sleep(5) 
        for i in range(count):
            pyautogui.typewrite(k)
            pyautogui.press("enter")
            print("Sent " + k)
        print("Spammed " + k + " " + str(count) + " times!")
    if a == 2:
        k = input("Enter The Word You Wand to Spam?:")
        delay = int(input("How much time should the app wait between the messages?:"))
        count = int(input("How Many Times Do You Want To Spam?:"))
        print("You Have 5 Seconds, Place The Mouse Cursor on The Chat Box Where You Type")
        time.sleep(5) 
        for i in range(count):
            pyautogui.typewrite(k)
            pyautogui.press("enter")
            time.sleep(delay)
            print("Sent " + k)
        print("Spammed " + k + " " + str(count) + " times!")
    if a == 3:
        delay = int(input("How much time should the app wait between the clicks?:"))
        count = int(input("How Many Times Do You Want To click?:"))
        print("You Have 5 Seconds, Place The Mouse Cursor on The Chat Box Where You Type")
        time.sleep(5)
        for i in range(count):
            pyautogui.click(button='left')
            time.sleep(delay)
thegodpart()
