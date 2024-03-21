# %%
import pandas as pd

def convert_to_list(string):
    return string.split(', ')

df = pd.read_csv('cosmetics.csv')
df['Ingredients'] = df['Ingredients'].apply(convert_to_list)

# %%
def skinType(df, x):

    test_df = df
    
    match x:
        case "Combination":
            test_df = test_df[test_df.Combination == 1]
        case "Dry":
            test_df = test_df[test_df.Dry == 1]
        case "Normal":
            test_df = test_df[test_df.Normal == 1]
        case "Oily":
            test_df = test_df[test_df.Oily == 1]
        case "Sensitive":
            test_df = test_df[test_df.Sensitive == 1]
            
    return test_df

# %%
def allergenFilter (df, opt_allergies_list):
    for allergen in opt_allergies_list:
        test = test[~test['Ingredients'].apply(lambda x: allergen in x)]
    return test

# %%
def labelFilter(df, label):
    filtered_df = df[df['Label'] == label]
    return filtered_df

# %%
def getBrands(df, opt_products_list):
   list = []
   brands = df
   row = 0

   for row in range (len(df)):
      list = df.Brand[row]
      for i in list:
         if i != opt_products_list:
            brands = brands.drop(row)
            break
   return brands

# %%
def hasAcne(df, opt_acne):
    if opt_acne == "Yes":
        filtered_df = df[df['Ingredients'].apply(lambda x: 'Salicylic Acid' in x)]
    return filtered_df

# %%

def recommendation(label, opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
    data = df
    sT = skinType(data, opt_skin_type)  # Assume returns DataFrame with a common unique identifier
    lbl = labelFilter(data, label)  # Same assumption
    brands = getBrands(data, opt_products_list)  # Same assumption
    allergens = allergenFilter(data, opt_allergies_list) 
    

    merge1 = pd.merge(sT, lbl, on='common_unique_identifier', how='inner')
    merge2 = pd.merge(merge1, brands, on='common_unique_identifier', how='inner')
    result_df = pd.merge(merge2, allergens, on='common_unique_identifier', how='inner')

    if label == "Cleanser":
        acne = hasAcne(data, opt_acne)  # Assume returns DataFrame with the same common unique identifier
        result_df = pd.merge(result_df, acne, on='common_unique_identifier', how='inner')

    return result_df

