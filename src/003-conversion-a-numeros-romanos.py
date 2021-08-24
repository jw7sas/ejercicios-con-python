""" 
    NUMEROS ROMANOS
    // NÚMEROS EN TIPIFICACIÓN INICIAL [NBASE_INICIAL]
        "I"  - Unidad - 1       - posicion: 0           
        "X"  - Decena - 10      - posicion: 1 
        "C"  - Centena - 100    - posicion: 2
        "M"  - Miles - 1000     - posicion: 3
    // NÚMEROS EN TIPIFICACIÓN MEDIA [NBASE_MEDIO]
        "V"  - Unidad - 5       - posicion: 0
        "L"  - Decena - 50      - posicion: 1
        "D"  - Centena - 500    - posicion: 2
        "V+" - Miles - 5000     - posicion: 3

    // position = [Unidad, Decena, Centena, Miles]
    EJ: 1546
        1000 -> Miles   ->    posicion 3    -> M
         500 -> Centena ->    posicion 2    -> D
          40 -> Decena  ->    posicion 1    -> XL
           6 -> Unidad  ->    posicion 0    -> VI
        
        1546 == MDXLVI
        
    // REGLAS

    (num > 0 and num <= 3) ENTONCES: 
        FORMULA: NBASE_INICIAL[position] * num  
        Ej: 30 = XXX || Ej: 3 = III

    (num = 4) ENTONCES:
        FORMULA: NBASE_INICIAL[position] + NBASE_MEDIO[position]  
        Ej: 400 = CD || Ej: 4 = IV

    (num = 5) ENTONCES:  
        FORMULA: NBASE_MEDIO[position]
        Ej: 5 = V || Ej: 50 L

    (num > 5 and num <= 8) ENTONCES:
        FORMULA: NBASE_MEDIO[position] + (NBASE_INICIAL[position] * (num - 5))
        Ej: 8 = VIII  || Ej: 17 = XVII 

    (num == 9) ENTONCES: 
        FORMULA: NBASE_INICIAL[position] + NBASE_INICIAL[(position) + 1]
        Ej: 9 = IX || Ej: 1900 = MCM

"""

INITIAL_ROMAN_NUMERALS = ["I", "X", "C", "M"]
HALF_ROMAN_NUMERALS = ["V", "L", "D", "V+"]

def getNumber(number, position):
    if number > 0 and number <= 3:
        return INITIAL_ROMAN_NUMERALS[position] * number 

    if number == 4:
        return INITIAL_ROMAN_NUMERALS[position] + HALF_ROMAN_NUMERALS[position] 
    
    if number == 5:
        return HALF_ROMAN_NUMERALS[position] 
    
    if number > 5 and number <= 8:
        return HALF_ROMAN_NUMERALS[position] + (INITIAL_ROMAN_NUMERALS[position] * (number - 5))
    
    if number == 9:
        return INITIAL_ROMAN_NUMERALS[position] + INITIAL_ROMAN_NUMERALS[(position) + 1]

    return ""

def arabicToRoman(number):
    list_of_parts = list(str(number))

    roman_numeral = ""
    counter = len(list_of_parts) - 1
    for num in list_of_parts:
        # print(f"Contador: {counter} - Numero: {num}")
        roman_numeral += str(getNumber(int(num), counter))
        counter -=1

    return roman_numeral


def run():
    try:
        while True:
            number = int(input("Ingrese el número: "))
            if number >= 10000 or number < 0:
                print("Error en la cantidad \n")
                break

            print(arabicToRoman(number) + "\n")

    except ValueError as e:
        print("Número no valido")

if __name__ ==  "__main__":
    run()

