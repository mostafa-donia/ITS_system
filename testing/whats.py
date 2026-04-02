from pygetwindow import getAllTitles, getAllWindows, getActiveWindow
from subprocess import Popen
from time import sleep
from pyautogui import hotkey,press,write
from pyperclip import paste,copy


def whatsupp_ready():
    chrome_windows = [w for w in getAllWindows() if "Chrome" in w.title]
    if not chrome_windows:
        print("here is 11")
        print("No Chrome windows found.")
        Popen("start chrome https://web.whatsapp.com", shell=True)
        for _ in range(100):
            for window in chrome_windows:
                print(f"Found Chrome window: {window.title}")
            sleep(0.1)
        for i in range(1000):
            #copy all
            hotkey("ctrl", "a")
            hotkey("ctrl", "c")
            clipboard_content = paste()
            print(f"Clipboard content: {clipboard_content}")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Yesterday","Today","Tomorrow"]
            found = False
            for day in days:
                if day in clipboard_content:
                    print(f"Found day in clipboard: {day}")
                    found = True
                    break
            if found:
                break
            sleep(0.1)

    else:
        print("all good")
        chrome = chrome_windows[0]
        if chrome.isMinimized:
            chrome.restore()
        chrome.activate()
        sleep(1)    
    whats_tab_found = False
    for _ in range(20):
        active_title = getActiveWindow().title
        print(f"Active window title: {active_title}")
        if "WhatsApp" in active_title:
            print("Switched to WhatsApp tab.")
            whats_tab_found = True
            break
        hotkey("ctrl", "tab")    
    if whats_tab_found:
        print("WhatsApp tab is active.")
        hotkey("ctrl", "alt", "/")    
        hotkey("ctrl", "a")
        press("delete")

    else:
        print("WhatsApp tab not found. Opening new one...")
        Popen("start chrome https://web.whatsapp.com", shell=True)
        for _ in range(100):
            for window in chrome_windows:
                print(f"Found Chrome window: {window.title}")
            sleep(0.1)
        for i in range(1000):
            #copy all
            hotkey("ctrl", "a")
            hotkey("ctrl", "c")
            clipboard_content = paste()
            print(f"Clipboard content: {clipboard_content}")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Yesterday","Today","Tomorrow"]
            found = False
            for day in days:
                if day in clipboard_content:
                    print(f"Found day in clipboard: {day}")
                    found = True                    
                    break
            if found:   
                    break
            sleep(0.1)        
        print("WhatsApp tab is active.")
        hotkey("ctrl", "alt", "/")
        hotkey("ctrl", "a")
        press("delete")

def send_message(phone:str,message:str):
    hotkey("ctrl", "alt", "/")
    hotkey("ctrl", "a")
    press("delete")
    write(phone)
    press("enter")
    sleep(0.2)
    copy(message)
    hotkey("ctrl", "v")
    press("enter")

if __name__ == "__main__":
    whatsupp_ready()
    phones = ["01080922432","01098570300","01080922432","01098570300","01080922432","01098570300"]
    message = "Hello World"
    for phone in phones:
        send_message(phone, message)
        sleep(0.2)
    