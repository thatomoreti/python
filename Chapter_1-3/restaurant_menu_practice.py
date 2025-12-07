menu=['Kota','Chips','Loaf-Bite','Pap & Wors','Chakalaka'];
print(f"Hiya boss, these are the foods currently sold by the restaurant:{menu}")

print(f"We'll add more sir!")
menu.insert(0,"Bobotie")
print(f"Here is the updated menu for food sold currently sold by the restaurant:{menu}")

print(f"More? Yes sir!")
menu.append("Mala le Mogodu")
print(f"Here is the updated menu for food sold currently sold by the restaurant:{menu}")

print("Chakalaka is not sellig ?? We'll remove it")
menu[5]="Chicken Stew"

print("We don't actually have the budget for all of it ? Ok I'll remove some of the food")
off_menu=menu.pop(3)
print(f"We removed {off_menu}, too many ingredients needed")
print(f"Here is the updated menu for food sold currently sold by the restaurant:{menu}")

print(f"Not enough? ok sir!")
del menu[2]

print(f"Here is the final menu for food sold currently sold by the restaurant:{menu}")