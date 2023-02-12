from telegram import *
from telegram.ext import *
player_mode = 'X'
bot_mode = 'O'
turn_count = 0
status = 'ХОДИТЕ ЗА ' + player_mode

table = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def reset_table():
    global table
    table = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    return
    
def get_status():
    return status

def win_condition(mode):
    global table
    global turn_count
    for i in range(3):
        cols = True
        rows = True
        right = True
        left = True
        for j in range(3):
            right &= (table[j][j] == mode)
            left &= (table[2-j][j] == mode)
            cols &= (table[i][j] == mode)
            rows &= (table[j][i] == mode)

        if left or right or cols or rows:
            return mode

    return ' ' if turn_count == 9 else ''

def get_table():
    buttons = []
    for row in range(0,3):
        br = []
        for col in range(0,3):
            br.append(InlineKeyboardButton(table[row][col], callback_data=f"{row}{col}"))
        buttons.append(br)
    return InlineKeyboardMarkup(buttons)

def reset():
    global turn_count
    turn_count = 0
    reset_table()
    return

def set_playerX():
    