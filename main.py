#We're going to be calculating the return percentage on rosin pressing. I got tired of googling my request.

rosinDict = {}

def get_flowerDetails():
    """Here we're gathering the details of our flower before pressing."""
    print("We're going to be gathering some info on the strain were pressing!")
    strainName = input('Strain Name: ')
    while True:
        try:
            dryWeight = float(input('How much are you pressing(enter in grams): '))
        except ValueError:
            print('Sorry, maybe I confused you...Enter the weight of dry flower in GRAMS....')
        else:
            break
    return strainName, dryWeight

def get_rosinDetails():
    """Here we're getting the details of our rosin after pressing."""
    
    print(f"Now that you've pressed {strainName} I've got a few questions regarding the rosin.")
    while True:
        try:
            rosinWeight = float(input('How much rosin did you yield(enter in grams): '))
        except ValueError:
            print('Okay, how did you fuck that up? I said grams, put the blunt down and enter the weight in GRAMS....')
        else:
            break

    rosinType = input("Please select one of the following fitting types of rosin this flower produced.\n"
                      "1 - Buddrer/Badder\n2 - Wax\n3 - Shatter\n4 - Crumble\n5 - Sauce\n6 - Sugar")
    while rosinType not in ('1', '2', '3', '4', '5', '6'):
        rosinType = input('You are just...Enter 1-6 man...: ')
    else:
        for r in rosinType:
            if r == '1':
                #Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.

                pass
            elif r == '2':
                # Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.
                pass
            elif r == '3':
                # Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.
                pass
            elif r == '4':
                # Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.
                pass
            elif r == '5':
                # Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.
                pass
            elif r == '6':
                # Here we're going to be addindg the value chosen to the Consistency key in the not yet created dict.
                pass

    rosinDesc = str(input('Rosin Description: '))
