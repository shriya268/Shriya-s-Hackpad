import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

rows = (board.D5, board.D6, board.D7)
cols = (board.D2, board.D3, board.D4)

keys = keypad.KeyMatrix(row_pins=rows, column_pins=cols, columns_to_anodes=False)

kbd = Keyboard(usb_hid.devices)

keymap = {
    0: Keycode.ESCAPE,      
    1: Keycode.UP_ARROW,     
    2: Keycode.L,           
    3: Keycode.LEFT_ARROW,   
    4: Keycode.DOWN_ARROW,   
    5: Keycode.RIGHT_ARROW,  
    6: Keycode.SPACEBAR,     
    7: Keycode.ENTER,        
    8: Keycode.SHIFT         
}

while True:
    event = keys.events.get()
    if event:
        if event.pressed:
            kbd.press(keymap[event.key_number])
        elif event.released:
            kbd.release(keymap[event.key_number])
