from mss import mss
from PIL import Image

class ScreenController:
    def __init__(self) -> None:
        self._mss = mss()

    def size(self) -> tuple[int, int]:
        monitor = self._mss.monitors[1]
        return int(monitor["width"]), int(monitor["height"])

    def screenshot(self, path: str = "screen.png") -> str:
        monitor = self._mss.monitors[1]
        image = self._mss.grab(monitor)
        Image.frombytes("RGB", image.size, image.rgb).save(path)
        return path
