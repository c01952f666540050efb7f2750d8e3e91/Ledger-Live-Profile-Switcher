# Local Imports
from support import account_types, utxo_types

def validate_addr_type(input_type):
    if input_type in account_types or input_type in utxo_types.keys():
        return True
    else:
        return False
    
# ENUM potential options?
options = {
    'address_types': validate_addr_type
}

# Listen for answer
def listen(min_text:str="") -> str:
    input_data = input(f"{min_text}> ")

    # If we get an "x"
    if input_data == "x":

        # Panic exit
        raise(SystemExit())
    
    # Return data
    return input_data

def validate(input_data:str, verbose:bool=True, can_complete:bool=False):
    if verbose:
        print("Validating...")


    

# Ask a question
def ask(question_type:str, question:str="", verbose:bool=True, can_complete:bool=False) -> str:

    if verbose: # If we're verbose

        # Print the question
        print(question)

        # And await the answer
        ret_data = listen()
    else: # If we're not verbose
        
        # wait for answer with minimal data
        ret_data = listen(question_type)

    # Return data
    return ret_data




def get_acc_data(verbose:bool=True) -> list:
    ret_data = []

    while True:
        input_addr_type = ask(
            "address_type",
            "What address type do you want to add?",
            verbose=verbose
        )

        input_addr = ask(
            "address",
            "What is the address?",
            verbose=verbose
        )
        
        ret_data.append({input_addr_type,input_addr})

    
