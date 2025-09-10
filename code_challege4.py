print("Welcome to Manga reader Recomender📖")
print("Answer a few question to find your next read🕵️")
ch = input("Choose genre would you like to choose: (Action, Romance, Horror, Drama)")

if ch == 'Action':
    n1 = input("How lng would the manga be? (short, medium, long)")
    if n1 == 'short':
        n2 = input("Which decade? (2000s, 2010s)")
        if n2 == '2000s':
            print("We recomended: Girls' Last Tour")
        elif n2 == '2010s':
            print("We recomended: Kaiju")
    elif n1 == 'medium':
        n3 = input("Which decade? (2000s, 2010s)")
        if n3 == '2000s':
            print("We recomended: Golgo 13")
        elif n3 == '2010s':
            print("We recomended: Hajime ippo")
    elif n1 == 'long':
        n4 = input("Which decade? (2000s, 2010s)")
        if n4 == '2000s':
            print("We recomended: Naruto")
        elif n4 == '2010s':
            print("We recomended: One piece")
elif ch == 'Romance':
    n5 = input("How lng would the manga be? (short, medium, long)")
    if n5 == 'short':
        n6 = input("Which decade? (2000s, 2010s)")
        if n6 == '2000s':
            print("We recomended: After the Rain is About Rekindled Love & Hope")
        if n6 == '2010s':
            print("We recomended: A Silent Voice")
    elif n5 == 'medium':
        n7 = input("Which decade? (2000s, 2010s)")
        if n7 == '2000s':
            print("We recomended: Special A")
        elif n7 == '2010s':
            print("We recomended: Electric Daisy 1")
    elif n5 == 'long':
        n8 = input("Which decade? (2000s, 2010s)")
        if n8 == '2000s':
            print("We recomended: Glass Mask")
        elif n8 == '2010s':
            print("We recomended: Skip Beat")
elif ch == 'Horror':
    n9 = input("How lng would the manga be? (short, medium, long)")
    if n9 == 'short':
        n10 = input("Which decade? (2000s, 2010s)")
        if n10 == '2000s':
            print("We recomended: REMINA")
        if n10 == '2010s':
            print("We recomended: Mieruko chan")
    elif n9 == 'medium':
        n11 = input("Which decade? (2000s, 2010s)")
        if n11 == '2000s':
            print("We recomended: Uzumaki")
        elif n11 == '2010s':
            print("We recomended: Tokyo Ghoul")
    elif n9 == 'long':
        n12 = input("Which decade? (2000s, 2010s)")
        if n12 == '2000s':
            print("We recomended: Blame!")
        elif n12 == '2010s':
            print("We recomended: Dorohedoro")
elif ch == 'Drama':
    n13 = input("How lng would the manga be? (short, medium, long)")
    if n13 == 'short':
        n14 = input("Which decade? (2000s, 2010s)")
        if n14 == '2000s':
            print("We recomended: Wolf Children")
        if n14 == '2010s':
            print("We recomended: Solanin")
    elif n13 == 'medium':
        n15 = input("Which decade? (2000s, 2010s)")
        if n15 == '2000s':
            print("We recomended: JoJo's Bizarre Adventure")
        elif n15 == '2010s':
            print("We recomended: Beserk")
    elif n13 == 'long':
        n16 = input("Which decade? (2000s, 2010s)")
        if n16 == '2000s':
            print("We recomended: DEtective Conan")
        elif n16 == '2010s':
            print("We recomended: AOT")

