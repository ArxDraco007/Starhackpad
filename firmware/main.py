import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.keymap = [
    [
        KC.NUM_1, KC.NUM_2, KC.NUM_3, KC.NUM_4,
        KC.NUM_5, KC.NUM_6, KC.NUM_7, KC.NUM_8,
        KC.NUM_9, KC.NUM_0, KC.BSPC,  KC.ENTER,
        KC.ESC,   KC.TAB,   KC.SPACE, KC.NO, 
    ]
]
encoder_handler.map = [
    [(KC.VOLD, KC.VOLU, KC.NO)],
]

encoder_handler.pins = ((board.D4, board.D5, None),)

if __name__ == "__main__":
    keyboard.go()