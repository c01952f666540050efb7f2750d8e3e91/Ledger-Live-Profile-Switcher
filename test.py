# Imports
import argparse

# Internal Import
from lib.accounts import accounts, account_types
from lib.appjson import appjson
from lib.writer import inject_appjson, replace_appjson

# We shall use this as the testing file eventually

# How should we use this CLI tool

# Create parser object
parser = argparse.ArgumentParser(
    description="Inject addresses into app.json of Ledger Live"
)
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Boolean for verbosity for this tool for testing purposes"
) # Verbosity

# We first parse all the arguments for the options that we will have
# Create argument object
args = parser.parse_args()

# Let the user know we are being verbose
if args.verbose:
    print("Beginnging script in verbose mode.")

# We then ask the user to enter the account types and "public keys" (eg addresses or xpubs) in a loop
# Note to self - we are trying to create a finite state machine to add these accounts, essentially

# Exit boolean
continue_loop = True

# Added account list
added_accounts = []

# Begin loop
while continue_loop:

    # If this is the first run
    if len(added_accounts) == 0:
        # Print account types:
        print(account_types)
    else:
        print("Exit: (x) / Back: (b)")

    # Get address type input
    print("What address type do you want to add?")
    typed_input = input()

    # Check for exit or back inputs
    if typed_input == 'b': # Back input
        # To input code later
        pass
    elif typed_input == 'x': # Exit input
        # Raise System Exit
        raise(SystemExit())

    # Check address type is supported
    if typed_input in account_types:
        print(f"Account type blockchain")
        print("What is the address to be added?")

        # Get address
        typed_input_addr = input()

        # Append data into list of added accounts (to update)
        added_accounts.append(
            {
                typed_input: typed_input_addr
            }
        )

    


    

exit()




# Once we have everything we need, we print a confirmation with all of the addresses that we want to add in a table

# We input a selection mechanism to remove addresses if need be

# Confirm and write to file


# We have a specific address we want to inject
test_address = "0xbBEFA5eE210719D21AEAc41B0722C19624d32A5B"
test_obj = appjson()

# This creates the account
test_account = accounts("bsc", test_address)

# We then create the json
account_json = test_account.ret_account()

# Test print of the account (not full appjson)
print(account_json)
print("---"*16)

# Test print appjson
print(test_obj.return_appjson())
print("---"*16)

# Add account
test_obj.add_account(account_json)

# Test Print
print(test_obj.return_appjson())
print("---"*16)

# Inject JSON
inject_appjson(test_obj.return_appjson())
