import pandas as df
baseball_player = df.read_csv('data/Master.csv')

baseball_player = df.DataFrame(baseball_player)
baseball_player['nameFull'] = baseball_player['nameFirst'] + " " + baseball_player['nameLast']
print(baseball_player['nameFull'])