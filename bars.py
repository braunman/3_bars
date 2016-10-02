import json

file = "bars.json"

def load_data(filepath):
    url = 'http://data.mos.ru/opendata/7710881420-bary'
    with open(file) as data_file:    
        data = json.load(data_file)
    return data


def get_biggest_bar(data):
    print("Самый большой бар:")
    big = 0 
    bar = []
    for i in data:
        seats = i['Cells']["SeatsCount"]
        if big <= seats or not big:
            big = seats
            bar = i['Cells']
    print (bar['Name'], bar['Address'], bar['SeatsCount'], 'мест')


def get_smallest_bar(data):
    print("Самый маленький бар:")
    big = None
    bar = []
    for i in data:
        seats = i['Cells']["SeatsCount"]
        if not big:
            big = seats
        if big >= seats:
            big = seats
            bar = i['Cells']
    print (bar['Name'], bar['Address'], bar['SeatsCount'], 'мест')



def get_closest_bar(data, longitude, latitude):
    
    pass


if __name__ == '__main__':
    data = load_data(file)
    get_biggest_bar(data)
    get_smallest_bar(data)
