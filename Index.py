import pyautogui
import time

def switch_between_pages():
    # Define a pausa automática de 0.5 segundos entre as ações do PyAutoGUI
    pyautogui.PAUSE = 0.5

    while True:
        # Pressiona 'alt' e 'tab' para alternar para a próxima janela
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(30)  

        # Pressiona 'alt' e 'tab' duas vezes para alternar para a segunda próxima janela
        pyautogui.keyDown('alt')
        for _ in range(2):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(30)  

        # Pressiona 'alt' e 'tab' para alternar de volta para a primeira janela
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(30)  

if __name__ == "__main__":
    switch_between_pages()