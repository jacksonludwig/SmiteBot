import requests
from bs4 import BeautifulSoup

CONST_RANKED_DUEL_VAL = 440
CONST_RANKED_JOUST_VAL = 450
CONST_RANKED_CONQUEST_VAL = 451
CONST_UNRANKED_CONQUEST_VAL = 426
CONST_UNRANKED_ARENA_VAL = 435
CONST_UNRANKED_ASSAULT_VAL = 445
CONST_UNRANKED_JOUST_VAL = 448
CONST_UNRANKED_SIEGE_VAL = 459
CONST_UNRANKED_CLASH_VAL = 466


def parse_info(data):
    name = data.strip()
    return name.replace(" ", "-").lower()


def parse_game_mode(game_mode):
    game = parse_info(game_mode)
    if game == "rduel":
        return CONST_RANKED_DUEL_VAL
    if game == "rjoust":
        return CONST_RANKED_JOUST_VAL
    if game == "rconquest":
        return CONST_RANKED_CONQUEST_VAL
    if game == "conquest":
        return CONST_UNRANKED_CONQUEST_VAL
    if game == "arena":
        return CONST_UNRANKED_ARENA_VAL
    if game == "assault":
        return CONST_UNRANKED_ASSAULT_VAL
    if game == "joust":
        return CONST_UNRANKED_JOUST_VAL
    if game == "siege":
        return CONST_UNRANKED_SIEGE_VAL
    if game == "clash":
        return CONST_UNRANKED_CLASH_VAL

    return CONST_RANKED_CONQUEST_VAL


def get_page_info(god_name, game_mode):
    URL = "https://smite.guru/builds/{}?queue={}".format(
        parse_info(god_name), str(parse_game_mode(game_mode)))
    print(URL)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", class_="pro-build")
    for img in results.findAll("img", alt=True):
        print(img["alt"])

    return "sent"
