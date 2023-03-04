# Imports

# Local Imports
from lib.support import account_types, utxo_types

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

    
    # Return data
    return input_data

def validate_addr(input_addr:str, verbose:bool=True):
    if verbose:
        print("Validating...")


# Ask a question
def ask(variable:str="", question:str="", verbose:bool=True) -> str:

    if verbose: # If we're verbose

        # Print the question
        print(question)

        # And await the answer
        ret_data = input(f"{variable}> ")

    else: # If we're not verbose

        # wait for answer with minimal data
        ret_data = input(f"{variable}> ")

    # # If we get an "x"
    # if ret_data == "x":

    #     # Panic exit
    #     raise(SystemExit())
    
    # Return data
    return ret_data

def command_check(command:str):
    pass

def process_command(comamand:str):
    pass


def valid_addr_type(address_type:str, verbose:bool=True) -> bool:
    if address_type in account_types or address_type in utxo_types:
        return True
    else:
        if verbose:
            print("Invalid address type!")
        return False
    
def valid_addr(address:str) -> bool:
    # Currently passes all strings as valid
    return True
    
def ask_loop(validate_func, variable:str="", question:str="", verbose:bool=True) -> str:
    # Get address type
    while True:
        input_addr_type = ask(
            variable,
            question,
            verbose=verbose
        )

        # If the address is valid
        if validate_func(input_addr_type, verbose):
            # Vald address -> continue to next step
            break
    
    return input_addr_type

def get_acc_data(verbose:bool=True) -> list:
    ret_data = []

    while True:
        addr_type = ask_loop(
            valid_addr_type,
            "address_type",
            "What address type do you want to add?",
            verbose=verbose
        )

        addr = ask_loop(
            valid_addr,
            "address",
            f"What {addr_type} address do you want to add?",
            verbose=verbose
        )
        


        ret_data.append({input_addr_type,input_addr})

    
