two = 2
three = 3


# Zkontrolujte, zda se proměnná two rovná three.
is_equal = two ??? three
print(f"is_equal = {is_equal}")

# Zkontrolujte, zda proměnná is_equal nemá zavádějící jméno.
is_false = is_equal is # logická hodnota pro pravdivé výroky
print(f"is_false = {is_false}")

# Zkontrolujte, zda proměnná is_false skutečně obsahuje lež.
is_true = is_false is # logická hodnota pro nepravdivé výroky
print(f"is_true = {is_true}")