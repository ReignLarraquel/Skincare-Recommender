"""
EMPATHY S13 - Group 1
Members:
    DY, Justin
    JUMILLA, Sarah
    LARRAQUEL, Reign
    RECOMONO, Francis
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import csv
import tkinter as tk
from tkinter import ttk

import filterdata

from filterdata import recommendation
from filterdata import checkExisting

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.title("Skincare Recommender")
app.geometry('900x700')

#COVER FRAME
cover_frame = ctk.CTkFrame(app, width=350, height=700)
cover_frame.grid(row=0, column=0, padx=0, pady=0)

cov = ctk.CTkImage(light_image=Image.open("cover.png"),
                                  size=(350, 700))
cover_label = ctk.CTkLabel(cover_frame, image=cov, text="")
cover_label.pack()



#MAIN FRAME
frame = ctk.CTkFrame(app, width=550, height=700, fg_color="#FFFFF9")
frame.grid(row=0, column=1, padx=0, pady=0)

#TITLE
title = ctk.StringVar(value="SKINCARE RECOMMENDER")
sub_title = ctk.StringVar(value="Find your perfect balance!")

title_label = ctk.CTkLabel(master=frame, textvariable=title, font=("Arial", 28, "bold"))
title_label.configure(text_color="sky blue")
title_label.place(relx=0.5, rely=0.05, anchor=ctk.CENTER)

sub_title_label = ctk.CTkLabel(master=frame, textvariable=sub_title, font=("Helvetica", 14), fg_color="transparent")
sub_title_label.configure(text_color="gray")
sub_title_label.place(relx=0.5, rely=0.09, anchor=ctk.CENTER)

#####################################################################################
# variables (user inputs)
opt_skin_type = ctk.StringVar(value="Normal")
opt_acne = ctk.StringVar(value="No")
opt_products_list = [] 
opt_allergies_list = [] 
#####################################################################################

#SKIN TYPE
skin_type_label = ctk.CTkLabel(master=frame, text="Choose skin type:", font=("Arial", 13))
skin_type_label.place(relx=0.235, rely=0.15, anchor=ctk.CENTER)

skin_type_combobox = ctk.CTkComboBox(master=frame, values=["Combination", "Dry", "Normal", "Oily", "Sensitive"], variable=opt_skin_type, width=150)
skin_type_combobox.place(relx=0.30, rely=0.20, anchor=ctk.CENTER)

#ACNE
acne_label = ctk.CTkLabel(master=frame, text="Do you have acne?", font=("Arial", 13))
acne_label.place(relx=0.265, rely=0.24, anchor=ctk.CENTER)

acne_yes_radiobttn = ctk.CTkRadioButton(master=frame, text="Yes", fg_color="light blue", variable=opt_acne, value="Yes")
acne_yes_radiobttn.place(relx=0.45, rely=0.28, anchor=ctk.CENTER)

acne_no_radiobttn = ctk.CTkRadioButton(master=frame, text="No", fg_color="light blue", variable=opt_acne, value="No")
acne_no_radiobttn.place(relx=0.68, rely=0.28, anchor=ctk.CENTER)

#SKINCARE ROUTINE
products = []
brands = []#for combobox display

with open("cosmetics.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append({"Brand": row['Brand'], "Name": row['Name']})
        if row['Brand'] not in brands:
            brands.append(row['Brand'])

brands.sort()

def add_product(product_combobox, selected_brand, add_product_button):
    name = product_combobox.get()
    if name:
        #prod = selected_brand + " - " + name
        if name not in opt_products_list:
            opt_products_list.append(name)
        update_products_label()
        ########
        product_label.place_forget()
        product_combobox.place_forget()
        add_product_button.place_forget()

def update_products_label():
    products_selected_label_var.set("Products:\n∙ " + "\n∙ ".join(opt_products_list))

    vertical_scroll_frame.inner_height = products_selected_label.winfo_reqheight()
    horizontal_scroll_frame.inner_width = products_selected_label.winfo_reqwidth()    

def filter_products():
    selected_brand = brand_combobox.get()
    if selected_brand:
        filtered_products = [f"{product['Name']}" for product in products if product["Brand"] == selected_brand]
        if filtered_products:
            filtered_products.sort()
            product_label.place(relx=0.19, rely=0.43, anchor=ctk.CENTER)
            product_combobox = ctk.CTkComboBox(master=frame, values=filtered_products, width=250)
            product_combobox.place(relx=0.35, rely=0.47, anchor=ctk.CENTER)
            
            add_product_button = ctk.CTkButton(master=frame, text="Add Product", border_color="light blue", command=lambda: add_product(product_combobox, selected_brand, add_product_button), width=100)
            add_product_button.place(relx=0.80, rely=0.47, anchor=ctk.CENTER)
            
            product_combobox.set(filtered_products[0])#default


routine_label = ctk.CTkLabel(master=frame, text="Provide your current skincare routine:", font=("Arial", 13))
routine_label.place(relx=0.355, rely=0.32, anchor=ctk.CENTER)

brand_label = ctk.CTkLabel(master=frame, text="Select brand of product first:", font=("Arial", 13))
brand_label.place(relx=0.26, rely=0.35, anchor=ctk.CENTER)

brand_combobox = ctk.CTkComboBox(master=frame, values=brands, width=250)
brand_combobox.place(relx=0.35, rely=0.39, anchor=ctk.CENTER)

filter_button = ctk.CTkButton(master=frame, text="Filter", border_color="light blue", command=filter_products, width=100)
filter_button.place(relx=0.80, rely=0.39, anchor=ctk.CENTER)

product_label = ctk.CTkLabel(master=frame, text="Select product:", font=("Arial", 13))
product_label.place_forget()

products_selected_label_var = ctk.StringVar(value="")

vertical_scroll_frame = ctk.CTkScrollableFrame(master=frame, width=400, height=80, orientation="vertical", fg_color="white", border_color="light gray", border_width=2)
vertical_scroll_frame.place(relx=0.5, rely=0.57, anchor=ctk.CENTER)

horizontal_scroll_frame = ctk.CTkScrollableFrame(master=vertical_scroll_frame, orientation="horizontal", fg_color="white")
horizontal_scroll_frame.pack(fill="both", expand=True)

vertical_scroll_frame._scrollbar.configure(height=0)###

products_selected_label_var = ctk.StringVar(value="Products:\n∙ ")
products_selected_label = ctk.CTkLabel(master=horizontal_scroll_frame, textvariable=products_selected_label_var, justify="left")
products_selected_label.pack()

#delete most recently added product
def clear_products_list():
    opt_products_list.pop()
    update_products_label()

clear_prod_button = ctk.CTkButton(master=frame, text="x", border_color="light blue", command=clear_products_list, width=25)
clear_prod_button.place(relx=0.925, rely=0.53, anchor=ctk.CENTER)

#ALLERGIES
"""TO DO: empty allergies_list once may csv na"""
allergies_list = []

"""
TO DO:  (insert csv containing the allergens)
"""
with open("allergens.csv", "r") as file:
    reader = csv.DictReader(file)
    for allergy in reader:
        allergies_list.append(allergy['Name'])


allergies_list.sort()

def add_allergy():
    allergy = allergies_combobox.get()
    if allergy not in opt_allergies_list:
        opt_allergies_list.append(allergy)
        update_allergies_label()
    #else display error

def update_allergies_label():
    allergies_selected_label_var.set("Allergies:\n∙ " + "\n∙ ".join(opt_allergies_list))

    allergies_vertical_scroll_frame.inner_height = allergies_selected_label.winfo_reqheight()
    allergies_horizontal_scroll_frame.inner_width = allergies_selected_label.winfo_reqwidth() 

allergies_label = ctk.CTkLabel(master=frame, text="Please specify any allergies:", font=("Arial", 13))
allergies_label.place(relx=0.328, rely=0.66, anchor=ctk.CENTER)

allergies_combobox = ctk.CTkComboBox(master=frame, values=allergies_list, width=200)
allergies_combobox.place(relx=0.35, rely=0.7, anchor=ctk.CENTER)

add_allergy_button = ctk.CTkButton(master=frame, text="Add Allergy", border_color="light blue", command=add_allergy, width=100)
add_allergy_button.place(relx=0.80, rely=0.7, anchor=ctk.CENTER)

allergies_vertical_scroll_frame = ctk.CTkScrollableFrame(master=frame, width=400, height=80, orientation="vertical", fg_color="white", border_color="light gray", border_width=2)
allergies_vertical_scroll_frame.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

allergies_horizontal_scroll_frame = ctk.CTkScrollableFrame(master=allergies_vertical_scroll_frame, orientation="horizontal", fg_color="white")
allergies_horizontal_scroll_frame.pack(fill="both", expand=True)

allergies_vertical_scroll_frame._scrollbar.configure(height=0)###

allergies_selected_label_var = ctk.StringVar(value="Allergies:\n∙ ")
allergies_selected_label = ctk.CTkLabel(master=allergies_horizontal_scroll_frame, textvariable=allergies_selected_label_var, justify="left")
allergies_selected_label.pack()

#delete most recently added product
def clear_allergies_list():
    opt_allergies_list.pop()
    update_allergies_label()

clear_allergies_button = ctk.CTkButton(master=frame, text="x", border_color="light blue", command=clear_allergies_list, width=25)
clear_allergies_button.place(relx=0.925, rely=0.76, anchor=ctk.CENTER)

##########################################
#SUBMIT
def submit():
    skin_type = str(opt_skin_type.get())
    acne = str(opt_acne.get())
    products = ", ".join(opt_products_list)
    allergies = ", ".join(opt_allergies_list)

    print("Skin type: " + skin_type + "\n" 
          + "Acne: " + acne + "\n" 
          + "Products: " + products + "\n" 
          + "Allergies: " + allergies + "\n")
    
    

    cover_frame.grid_forget()
    frame.grid_forget()
    
    result_frame.grid(row=0, column=0, padx=0, pady=0, rowspan=2, columnspan=2)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    app.geometry('1050x350')

    fill_skincare_table()#########

def go_back():
    result_frame.grid_forget()
    cover_frame.grid(row=0, column=0, padx=0, pady=0)
    frame.grid(row=0, column=1, padx=0, pady=0)
    app.geometry('900x700')
    reset_form()

def reset_form():
    opt_skin_type.set("Normal")
    opt_acne.set("No")
    brand_combobox.set(brands[0])
    allergies_combobox.set(allergies_list[0])

    opt_products_list.clear()
    opt_allergies_list.clear()

    update_products_label()
    update_allergies_label()

button = ctk.CTkButton(master=frame, text="Submit", border_color="light blue", command=submit)
button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

#RESULTS
def fill_skincare_table():
    #clear previous data
    for item in skincare_table.get_children():
        skincare_table.delete(item)

    #RECOMMENDATIONS
    moisturizer, cleanser, sunscreen = None, None, None

    moisturizer, cleanser, sunscreen = checkExisting(str(opt_skin_type.get()), opt_products_list, opt_allergies_list, str(opt_acne.get()))
    
    if not cleanser:
        cleanser = recommendation("Cleanser", opt_skin_type, opt_allergies_list, str(opt_acne.get()))

    if not moisturizer:
        moisturizer = recommendation("Moisturizer", opt_skin_type, opt_allergies_list, str(opt_acne.get()))

    if not sunscreen:
        sunscreen = recommendation("Sun protect", opt_skin_type, opt_allergies_list, "No")
        

    recommended_routine = [
    {"Brand": moisturizer["Brand"], "Product": moisturizer["Product"], "Link": moisturizer["Link"]},
    {"Brand": cleanser["Brand"], "Product": cleanser["Product"], "Link": cleanser["Link"]},
    {"Brand": sunscreen["Brand"], "Product": sunscreen["Product"], "Link": sunscreen["Link"]}
    ]
    
    for prod in recommended_routine:
        brand = prod["Brand"]
        product_name = prod["Product"]
        link = prod["Link"]
        if product_name in opt_products_list:
            skincare_table.insert("", tk.END, values=[brand, product_name, link], tags=("existing",))#highlight products that users already use?
        else:
            skincare_table.insert("", tk.END, values=[brand, product_name, link])

    skincare_table.insert("", tk.END, values=["", ""], tags=("separator",))
    
result_frame = ctk.CTkFrame(app, width=900, height=700, fg_color="#FFFFF9")

skincare_table = ttk.Treeview(result_frame, columns=("Brand", "Product", "Link"), show="headings", height=10)
skincare_table.heading("Brand", text="Brand")
skincare_table.heading("Product", text="Product")
skincare_table.heading("Link", text="Link")
skincare_table.column("Brand", width=100, anchor="center")
skincare_table.column("Product", width=500, anchor="center")
skincare_table.column("Link", width=400, anchor="center")

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="black")
style.configure("Treeview", font=("Arial", 12), background="#FFFFF9", fieldbackground="#FFFFF9", foreground="black")

skincare_table.tag_configure("separator", background="light gray")
skincare_table.tag_configure("avoid", background="#BF0013")
skincare_table.tag_configure("existing", background="#f4e470")

skincare_table.pack(pady=10)

back_button = ctk.CTkButton(master=result_frame, text="x", border_color="light blue", command=go_back, width=25)
back_button.place(relx=0.97, rely=0.1, anchor=ctk.CENTER)

app.mainloop()

