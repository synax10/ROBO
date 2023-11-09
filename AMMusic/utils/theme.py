


import random
from AMMusic.utils.database import get_theme

themes = [
    "thumb_26",
    "thumb_27",
    "thumb_28",
    "thumb_29",
    "thumb_30",
    "thumb_31",
    "thumb_01",
    "thumb_01",
    "thumb_01",
    "thumb_02",
    "thumb_03",
    "thumb_04",
    "thumb_05",
    "thumb_06",
    "thumb_07",
    "thumb_08",
    "thumb_09",
    "thumb_10",
    "thumb_11",
    "thumb_12",
    "thumb_13",
    "thumb_14",
    "thumb_15",
    "thumb_16",
    "thumb_17",
    "thumb_18",
    "thumb_19",
    "thumb_20",
    "thumb_21",
    "thumb_22",
    "thumb_23",
    "thumb_24",
    "thumb_25",
    "thumb_32",
    "thumb_33",
    "thumb_34",
    "thumb_35",
    "thumb_36",
    "thumb_37",
    "thumb_38",
    "thumb_39",
    "thumb_40",
    "thumb_41",
    "thumb_44",
    "thumb_45",
    "thumb_46",
    "thumb_47",
    "thumb_48",
    "thumb_49",
    "thumb_42",
    "thumb_43",
    "thumb_50",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
