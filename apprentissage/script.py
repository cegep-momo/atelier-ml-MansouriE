import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

nosPokemons = pd.read_csv("datas/pokedex.csv")
print(nosPokemons.columns.values)

