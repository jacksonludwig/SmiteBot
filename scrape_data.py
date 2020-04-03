import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

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
    return data.strip().replace(" ", "-").lower()


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
        parse_info(god_name), game_mode)

    print("The URL about to be scraped is: {}".format(URL))

    return BeautifulSoup(requests.get(URL).content, "html.parser")


'''
def find_pro_builds(soup):
    items = []
    results = soup.find("div", class_="pro-build")
    for img in results.findAll("img", alt=True):
        items.append(img["alt"])
    return items
'''


def find_pro_builds_start(soup):
    items = []
    build_div = soup.find("div", attrs={"class": "pro-build"})

    for item in build_div:
        if isinstance(item, NavigableString):
            continue
        if item.text == "Final Build":
            break
        if item.get("class") == None:
            data = item.findAll("img")
            for image in data:
                items.append(image["alt"])

    return items


def find_generic_build(soup):
    items = []


def get_results(god_name, game_mode):
    build_list = []
    game_num = parse_game_mode(game_mode)
    soup = get_page_info(god_name, game_num)

    if game_num == CONST_RANKED_CONQUEST_VAL or game_num == CONST_UNRANKED_CONQUEST_VAL:
        build_list = find_pro_builds_start(soup)
    else:
        build_list = find_generic_build(soup)

    return build_list
