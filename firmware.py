from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

from kmk.keys import KC
import board

keyboard = KMKKeyboard()

# Define row and column pins
keyboard.row_pins = (board.D5, board.D6, board.D7)
keyboard.col_pins = (board.D2, board.D3, board.D4)

# Diode direction: COL2ROW (based on your PCB)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layout: 3x3 matrix
keyboard.keymap = [
    [
        KC.ESC,   KC.UP,    KC.L,      # Row 0
        KC.LEFT,  KC.DOWN,  KC.RIGHT,  # Row 1
        KC.SPACE, KC.ENTER, KC.LSFT    # Row 2
    ]
]

if __name__ == '__main__':
    keyboard.go()
