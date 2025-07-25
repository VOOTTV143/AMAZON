from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic import app

    

def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
      
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            
            [
                    InlineKeyboardButton(
                        "⚠️ 𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/I_RAMBHAKT_I"
                    )
                ,
                    InlineKeyboardButton(
                        "📌 𝗨𝗣𝗗𝗔𝗧𝗘", url=f"https://t.me/BOTXBAZAAR"
                    )
                ]         ,       [
                    InlineKeyboardButton(
                        "🛠️ 𝗕𝗢𝗧 𝗠𝗔𝗦𝗧𝗘𝗥", url=f"https://t.me/I_RAMBHAKT_I"
                    )
                ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
