# Imports
import argparse

# Internal Import
from lib.accounts import accounts
from lib.appjson import appjson
from lib.writer import inject_appjson, restore_appjson
from lib.listener import get_acc_data

# Create parser object
parser = argparse.ArgumentParser(
    description="Inject addresses into app.json of Ledger Live"
)

# Verbosity
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Boolean for verbosity for this tool.",
    required=False
)

# Test mode - to print json
parser.add_argument(
    "--test",
    action="store_true",
    help="Flag to not write and only print final output for testing purposes",
    required=False
)

parser.add_argument(
    "--restore",
    action="store_true",
    help="Flag to restore files back to appjson you were using before.",
    required=False
)

# Argument object
args = parser.parse_args()
verbosity = False
if args.verbose:
    verbosity = True

# If we're restoring from copy_of_app.json
if args.restore:
    restore_appjson()
else:
    # How should we use this CLI tool
    json_obj = appjson()

    # Get account data
    acc_data = get_acc_data(verbose=verbosity)

    # For each account
    for account in acc_data:
        # Create account dict
        acc = accounts(account['acc_type'], account['address']).ret_account(
            derivationMode=account['utxo_type']
        )

        # Add to app.json
        json_obj.add_account(acc)

    # Injet appjson
    if args.test:
        print(json_obj.return_appjson())
    else:    
        inject_appjson(json_obj.return_appjson())