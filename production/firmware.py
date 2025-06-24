import board
from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.scanners.keypad import KeysScanner # type: ignore
from kmk.keys import KC # type: ignore
from kmk.modules.macros import Press,Release,Tap,Macros # type: ignore

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
PINS=[board.D3, board.D4, board.D1, board.D2]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.MACRO(              # Macro for clearing the console on windows (Also stops any running process in that console)
            Tap(KC.LCTL(KC.C)),
            Tap(KC.LCTL(KC.A)),
            Tap(KC.DEL),
            Tap(KC.C),
            Tap(KC.L),
            Tap(KC.S),
            Tap(KC.ENTER)
        ), 
        KC.MACRO(
            Tap(KC.LCTL(KC.C)),  # Macro for copying selected text to clipboard
            Tap(KC.LCTL(KC.C))
        ), 
        KC.MACRO(
            Tap(KC.LCTL(KC.V))  # Macro for pasting from clipboard
        ), 
        KC.MACRO(
            Tap(KC.LCTL(KC.Z))  # Macro for undoing the last action
        )
    ]
]

if __name__ == '__main__':
    keyboard.go()