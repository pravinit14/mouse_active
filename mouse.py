import pyautogui
import time
import datetime

pyautogui.FAILSAFE = False
idle_threshold_seconds = 60
idle_start_time = time.time()
user = "Jack"
dispFlg = True


# Function to get current cursor position
def get_cursor_position():
    return pyautogui.position()

def checkCursorIdle(previous_position,idle_start_time):
    global dispFlg
    current_position = get_cursor_position()
     # Check if cursor position has changed
    if current_position != previous_position:
        # Cursor moved, reset idle start time and update previous position
        idle_start_time = time.time()
        previous_position = current_position
        # print(idle_start_time)
    else:
        # Cursor hasn't moved
        idle_duration = time.time() - idle_start_time
        # print(idle_duration)
        # Check if idle duration exceeds threshold
        if idle_duration >= idle_threshold_seconds:
            if(dispFlg):
                print(user+f" you look tired. Let me work for you while you are away.")
                dispFlg = False
            print(f"{idle_duration:.2f} + seconds.")
            return True



try:

    while True:
        d = datetime.datetime.now()
        
        if(d.hour >= 21):
            print(user+" its too late am going to sleep. Good Night")
            break
        
        #print(d.hour)
        if(d.hour not in range(12, 13)):
            previous_position = get_cursor_position()
            time.sleep(30)

            if(checkCursorIdle(previous_position,idle_start_time)):
                for i in range (0,100):
                    pyautogui.moveTo(0,i*5)
                    x, y = get_cursor_position()
                    # print(x,y)
                    if x != 0:
                        print(user+" you are back already. Lets get back to work.")
                        dispFlg = True
                        break
                
                for i in range(0,3):
                    pyautogui.press('shift')

except KeyboardInterrupt:
    print ('\n')

