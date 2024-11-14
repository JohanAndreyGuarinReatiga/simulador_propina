def calcular_propina(total, percentage):
    decimal = percentage / 100
    tip = decimal * total
    return tip

def calcular_total_con_propina(total, tip):
    return total + tip

def dividir_total(total, personas):
    return total / personas