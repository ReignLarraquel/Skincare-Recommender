import pandas as pd

def convert_to_list(string):
    return string.split(', ')
	
def for_acne(list):
    acne_ingredients = ['Benzoyl Peroxide', 'Salicylic Acid', 'Alpha Hydroxy Acids', 'Azelaic Acid', 'Adapalene']
    return 1 if any(elem in list for elem in acne_ingredients) else 0
	

def process_df():
	df = pd.read_csv('cosmetics.csv')
	df['Ingredients'] = df['Ingredients'].apply(convert_to_list)

	df['Acne'] = df['Ingredients'].apply(for_acne)
	return df
