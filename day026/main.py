import pandas as pd

nato_alphabet_dataframe = pd.read_csv('nato_phonetic_alphabet.csv')
column_names = list(nato_alphabet_dataframe.keys())
nato_alphabet_dict = {row[column_names[0]]: row[column_names[1]] for _, row in nato_alphabet_dataframe.iterrows()}

name_input = input('Enter a name: ').upper()
codes = [nato_alphabet_dict[l] for l in name_input]

print(codes)