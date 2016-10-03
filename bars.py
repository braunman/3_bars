# -*- coding: utf-8 -*-
import json
from geopy.distance import vincenty

data_file = "bars.json"

def load_data(filepath):
    url = 'http://data.mos.ru/opendata/7710881420-bary'
    with open(filepath, encoding="utf8") as data_file:    
        data = json.load(data_file)
    return data


def get_biggest_bar(data):
    print("Самый большой бар:\n", max(data, key = lambda x: x['Cells']["SeatsCount"]), end = "\n"*2 )


def get_smallest_bar(data):
    print ("Самый маленький бар:\n", min(data, key = lambda x: x['Cells']["SeatsCount"]), end = "\n"*2 )



def get_closest_bar(data, longitude, latitude):
    print ("Самый близкий бар:\n", 
        min(data, key = lambda x: vincenty((longitude, latitude),x['Cells']['geoData']['coordinates']).meters), end = "\n"*2 )


if __name__ == '__main__':
    data = load_data(data_file)
    get_biggest_bar(data)
    get_smallest_bar(data)
    print ("Введите координаты по одной( в формате - 39.635709999611 ):")
    try:
        n = float(input("северная широта:"))
        e = float(input("восточная долгота:"))
    except:
        print("Вы ввели что-то не так")
    get_closest_bar(data, n , e)


