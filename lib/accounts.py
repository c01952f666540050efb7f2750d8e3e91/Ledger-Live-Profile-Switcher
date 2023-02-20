import json

default_eth = {
    "id": "js:2:ethereum:0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045:",
    "seedIdentifier": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "xpub": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "derivationMode": "",
    "index": 0,
    "freshAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "freshAddressPath": "0'/0'/0'/0/0",
    "freshAddresses": [],
    "name": "CS ETH",
    "starred": True,
    "balance": "0",
    "blockHeight": 0,
    "currencyId": "ethereum",
    "operations": [],
    "pendingOperations": [],
    "swapHistory": [],
    "unitMagnitude": 0,
    "lastSyncDate": "0"
}

def ret_xpublic(address_type:str, xpublic_key:str):
    pass

def ret_account(address_type:str, address:str):
    return {
        "id": f"js:2:{address_type}:{address}:",
        "seedIdentifier": address,
        "xpub": address,
        "derivationMode": "",
        "index": 0,
        "freshAddress": {address},
        "freshAddressPath": "0'/0'/0'/0/0",
        "freshAddresses": [],
        "name": f"CS {address_type}",
        "starred": True,
        "balance": "0",
        "blockHeight": 0,
        "currencyId": address_type,
        "operations": [],
        "pendingOperations": [],
        "swapHistory": [],
        "unitMagnitude": 0,
        "lastSyncDate": "0"
    }