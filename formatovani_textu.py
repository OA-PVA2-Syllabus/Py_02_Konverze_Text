# Formátování řetězců
# Operátor % za řetězcem slouží ke spojení řetězce s proměnnými. Operátor % nahradí %s v řetězci řetězcovou proměnnou, která následuje za ním.
# Speciální symbol %d se používá jako zástupný symbol pro číselné nebo desetinné hodnoty.

# Poznámka: Zde popsané formátovací operace vykazují řadu zvláštností, které vedou k řadě častých chyb.
# Těmto chybám může pomoci vyhnout se používání novějších formátovaných řetězcových literálů (viz dále), rozhraní str.format() nebo šablon řetězců.
# Každá z těchto alternativ poskytuje vlastní kompromisy a výhody v podobě jednoduchosti, flexibility a/nebo rozšiřitelnosti.

# Řekněte programu, kolik je vám let (pomocí číslic).

name = "John"
# Note: %s is inside the string, % is after the string.
print("Hello, PyCharm! My name is %s!" % name)

print("I'm ??? years old" '???')