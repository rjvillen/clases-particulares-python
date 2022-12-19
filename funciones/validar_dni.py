dni_probar = input('Introduce tu DNI: ')
def validar_dni(dni):
    'función que devuelve True si el dni input sigue un formato válido y False, si no.'
    #para empezar todos los dni tienen nueve caracteres: 8 números y una letra en mayúscula.
    dni=dni.strip()
    if len(dni)==9:
        nums,letra=dni[:8],dni[8]
        try:
            int(nums)
        except:
            return False
        return letra==letra.upper()
    else:
        return False

def validar_dni2(dni):
    'función que devuelve True si el dni input sigue un formato válido y False, si no.'
    #para empezar todos los dni tienen nueve caracteres: 8 números y una letra en mayúscula.
    dni=dni.strip()#aquí uitamos los posibles espacios en blanco que haya al principio y al final
    if len(dni)==9:
        nums,letra=dni[:8],dni[8]
        if nums.isdigit() and letra==letra.upper():
            #esta función (isdigit()) comprueba si una cadena de caracteres es un número
            #también nos aseguramos de que la letra ya está en mayúscula con ==letra.upper()
            return True
    return False
print(validar_dni(dni_probar))
