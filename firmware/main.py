import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

# Direct pins from StarDance Macropad.kicad_pcb (left → right):
# SW1 = D10, SW2 = D9, SW3 = D8; other side of each switch is GND.
_KEY_CFG = [board.D10, board.D9, board.D8]


class StarDance(KMKKeyboard):
    def __init__(self):
        super().__init__()
        self.matrix = KeysScanner(
            pins=_KEY_CFG,
            value_when_pressed=False,
            pull=True,
            interval=0.02,
            max_events=64,
        )


keyboard = StarDance()

keyboard.keymap = [
    [KC.COPY, KC.PASTE, KC.UNDO],
]

if __name__ == "__main__":
    keyboard.go()
