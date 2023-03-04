# Imports
import os

# Local Imports
from lib.support import account_types, utxo_types

# Main printing function
def printer(input_data:dict, verbose:bool=True):
    # Windows Clear
    os.system("cls")

    if verbose: # If verbose
        print("---"*32) # Initial Split
        
        # If we have some accounts added
        if len(input_data['added_accounts']) > 0:
            # Print added accounts
            print("Added accounts: ")
            print(input_data['added_accounts'])
            print("---"*32)

    else:
        print("---"*32) # Initial Split
    
    # Print account types
    print("Possible Account Types:")
    print(account_types)
    print(utxo_types)
    print("---"*32) # Final Split