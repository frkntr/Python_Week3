def alphabetical():
    newlist = []
    while True:
        a = input("Enter word: for exit press 'q' ")
        if a != "q":
            newlist.append(a)
        else:
            break

    text = ""
    for i in sorted(newlist):
        text += i
        if i != newlist[len(newlist)-1]:
            text += "-"


    print(text)


alphabetical()

