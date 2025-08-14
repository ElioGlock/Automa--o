import pyautogui
import time
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


a = resource_path("images/c.png")
b = resource_path("images/new.png")
c = resource_path("images/button-ulife.png")
d = resource_path("images/account.png")
e = resource_path("images/leave.png")
f = resource_path("images/login.png")
g = resource_path("images/into.png")
h = resource_path("images/leave.png")
i = resource_path("images/pick.png")
j = resource_path("images/course.png")
k = resource_path("images/exten.png")


chrome = pyautogui.locateOnScreen(a, confidence=0.9)
pyautogui.click(chrome)
time.sleep(3)
new = pyautogui.locateOnScreen(b, confidence=0.9)
pyautogui.click(new)
time.sleep(2)
button = pyautogui.locateOnScreen(c, confidence=0.9)
pyautogui.click(button)
time.sleep(2)
try:
    account = pyautogui.locateOnScreen(d, confidence=0.9)
    if account is None:
        raise pyautogui.ImageNotFoundException
    else:
        pyautogui.click(account)
        time.sleep(2)
        leave = pyautogui.locateOnScreen(e, confidence=0.9)
        pyautogui.click(leave)
        time.sleep(2)
        login = pyautogui.locateOnScreen(f, confidence=0.9)
        pyautogui.click(login)
        time.sleep(2)
        pyautogui.write("202512408")
        time.sleep(2)
        into = pyautogui.locateOnScreen(g, confidence=0.9)
        pyautogui.click(into)
        time.sleep(2)
        pick = pyautogui.locateOnScreen(i, confidence=0.9)
        pyautogui.click(pick)
        time.sleep(4)
        course = pyautogui.locateOnScreen(j, confidence=0.9)
        pyautogui.click(course)
        time.sleep(2)
        exten = pyautogui.locateOnScreen(k, confidence=0.9)
        pyautogui.click(exten)


except pyautogui.ImageNotFoundException:
    login = pyautogui.locateOnScreen(f, confidence=0.9)
    pyautogui.click(login)
    time.sleep(2)
    pyautogui.write("202512408")
    time.sleep(2)
    into = pyautogui.locateOnScreen(g, confidence=0.9)
    pyautogui.click(into)
    time.sleep(2)
    pick = pyautogui.locateOnScreen(i, confidence=0.9)
    pyautogui.click(pick)
    time.sleep(4)
    course = pyautogui.locateOnScreen(j, confidence=0.9)
    pyautogui.click(course)
    time.sleep(2)
    exten = pyautogui.locateOnScreen(k, confidence=0.9)
    pyautogui.click(exten)



