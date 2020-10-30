import os
import time
import datetime

print("Starting Bot...")

while True:
    try:
        os.system("python bot.py")
        print('------------------ERROR----------------')
        print(f"Error occured at: {datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC')}")
        print("RESTARTING BOT...")
        print('---------------------------------------')
    except Exception as e:
        print(f"An excption occured preventing restart: {e}")
