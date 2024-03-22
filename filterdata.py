import pandas as pd
import processdata

def convert_to_list(string):
    return string.split(', ')

df = processdata.process_df()
#df['Ingredients'] = df['Ingredients'].apply(convert_to_list)

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

def allergenFilter (df, opt_allergies_list):
    for allergen in opt_allergies_list:
        df = df[~df['Ingredients'].apply(lambda x: allergen in x)]
    return df

def labelFilter(df, label):
    filtered_df = df[df['Label'] == label]
    return filtered_df

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

def hasAcne(df, opt_acne):
    if opt_acne == "Yes":
        filtered_df = df[df.Acne == 1] 
        return filtered_df
    else:
        return df

def productdf_to_list(df): #converts df to list #Note: useful since output of the filter is a df and you probably want a list
    if not df.empty:
        return {"Brand": df['Brand'].tolist()[0], "Product": df['Name'].tolist()[0], "Link": "www.google.com"}  
    else:
        return {}

def recommendation(label, opt_skin_type, opt_allergies_list, opt_acne):
    data = df
    sT = skinType(data, opt_skin_type)  # Assume returns DataFrame with a common unique identifier
    lbl = labelFilter(sT, label)  # Same assumption
    acne = hasAcne(lbl, opt_acne)
    allergens = allergenFilter(acne, opt_allergies_list) 

    allergens = allergens.sort_values(by="Rank",ascending=False)
    allergens = productdf_to_list(allergens)

    return allergens

def checkExisting(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne): #checks if exisitng products is good for skin type. Format: ['Brand', 'Name', 'Link']
    moisturizer = pd.DataFrame()
    cleanser = pd.DataFrame()
    sunscreen = pd.DataFrame()
    for product in opt_products_list:
        product = df[df['Name'] == product]
        product = product[~product['Ingredients'].apply(lambda x: any(allergen in x for allergen in opt_allergies_list))]
        label = product['Label'].to_string(index=False)
        match label:
            case "Moisturizer":
                product = hasAcne(product, opt_acne)
                if product[opt_skin_type].to_string(index=False) == '1':
                    moisturizer = product
            case "Cleanser":
                product = hasAcne(product, opt_acne)
                if product[opt_skin_type].to_string(index=False) == '1':
                    cleanser = product
            case "Sun protect":
                if product[opt_skin_type].to_string(index=False) == '1':
                    sunscreen = product
    
    moisturizer = productdf_to_list(moisturizer)
    cleanser = productdf_to_list(cleanser)
    sunscreen = productdf_to_list(sunscreen)
    
    return moisturizer, cleanser, sunscreen