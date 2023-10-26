import csv

def ReadData():
    with open('game_data.csv', 'r') as myFile:
        reader = csv.reader(myFile)
        game_data = list(reader)
        return game_data












