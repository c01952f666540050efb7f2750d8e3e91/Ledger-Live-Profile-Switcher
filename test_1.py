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


# Ask loop
acc_data = get_acc_data()
# print(acc_data)

inject_json = appjson()

for account in acc_data:
    acc = accounts(account['acc_type'], account['address']).ret_account()
    # print(acc)

    inject_json.add_account(acc)

# print(inject_json.return_appjson())

inject_appjson(inject_json.return_appjson())