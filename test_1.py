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


# Added account list
added_accounts = []

# Call printer function
printer(
    {
        'added_accounts': added_accounts
    },
    verbose=True,
    comp_stage=False
)

# Ask loop
acc_data = get_acc_data()

# # Begin loop
# while True:

#     # Call printer function
#     printer(
#         {
#             'added_accounts': added_accounts
#         },
#         verbose=True
#     )

#     # Get address type input
#     acc_data = get_acc_data()
#     print()
#     typed_input = input("> ")

#     # Check for exit or back inputs
#     if typed_input == 'b': # Back input
#         # To input code later
#         pass
#     elif typed_input == 'x': # Exit program
#         # Raise System Exit
#         raise(SystemExit())
#     elif typed_input == 'c': # Complete
#         break

#     # Check address type is supported
#     if typed_input in account_types:
#         print(f"Account type blockchain")
#         print("What is the address to be added?")

#         # Get address
#         typed_input_addr = input()

#         # Test print
#         print(f"Adding...")
#         print(f"{typed_input} // {typed_input_addr}")

#         # Append data into list of added accounts (to update)
#         added_accounts.append(
#             {
#                 typed_input: typed_input_addr
#             }
#         )

# for account in added_accounts:
#     print(account)
    

# exit()

