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
    print("The URL about to be scraped is: {}".format(URL))

    page = requests.get(URL)

    return BeautifulSoup(page.content, "html.parser")


def find_pro_builds(soup):
    items = []
    results = soup.find("div", class_="pro-build")
    for img in results.findAll("img", alt=True):
        items.append(img["alt"])
    return items


def find_generic_build(soup):
    items = []


def get_results(god_name, game_mode):
    build_list = []
    soup = get_page_info(god_name, game_mode)

    game_num = parse_game_mode(game_mode)
    if game_num == CONST_RANKED_CONQUEST_VAL or game_num == CONST_UNRANKED_CONQUEST_VAL:
        build_list = find_pro_builds(soup)
    else:
        build_list = find_generic_build(soup)

    return build_list
