import pyautogui
import time

numero_de_repeticoes = 30

for _ in range(numero_de_repeticoes):
    pyautogui.click(1239, 382, duration=0.5)
    pyautogui.click(519, 237, duration=0.5)
    pyautogui.click(551, 270, duration=0.5)
    pyautogui.click(933, 655, duration=1.3)

    time.sleep(6)
