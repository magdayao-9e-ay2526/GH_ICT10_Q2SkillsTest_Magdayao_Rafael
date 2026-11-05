#Glee Club checker
from pyscript import display, document


def check_element(e):
    document.getElementById('result').innerHTML = ' '
    element = document.getElementById('symbol').value.strip().capitalize()
    #Elements:
    Element_list = {
        'H': {
            'Symbol': 'H',
            'Element': 'Hydrogen',
            'Atomic Number': '1',
            'Atomic Mass': '1.00784'
        },
        'He': {
            'Symbol': 'He',
            'Element': 'Helium',
            'Atomic Number': '2',
            'Atomic Mass': '4.0026'
        },
         'C': {
            'Symbol': 'C',
            'Element': 'Carbon',
            'Atomic Number': '6',
            'Atomic Mass': '12'
        },
         'N': {
            'Symbol': 'N',
            'Element': 'Nitrogen',
            'Atomic Number': '7',
            'Atomic Mass': '14'
        },
         'O': {
            'Symbol': 'O',
            'Element': 'Oxygen',
            'Atomic Number': '8',
            'Atomic Mass': '16'
        },
         'F': {
            'Symbol': 'F',
            'Element': 'Fluorine',
            'Atomic Number': '9',
            'Atomic Mass': '18.998'
        },
         'P': {
            'Symbol': 'P',
            'Element': 'Phosphorus',
            'Atomic Number': '15',
            'Atomic Mass': '30'
        },
         'S': {
            'Symbol': 'S',
            'Element': 'Sulfur',
            'Atomic Number': '16',
            'Atomic Mass': '32'
        },
         'Cl': {
            'Symbol': 'Cl',
            'Element': 'Chlorine',
            'Atomic Number': '17',
            'Atomic Mass': '35'
        },
         'Se': {
            'Symbol': 'Se',
            'Element': 'Selenium',
            'Atomic Number': '34',
            'Atomic Mass': '78.960'
        },
         'Br': {
            'Symbol': 'Br',
            'Element': 'Bromine',
            'Atomic Number': '35',
            'Atomic Mass': '79.904'
        },
         'I': {
            'Symbol': 'I',
            'Element': 'Iodine',
            'Atomic Number': '53',
            'Atomic Mass': '126.90'
        },
         'Ne': {
            'Symbol': 'Ne',
            'Element': 'Neon',
            'Atomic Number': '10',
            'Atomic Mass': '20.180'
        },
         'Ar': {
            'Symbol': 'Ar',
            'Element': 'Argon',
            'Atomic Number': '18',
            'Atomic Mass': '39.148'
        },
         'Kr': {
            'Symbol': 'Kr',
            'Element': 'Krypton',
            'Atomic Number': '36',
            'Atomic Mass': '83.798'
        },
         'Xe': {
            'Symbol': 'Xe',
            'Element': 'Xenon',
            'Atomic Number': '54',
            'Atomic Mass': '131.29'
        },
         'Rn': {
            'Symbol': 'Rn',
            'Element': 'Radon',
            'Atomic Number': '86',
            'Atomic Mass': '222'
        }   
    }
    checkE = element in Element_list


    display_message = (f'Element not found', f"{Element_list.get(element, [])}")
    display(display_message[checkE], target='result')