import pandas as pd

def skinType(test_df, x):
    
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

def allergenFilter (xdd, allergen):
    row = 0
    list = []
    test = xdd
    
    for row in range (len(xdd)):
        list = xdd.Ingredients[row]
        for i in list:
            if i == allergen:
                test = test.drop(row)
                break
    return test