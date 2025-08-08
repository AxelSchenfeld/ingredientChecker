recipe_cake_ingredients = {"azucar", "harina", "huevos", "miel", "leche", "vanilla"}

i = ""
user_ingredients = set()

while i != "n":
    ingredient = input("ingrese uno de los ingredientes que tiene: ")
    user_ingredients.add(ingredient)
    i = input("¿desea agregar otro ingrediente? (s/n)")

missing_ingredients = recipe_cake_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_cake_ingredients
total_ingredients = recipe_cake_ingredients | user_ingredients


print ("\n ------ comprobacion de ingredientes ------")

if missing_ingredients:
    print("faltan los siguientes ingredientes: ", ", ".join(missing_ingredients))
else:
    print("usted tiene todos los ingredientes")

if extra_ingredients:
    print("usted tiene los siguientes ingredientes extra: ", ", ".join(extra_ingredients))
else:
    print("usted no tiene ingredientes extra")

print("usted tiene los siguientes ingredientes: ", ", ".join(total_ingredients))
