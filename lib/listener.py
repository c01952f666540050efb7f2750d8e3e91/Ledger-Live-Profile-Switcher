# Imports

# Local Imports
from lib.support import account_types, utxo_types
from lib.printer import printer

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

    return ret_data

def command_check(command:str):
    if command == "x":
        raise(SystemExit())
    elif command == "c":
        return False
    elif command == "m":
        return True


def valid_addr_type(address_type:str, verbose:bool=True) -> bool:
    if address_type in account_types or address_type in utxo_types:
        return True
    else:
        if verbose:
            print("Invalid address type!")
        return False

def valid_addr(address:str, verbose:bool=True) -> bool:
    # Currently passes all strings as valid
    return True
    
def ask_loop(validate_func, variable:str="", question:str="", verbose:bool=True) -> str:
    # Get address type
    while True:
        input_str = ask(
            variable,
            question,
            verbose=verbose
        )

        # If the input is valid
        if validate_func(input_str, verbose=verbose):
            #Continue to next step
            break
    
    return input_str

def get_acc_data(verbose:bool=True) -> list:
    ret_data = []
    cont_loop = True

    while cont_loop:
        printer(
            {
                'added_accounts': ret_data
            },
            verbose=verbose
        )

        # Get address type
        addr_type = ask_loop(
            valid_addr_type,
            "address_type",
            "What address type do you want to add?",
            verbose=verbose
        )

        # Do validation loop
        addr = ask_loop(
            valid_addr,
            "address",
            f"What {addr_type} address do you want to add?",
            verbose=verbose
        )


        # Add to list
        ret_data.append(
            {
                'acc_type': addr_type,
                'address': addr
            }
        )

        cont_loop = command_check(
            ask(
                "",
                "More Accounts (m) / Exit: (x) / Complete (c)",
                True
            ).lower()
        )

    return ret_data

    
