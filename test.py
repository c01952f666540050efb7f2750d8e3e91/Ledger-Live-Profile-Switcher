# Imports
import argparse

# Internal Import
from lib.accounts import accounts
from lib.appjson import appjson
from lib.writer import inject_appjson, replace_appjson
from lib.printer import printer
from lib.support import account_types
from lib.listener import get_acc_data

# We shall use this as the testing file eventually
# Cobie - Ethereum - 0x676aecc97bf721c3cb3329a22d49c0ea0ed375f7
# GCR - Ethereum / Polygon / BSC - 0x25599b4c5d678299680c84f904001aa7661d77f7
# A16Z - Polygon / Ethereum / Moonriver / Optimism - 0x293ed38530005620e4b28600f196a97e1125daac
# Alameda - Ethereum / Moonbeam / Moonriver / Arbitrum - 0xe5d0ef77aed07c302634dc370537126a2cd26590
# Wintermute - Ethereum / Optimism / Fantom / Songbird - 0xdbf5e9c5206d0db70a90108bf936da60221dc080

# How should we use this CLI tool

# Create parser object
parser = argparse.ArgumentParser(
    description="Inject addresses into app.json of Ledger Live"
)

# Address type
parser.add_argument(
    "--type",
    required=False,
    help="The address type",
)

# Address / public key
parser.add_argument(
    "--address",
    required=False,
    help="The address/extended public key you want to add"
)

# CLI mode argument - to enter multiple addresses
parser.add_argument(
    "--cli",
    required=False,
    help="Run in CLI mode to add multiple addresses"
) 

# Verbosity argument
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Boolean for verbosity for this tool for testing purposes",
    required=False
)

# We first parse all the arguments for the options that we will have
# Create argument object
args = parser.parse_args()

# Let the user know we are being verbose
if args.verbose:
    print("Beginnging script in verbose mode.")


# We then ask the user to enter the account types and "public keys" (eg addresses or xpubs) in a loop
# Note to self - we are trying to create a finite state machine to add these accounts, essentially

# Added account list
added_accounts = []

# Begin loop
while True:

    # Call printer function
    printer(
        {
            'added_accounts': added_accounts
        },
        verbose=args.verbose
    )

    # Get address type input
    acc_data = get_acc_data()
    print()
    typed_input = input("> ")

    # Check for exit or back inputs
    if typed_input == 'b': # Back input
        # To input code later
        pass
    elif typed_input == 'x': # Exit program
        # Raise System Exit
        raise(SystemExit())
    elif typed_input == 'c': # Complete
        break

    # Check address type is supported
    if typed_input in account_types:
        print(f"Account type blockchain")
        print("What is the address to be added?")

        # Get address
        typed_input_addr = input()

        # Test print
        print(f"Adding...")
        print(f"{typed_input} // {typed_input_addr}")

        # Append data into list of added accounts (to update)
        added_accounts.append(
            {
                typed_input: typed_input_addr
            }
        )

for account in added_accounts:
    
    

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
