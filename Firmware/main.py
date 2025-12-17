# Using the starter code:
# You import all the IOs of your board
import board
# oled display import
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# oled display import
from kmk.extensions.display import Display, TextEntry, ImageEntry # don't know if I will do images yet
from kmk.extensions.display.ssd1306 import SSD1306

# global variables
last_key = "Waiting..."

def update_last_key(keyboard):
    global last_key
    if keyboard.keys_pressed:
        last_key = keyboard.keys_pressed[0].name

def show_last_key():
    return last_key

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
keyboard.before_matrix_scan = update_last_key

# oled display instance
# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Display.md
i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(i2c=i2c_bus)
display = Display(display=driver, width=128, height=32, flip=False, flip_left=False, flip_right=False,
                  brightness=0.8, brightness_step=0.1, dim_time=20, dim_target=0.1, off_time=60, powersave_dim_time=10,
                  powersave_dim_target=0.1, powersave_off_time=30) # every parameter here for future reference, all default values

# Add the macro extension (I won't be using macros right now) For future reference: KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)) -> in keymap
# macros = Macros()
# keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D0, board.D1, board.D2, board.D3, board.D6, board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.Y, KC.U, KC.I, KC.O, KC.P, KC.H, KC.J, KC.K, KC.L]
]

# Text display
display.entries = [
    TextEntry(text=show_last_key, x=64, y=16, x_anchor='M', y_anchor='M', scale=3)
]

keyboard.extensions.append(display)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()