from formula.logic import calcular_propina, calcular_total_con_propina
from server.saveTip import saveTip
import os
import keyboard

def design():
    while True:
        print('''
        =============================================
                        Tip calculation
        =============================================''')
        try:
            keyboard.is_pressed('ctrl+c')
            total = float(input('Write the total on the count: $'))
            if total < 0:
                raise ValueError()
            percentage = int(input('Write the tip percentage (for example: 10, 15, 20):  % '))
            if(percentage < 0):
                raise ValueError()
            tip = calcular_propina(total, percentage)
            totalPay = calcular_total_con_propina(total, tip)
            print(f'''
            =============================================
            The tip is: $ {tip}
            The total with the tip is: $ {totalPay}
            =============================================''')
            saveTip({'ammount': total, 'tip': tip, 'total to pay': totalPay, 'percentage': percentage})
            option = int(input('Do you wish to calculate it again? (1 - S/0 - N): ')) 
            if (option == 0): return None
            os.system('clear')
        except ValueError as e:
            print('Please enter an integer')
        except KeyboardInterrupt:
            print('''\n Don't press Ctrl+c, end the program and choose an option''')