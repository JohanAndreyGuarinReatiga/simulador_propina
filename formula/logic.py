def calculate_tip(total, percentage):
    decimal = percentage / 100
    tip = decimal * total
    return tip

def calculate_all_w_tip(total, tip):
    return total + tip

def divide_total(total, personas):
    return total / personas