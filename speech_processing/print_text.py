import pyautogui
import time

def write_text(text):
    # for testing, print to console
    testing = False

    if(testing):
        print(text)
    else:
        write_to_gui(text)


    

def write_to_gui(sentence):
    print("auto_gui called")
    # Set the position where you want to start typing
    start_x, start_y = 1208, 791

    # Split the sentence into words
    words = sentence.split()

    # Move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y)


    # Loop through each word
    for word in words:
        # Type the word
        pyautogui.typewrite(word, interval=0.05)  # Adjust interval as needed

        # Press Enter
        pyautogui.press("enter")

        # Wait for a short while (you can adjust the duration)
        time.sleep(0.1)


