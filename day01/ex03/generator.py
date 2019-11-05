from random import shuffle

def generator(text, sep=" ", option = None):
    split = text.split(sep)

    if option is "shuffle":
        shuffle(split)
    elif option is "unique":
        split = set(split)
    elif option is "ordered":
        split.sort(key=str.lower)
    elif option is not None or not isinstance(text, str):
        print("ERROR")
        exit()

    for word in split:
        yield word


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)
