# Imports
import argparse

# Internal Import
from lib.accounts import accounts
from lib.appjson import appjson
from lib.writer import inject_appjson
from lib.listener import get_acc_data

# Create parser object
parser = argparse.ArgumentParser(
    description="Inject addresses into app.json of Ledger Live"
)

# Verbosity
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Boolean for verbosity for this tool for testing purposes",
    required=False
)

# Argument object
args = parser.parse_args()
verbosity = False
if args.verbose:
    verbosity = True


# How should we use this CLI tool
json_obj = appjson()

# Get account data
acc_data = get_acc_data(verbose=verbosity)

# For each account
for account in acc_data:
    # Create account dict
    acc = accounts(account['acc_type'], account['address']).ret_account()

    # Add to app.json
    json_obj.add_account(acc)

# Injet appjson
inject_appjson(json_obj.return_appjson())