import pyautogui

class InputController:
    def move(self, x: int, y: int) -> None:
        pyautogui.moveTo(x, y, duration=0.15)

    def click(self, x: int, y: int) -> None:
        pyautogui.click(x, y)

    def type_text(self, text: str) -> None:
        pyautogui.write(text, interval=0.01)

    def press(self, key: str) -> None:
        pyautogui.press(key)
