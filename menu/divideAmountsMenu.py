from formula.logic import calculate_tip, calculate_all_w_tip, divide_total
import os
import keyboard

def design():
    opcion = 1
    while opcion:
        print(f"""
        =============================================
                  Divide Count Between Persons
        =============================================""")
        try:
            keyboard.is_pressed('ctrl+c')
            total = int(input("\tEnter the total of the count: $"))
            if(total < 0):
                raise ValueError()
            percentage = int(input("\tEnter the tip percentage (for example: 10, 15, 20): "))
            if(percentage < 0):
                raise ValueError()
            persons = int(input("\tEnter the ammount of persons : "))
            if(persons < 0):
                raise ValueError()
            tip = calculate_tip(total, percentage)
            totalWithTip = calculate_all_w_tip(total, tip)
            print(f"""
            =============================================
            The calculated tip is: ${tip}
            The total to pay is: ${totalWithTip}
            Amount per person: ${divide_total(totalWithTip, persons)}
            =============================================""")
            opcion = int(input('Do you wish to calculate it again? (1 - S/0 - N): ')) 
            os.system('clear')
        except ValueError as e:
            print('Please enter an integer')
        except KeyboardInterrupt:
            print('''\n Don't press Ctrl+c, end the program and choose an option''')