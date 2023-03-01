# Imports
import os

# Local Imports
from lib.support import account_types, utxo_types

# Main printing function
def printer(input_data:dict, verbose:bool=True):
    # Windows Clear
    os.system("cls")

    if verbose: # If verbose
        print("---"*32)

        if len(input_data['added_accounts']) > 0:
            print(input_data['added_accounts'])
            print("---"*32)

        print("Account types:")
        print(account_types)
        print(utxo_types)
        print("---"*32)
    else:
        print("---"*32)
    
    
    print("Exit: (x) / Back: (b) / Complete (c)")