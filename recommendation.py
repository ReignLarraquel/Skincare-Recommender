# %%
import filterdata

from filterdata import recommendation


# %%
def moisturizerRecom(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
   mRecom = recommendation("Moisturizer", opt_skin_type, opt_products_list, opt_allergies_list, opt_acne)
   print(mRecom)
   mRecom.sort_values(by=['Rank'])
   

   return mRecom[0]['Name']

# %%
def cleanserRecom(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
   cRecom = recommendation("Cleanser", opt_skin_type, opt_products_list, opt_allergies_list, opt_acne)

   return cRecom

# %%
def sunscreenRecom(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
   sRecom = recommendation("Sunscreen", opt_skin_type, opt_products_list, opt_allergies_list, opt_acne)

   return sRecom


# %%
# def m(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne):
#    moisturizer = moisturizerRecom(opt_skin_type, opt_products_list, opt_allergies_list, opt_acne)
#    first_item_name = str(moisturizer['Name'].iloc[0])
#    return first_item_name

name_List = ["Brand 1", "Brand 2"]
allergy_List = ["Latex"]

name = moisturizerRecom("Combination", name_List, allergy_List, "No")

print(name)
