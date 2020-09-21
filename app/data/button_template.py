from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data.localization import inline_buttons

temp_buttons = ['temp_btn1', 'temp_btn2', 'temp_btn3', 'temp_btn4']

phenomena_list = [
    "strong wind", "hailstorm", "hurricane", "storm", "rain", "heavy rain", "fog", "intense heat"
]


def gen_markup_hours(user_id, model, lang, callback='', ):
    markup = InlineKeyboardMarkup(row_width=4)
    for hours in range(0, 24, 4):
        temp_button_dict = {}
        for temp_btn in temp_buttons:
            if model.query.filter_by(user_id=user_id, hours=hours).first():
                tick = '✔'
            else:
                tick = '✖'
            temp_button_dict[temp_btn] = InlineKeyboardButton(f"{tick}{hours:0>2}:00",
                                                              callback_data=f"{hours:0>2}hr{callback}")
            hours += 1
        button_values = [v for k, v in temp_button_dict.items()]
        markup.add(button_values[0], button_values[1], button_values[2], button_values[3])
    if callback == '_ph':
        markup.add(InlineKeyboardButton(inline_buttons['back'][lang], callback_data=f"back_to{callback}"))
    return markup


def gen_markup_minutes(user_id, hours, model, lang, callback='', ):
    markup = InlineKeyboardMarkup(row_width=3)
    for mins in range(0, 60, 30):
        temp_button_dict = {}
        for temp_btn in temp_buttons[:3]:
            if model.query.filter_by(user_id=user_id, hours=hours, minutes=mins).first():
                tick = '✔'
            else:
                tick = '✖'
            temp_button_dict[temp_btn] = InlineKeyboardButton(f"{tick}{hours}:{mins:0>2}",
                                                              callback_data=f"{hours}:{mins:0>2}min{callback}")
            mins += 10
        button_values = [v for k, v in temp_button_dict.items()]
        markup.add(button_values[0], button_values[1], button_values[2])
    markup.add(InlineKeyboardButton(inline_buttons['back'][lang], callback_data=f"back_to_hours{callback}"))
    return markup
