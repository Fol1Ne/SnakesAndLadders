import csv

def SendData(game_data_dict):
    with open('game_data.csv', 'w', newline='') as myFile:
        writer = csv.DictWriter(myFile, fieldnames=list(game_data_dict.keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerow(game_data_dict)






        