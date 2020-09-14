def bubblesort(number,vari):
    global  actions
    actions = 0
    numberoftries = 0
    for p in range (1,number):
        if (numberoftries == number-2):
            break
        numberoftries = 0
        for cords in range(0, len(vari)):
            try:
                actions += 1
                first = varaibles[cords]
                second = varaibles[cords+1]
                firstx = first.x
                secondx  = second.x
                if(first.x > second.x):
                    first.x = secondx
                    second.x = firstx

                else:

                    if (numberoftries == number-2):
                        break
                    numberoftries +=1

            except:
                break
    print(actions)