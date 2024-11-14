from menu.mainMenu import design as designPrincipal
from menu.calculateTipMenu import design as designOption1
from menu.divideAmountsMenu import design as designOption2
from menu.optionsTipMenu import design as designOptionTip1
from server.findAllTip import optionTipOne
from server.findByIdTip import optionTipThree
from server.deleteByIdTip import optionTipFour
from server.updateByIdTip import optionTipFive

from tabulate import tabulate
import keyboard

while True:
    match designPrincipal():
        case 1:
            while True:
                option = designOptionTip1()
                if (option == 1): designOption1()
                elif(option == 2): print(tabulate(optionTipOne(), headers="keys"))
                elif(option == 3): 
                    try:
                        keyboard.is_pressed('ctrl+c')
                        id = int(input("Enter the tip id which you want to consult: "))   
                        if (id < 0):
                            raise ValueError()
                        print(tabulate(optionTipThree(id), headers="keys"))
                    except ValueError as e:
                        print('Please enter an integer')
                    except KeyboardInterrupt:
                        print('''\n Don't press Ctrl+c, end the program and choose an option''')
                elif(option == 4): 
                    try:
                        keyboard.is_pressed('ctrl+c')
                        id = int(input("Enter the tip id which you want to consult: "))   
                        if (id < 0):
                            raise ValueError()
                        optionTipFour(id)
                        print("Tip succesfully deleted")
                    except ValueError as e:
                        print('Please enter an integer')
                    except KeyboardInterrupt:
                        print('''\n Don't press Ctrl+c, end the program and choose an option''')
                elif(option == 5):
                    try:
                        keyboard.is_pressed('ctrl+c')
                        id = int(input("Enter the tip id which you want to consult: "))   
                        if (id < 0):
                            raise ValueError()
                        optionTipFive(id)
                        print("Tip succesfully deleted")
                    except ValueError as e:
                        print('Please enter an integer')
                    except KeyboardInterrupt:
                        print('''\n Don't press Ctrl+c, end the program and choose an option''')

                elif (option == 6): break
        case 2:
            designOption2()
        case _:
             print('''
            =============================================
                Thanks for using tip simulation!
            =============================================
            ''')
             exit()



