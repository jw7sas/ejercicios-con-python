class CustomMessage():
    """ Clase para el menejo de mensajes. """

    LETTER_BY_NUMBERS = {
        'I': '1',
        'E': '3',
        'T': '7',
        'O': '0',
        'A': '4',
        'S': '5',
        'B': '8',
    }

    def __init__(self, message):
        """ Constructor. """
        self.message = message


    def return_letter_associated_with_umber(self, letter):
        """ Método para verificar si una letra tiene asociado un número. """
        l = letter.upper()
        if l in self.LETTER_BY_NUMBERS:
            return self.LETTER_BY_NUMBERS[l]
        else:
            return l


    def substitute_letters_by_numbers(self):
        """ Método para convertir un mensaje a un mensaje combinado con números. """
        words = self.message.split(" ")
        new_message = []

        for word in words:
            new_word = ''
            for letter in word:
                new_word += self.return_letter_associated_with_umber(letter)

            new_message.append(new_word)
        
        return ' '.join(new_message)




def start():
    """ Método para iniciar el proceso de conversión de letras a números. """
    message = str(input("Escribe tu mensaje: "))
    m = CustomMessage(message)
    new_message = m.substitute_letters_by_numbers()
    print("<------------------------------------------------->")
    print(new_message)
    print("<------------------------------------------------->")


if __name__ == '__main__':
    start()


