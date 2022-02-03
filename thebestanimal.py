while True:
    from random import random
    cat = value = random()
    dog = value = random()
    threshold = 0.25
    monkey = value = random()

    if abs(cat - dog) > monkey:
        print("actually monkeys are the best")
    
    if not abs(cat - dog) > monkey:
        if abs(cat - dog) >= threshold and cat > dog:
            print("monkey is better than monkey")
    
        if abs(cat - dog) >= threshold and cat < dog:
            print("monkey is better than monkey")
    
        if abs(cat - dog) < threshold:
            print("they are equally good")
    cont = input("Another one? yes/no > ")
    while cont.lower() not in ("yes","no"):
        cont = input("Another one? yes/no > ")
    if cont == "no":
        break
