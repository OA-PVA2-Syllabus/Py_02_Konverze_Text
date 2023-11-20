# Formátované řetězcové literály
# Formátovaný řetězcový literál neboli f-řetězec je řetězcový literál s předponou 'f' nebo 'F'.
# Tyto řetězce mohou obsahovat náhradní pole, což jsou výrazy ohraničené složenými závorkami {}.


# S částmi řetězce mimo složené závorky se zachází doslovně. Escape sekvence se dekódují stejně jako u běžných řetězcových literálů.
# Náhradní výrazy mohou obsahovat zalomení řádků (např. v řetězcích s trojitými uvozovkami), ale nemohou obsahovat komentáře.
# Každý výraz se vyhodnocuje v kontextu, ve kterém se vyskytuje formátovaný řetězcový literál, a to v pořadí zleva doprava.


# Zde je několik příkladů:
# jméno = "Fred"
# f "Řekl, že se jmenuje {jméno}."
# "Řekl, že se jmenuje Fred.
# V řetězcích f lze dělat i další vymyšlené věci, např:


# f"{jméno.lower()} je legrační."
# "Fred je vtipný.
# Další informace o formátovaných řetězcových literálech najdete v Dokumentech Pythonu.


# Zkuste si sami vytvořit f-řetězec. Zkuste také spustit kód a podívat se, co vypíše.

name = ???
age = ???
print(f"Hello, My name is ??? and I'm ??? years old.")