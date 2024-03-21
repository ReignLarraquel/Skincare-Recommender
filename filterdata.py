# %%
import pandas as pd
import processdata

def convert_to_list(string):
    return string.split(', ')

df = processdata.process_df()

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
    row = 0
    list = []
    test = df
    print(df.Ingredients[9])
    for row in range (len(df)):
        list = df.Ingredients[row]
        for i in list:
            for allergy in opt_allergies_list:
                if i == allergy:
                    test = test.drop(row)
                    break
    return test

# %%
def labelFilter(df, label):
    filtered_df = df[df['Label'] == label]
    return filtered_df

# %%
# def getBrands(df, opt_products_list):
#    list = []
#    brands = df
#    row = 0

#    for row in range (len(df)):
#       list = df.Brand[row]
#       for i in list:
#          if i != opt_products_list:
#             brands = brands.drop(row)
#             break
#    return brands

# %%
def hasAcne(df, opt_acne):
    if opt_acne == "Yes":
        filtered_df = df[df['Ingredients'].apply(lambda x: 'Salicylic Acid' in x)]
    return filtered_df

# %%

def recommendation(label, opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
    data = df
    sT = skinType(data, opt_skin_type)  # Assume returns DataFrame with a common unique identifier
    lbl = labelFilter(sT, label)  # Same assumption
    # brands = getBrands(lbl, opt_products_list)  # Same assumption
    last_df = allergenFilter(lbl, opt_allergies_list) 
    

    # merge1 = pd.merge(sT, lbl, on='common_unique_identifier', how='inner')
    # merge2 = pd.merge(merge1, brands, on='common_unique_identifier', how='inner')
    # result_df = pd.merge(merge2, allergens, on='common_unique_identifier', how='inner')

    if label == "Cleanser":
         last_df = hasAcne(last_df, opt_acne)  # Assume returns DataFrame with the same common unique identifier

    return last_df

# Specify your CSV file path
# csv_file_path = 'path/to/your/file.csv'
# # Specify your Excel file path
# excel_file_path = 'path/to/your/newfile.xlsx'

# Read the CSV file


# Save the DataFrame to an Excel file
#df.to_excel(excel_file_path, index=False, engine='openpyxl')

