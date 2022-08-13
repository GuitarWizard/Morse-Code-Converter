# Morse Code converter

alphabet = {
    "A": "*- ",
    "B": "-*** ",
    "C": "-*-* ",
    "D": "-** ",
    "E": "* ",
    "F": "**-* ",
    "G": "**** ",
    "H": "**** ",
    "I": "** ",
    "J": "*--- ",
    "K": "-*- ",
    "L": "*-** ",
    "M": "-- ",
    "N": "-* ",
    "O": "--- ",
    "P": "*--* ",
    "Q": "--*- ",
    "R": "*-* ",
    "S": "*** ",
    "T": "- ",
    "U": "**- ",
    "V": "***- ",
    "W": "*-- ",
    "X": "-**- ",
    "Y": "-*-- ",
    "Z": "--** ",
    "1": "*--- ",
    "2": "**--- ",
    "3": "***-- ",
    "4": "****- ",
    "5": "***** ",
    "6": "-**** ",
    "7": "--*** ",
    "8": "---** ",
    "9": "----* ",
    "0": "----- "
}

message = input("Enter the message to be converted\n").upper()

print(message)
message=message.replace(" ","")
message_list = []
for letter in message:
    if letter in alphabet:
        message_list.append(letter)
    else:
        pass

morse_list = []
output = ""
for letter in message_list:
    morse_list.append(alphabet[letter])
    output += alphabet[letter]

print(f"converted message\n {output}")
