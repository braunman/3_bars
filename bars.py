# -*- coding: utf-8 -*-
import sys
import json
from geopy.distance import vincenty
import os.path

def load_data(filepath):
    with open(filepath, encoding="utf8") as data_file:
        bars_data = json.load(data_file)
    return bars_data


def get_biggest_bar(data):
    return max(data, key = lambda x: x['Cells']["SeatsCount"])


def get_smallest_bar(data):
    return min(data, key = lambda x: x['Cells']["SeatsCount"])



def get_closest_bar(data, longitude, latitude):
    return min(data, key = lambda x: vincenty((longitude, latitude),
            x['Cells']['geoData']['coordinates']).meters)


if __name__ == '__main__':
    try:
        json_bars_file = sys.argv[1]
        if not os.path.exists(json_bars_file):
            print("Переданный файл не существует")
            exit(1)
    except IndexError:
        print ("Вы не передали скрипту файл с барами")
        exit(1)
    bars_data = load_data(json_bars_file)
    print("Самый большой бар:\n{}" .format(get_biggest_bar(bars_data)), end = "\n"*2 )
    print ("Самый маленький бар:\n{}".format(get_smallest_bar(bars_data)), end = "\n"*2 )
    print ("Введите координаты по одной( в формате - 39.635709999611 ):")
    try:
        northern_latitude = float(input("северная широта:"))
        eastern_longitude = float(input("восточная долгота:"))
    except:
        print("Не верно введены координаты, попробуйте в формате 39.6357099")
        exit(1)
    print ("Самый близкий бар:\n{}".format(
        get_closest_bar(bars_data, northern_latitude , eastern_longitude)), 
    end = "\n"*2 )

