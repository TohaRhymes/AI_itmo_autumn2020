# -*- coding: utf-8 -*-

from typing import Set

map = {
    "Брест":[
        {"name":"Вильнюс", "dist":531},
        {"name":"Витебск", "dist":638},
        {"name":"Калининград",  "dist":699}],
    "Вильнюс":[
        {"name":"Брест",  "dist":531},
        {"name":"Витебск", "dist":360},
        {"name":"Даугавпилс",  "dist":211},
        {"name":"Калининград",  "dist":333},
        {"name":"Каунас",  "dist":102},
        {"name":"Киев",  "dist":634}],
    "Витебск":[
        {"name":"Брест",  "dist":638},
        {"name":"Вильнюс",  "dist":360},
        {"name":"Волгоград",  "dist":1455},
        {"name":"Воронеж",  "dist":869},
        {"name":"Ниж.Новгород",  "dist":911},
        {"name":"Орел",   "dist":522},
        {"name":"С.Петербург",  "dist":602}],
    "Волгоград":[
        {"name":"Витебск", "dist": 1455},
        {"name":"Воронеж", "dist": 581},
        {"name":"Житомир", "dist": 1493},
    ],
    "Воронеж":[
        {"name":"Витебск", "dist": 869},
        {"name":"Волгоград", "dist": 581},
        {"name":"Ярославль", "dist": 739},
    ],
    "Даугавпилс":[
        {"name":"Вильнюс", "dist": 211},
    ],
    "Донецк":[
        {"name": "Житомир", "dist": 863},
        {"name": "Кишинев", "dist": 812},
        {"name": "Москва", "dist": 1084},
        {"name": "Орел", "dist": 709},
    ],
    "Житомир":[
        {"name":"Волгоград", "dist": 1493},
        {"name":"Донецк", "dist": 863},
        {"name":"Киев", "dist": 131},
    ],
    "Казань":[
        {"name":"Москва", "dist": 815},
        {"name":"Уфа", "dist": 525},
    ],
    "Калининград":[
        {"name":"Брест", "dist": 699},
        {"name":"Вильнюс", "dist": 333},
        {"name":"С.Петербург", "dist": 739},
    ],
    "Каунас":[
        {"name":"Вильнюс", "dist": 102},
        {"name":"Рига", "dist": 267},
    ],
    "Киев":[
        {"name":"Вильнюс", "dist": 634},
        {"name":"Житомир", "dist": 131},
        {"name":"Кишинев", "dist": 467},
        {"name":"Одесса", "dist": 487},
        {"name":"Харьков", "dist": 471},
    ],
    "Кишинев":[
        {"name":"Донецк", "dist": 812},
        {"name":"Киев", "dist": 467},
    ],
    "Минск":[
        {"name":"Москва", "dist": 690},
        {"name":"Мурманск", "dist": 2238},
        {"name":"Ярославль", "dist": 940},
    ],
    "Москва":[
        {"name":"Донецк", "dist": 1084},
        {"name":"Казань", "dist": 815},
        {"name":"Минск", "dist": 690},
        {"name":"Ниж.Новгород", "dist": 411},
        {"name":"Орел", "dist": 368},
        {"name":"С.Петербург", "dist": 664},
    ],
    "Мурманск":[
        {"name":"Минск", "dist": 2238},
        {"name":"С.Петербург", "dist": 1412},
    ],
    "Ниж.Новгород":[
        {"name":"Витебск", "dist": 911},
        {"name":"Москва", "dist": 411},
    ],
    "Одесса":[
        {"name":"Киев", "dist": 487},
    ],
    "Орел":[
        {"name":"Витебск", "dist": 522},
        {"name":"Донецк", "dist": 709},
        {"name":"Москва", "dist": 368},
    ],
    "Рига":[
        {"name":"Каунас", "dist": 267},
        {"name":"С.Петербург", "dist": 641},
        {"name":"Таллин", "dist": 308},
    ],
    "С.Петербург":[
        {"name":"Витебск", "dist": 602},
        {"name":"Калининград", "dist": 739},
        {"name":"Москва", "dist": 664},
        {"name":"Мурманск", "dist": 1412},
        {"name":"Рига", "dist": 641},
    ],
    "Самара":[
        {"name":"Уфа", "dist": 461},
    ],
    "Симферополь":[
        {"name":"Харьков", "dist": 639},
    ],
    "Таллин":[
        {"name":"Рига", "dist": 308},
    ],
    "Уфа":[
        {"name":"Казань", "dist": 525},
        {"name":"Самара", "dist": 461},
    ],
    "Харьков":[
        {"name":"Киев", "dist": 471},
        {"name":"Симферополь", "dist": 639},
    ],
    "Ярославль":[
        {"name":"Воронеж", "dist": 739},
        {"name":"Минск", "dist": 940},
    ],
}

counter = 0
route = ""

def make_route(checked: Set, cur: str, suffix: str):
    checked.add(cur)
    global counter
    global route
    counter += 1

    cnt = counter

    destinations = map[cur]
    for city in destinations:
        city_name = city["name"]
        if city_name not in checked:
            route += f"\n\"{cur}_{suffix}\"->\"{city_name}_{cnt}\""
            make_route(checked, city_name, cnt)

    checked.remove(cur)


if __name__=="__main__":
    checked = set()
    suffix = ""
    cur ="Самара"

    make_route(checked, cur, suffix)

    print(route)