


x = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
y = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
firstteen = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

thislist = []
while True:
    readingNumber = int(input("pelase enter the number: "))
    for i in y:
        for a in x:
            thislist.append(i+' ' + a)


    newlist =firstteen + thislist

    print(readingNumber, '-------', newlist[readingNumber-11])
