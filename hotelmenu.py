# Let's start our first mini python project:-
menu={
    "pizza": 800,
    "pasta":700,
    "macroni":200,
    "biryani":250,
    "manchoriyan":300,
    "daalchawal":250,
    "cocacola":150,
    "7UP":140
}

print("WellCome to the Restaurant")
print("Our Menu offers a variety of Delicious Dishes:")
print("Pizza:800\nPasta:700\nMacroni:200")
print("Biryani:250\nManchoriyan:300\nDaal-Chawal:250\nCoca-Cola:150\n7UP:140")

ORDER_TOTAL = 0

item_1 = input("Enter the Name of Item you want to Order = ")
if item_1 in menu:
    ORDER_TOTAL = ORDER_TOTAL + menu[item_1]
    print(f"Your Item {item_1} has been added to your Order")
else:
    print(f"Your Ordered Item {item_1} is not available yet")

Another_item = input("Do you want to add another item? (Yes/No)")
if Another_item=="Yes":
    item_2 = input("Enter the Name of Another Item you want to Order = ")
    if item_2 in menu:
        ORDER_TOTAL = ORDER_TOTAL + menu[item_2]
        print(f"Your Item {item_2} has been added to your Order")
    else:
        print(f"Your Ordered Item {item_2} is not available yet")

Another_item2 = input("Do you want to add another item? (Yes/No)")
if Another_item2=="Yes":
    item_3 = input("Enter the Name of Another Item you want to Order = ")
    if item_3 in menu:
        ORDER_TOTAL = ORDER_TOTAL + menu[item_3]
        print(f"Your Item {item_3} has been added to your Order")
    else:
        print(f"Your Ordered Item {item_3} is not available yet")

print(f"The Total Amount of Items to pay is {ORDER_TOTAL}")