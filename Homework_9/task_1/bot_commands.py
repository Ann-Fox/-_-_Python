from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from random import randint
import xo_new

game_is_started = False
player_sym = ""


def start_command(update: Update, context: CallbackContext):
    global player_sym, game_is_started

    if not game_is_started:
        game_is_started = True
        player_sym = xo_new.game_init()
        update.message.reply_text(f'{xo_new.print_field(player_sym)}\n\nВы ходите {player_sym}')
    else:
        update.message.reply_text(f'Игра уже идёт')


def analize_command(update: Update, context: CallbackContext):
    global player_sym, game_is_started

    msg = update.message.text  # ~input
    res_str = ""
    
    if game_is_started:

        if msg in ["/A1", "/A2", "/A3", "/B1", "/B2", "/B3", "/C1", "/C2", "/C3"]:
            match xo_new.player_move(msg[1:]):
                case -1:
                    res_str = xo_new.print_field(player_sym) + '\n\nНичья! Ещё раз? /start'
                    game_is_started = False
                case 0:
                    res_str = xo_new.print_field(player_sym)
                case 1:
                    res_str = xo_new.print_field(player_sym) + '\n\nПоздравляю! Вы выиграли! Ещё раз? /start'
                    game_is_started = False
                case 2:
                    res_str = xo_new.print_field(player_sym) + '\n\nЯ победил! Ещё раз? /start'
                    game_is_started = False

            if not game_is_started:
                update.message.reply_text(res_str)
            else:
                res_str = ""
                match xo_new.player_move(msg[1:]):
                    case -1:
                        res_str = xo_new.print_field(player_sym) + '\n\nНичья! Ещё раз? /start'
                        game_is_started = False
                    case 0:
                        res_str = xo_new.print_field(player_sym)
                    case 1:
                        res_str = xo_new.print_field(player_sym) + '\n\nПоздравляю! Вы выиграли! Ещё раз? /start'
                        game_is_started = False
                    case 2:
                        res_str = xo_new.print_field(player_sym) + '\n\nЯ победил! Ещё раз? /start'
                        game_is_started = False
                update.message.reply_text(res_str)
        else:
            if game_is_started:
                update.message.reply_text(f"Вы указали неправильное поле. Выберите поле, куда собираетесь поставить {player_sym}")
            else:
                update.message.reply_text(f"Игра ещё не началась. /start")

def quit_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    update.message.reply_text('Бот остановлен')
    quit()
