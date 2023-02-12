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