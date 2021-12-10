from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# \\\ Auto narxlar uchun ///
auto = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Damas-2 (75mln)",callback_data="damas")
        ],
        [ 
            InlineKeyboardButton(text="Spark (94mln)",callback_data="spark")
        ],
        [
            InlineKeyboardButton(text="Nexia-3 (109mln)",callback_data="nexia")
        ],
        [
            InlineKeyboardButton(text="Cobalt (116mln)",callback_data="cobalt")
        ],
        [
            InlineKeyboardButton(text="Lacetti (115mln)",callback_data="lacetti")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga",callback_data="back")
        ],    
    ]
)