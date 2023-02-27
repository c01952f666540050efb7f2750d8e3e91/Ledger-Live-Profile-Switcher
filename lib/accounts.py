import json

# Account based assets/networks
account_types = [
    'ethereum',
    'polygon',
    'cosmos',
    'tron',
    'bsc',
    'polkadot'
]

# UTXO based assets/networks
utxo_types = {
    'bitcoin': [
        'taproot',
        'native_segwit',
        'segwit',
        'legacy'
    ]
}

class accounts:
    def __init__(self, address_type: str = "", public_key: str = ""):
        self.address_type = address_type
        self.public_key = public_key

        if address_type not in account_types:
            # UTXO based account -> update derivation mode
            pass
        
    def ret_account(self, index:int = 0, freshAddressPath:str = "0'/0'/0'/0/0", derivationMode:str = "", starred:bool = True):
        return {
            "data": {
                "id": f"js:2:{self.address_type}:{self.public_key}:",
                "seedIdentifier": f"{self.public_key}",
                "xpub": f"{self.public_key}",
                "derivationMode": derivationMode,
                "index": index,
                "freshAddress": f"{self.public_key}",
                "freshAddressPath": freshAddressPath,
                "freshAddresses": [],
                "name": f"CS {self.address_type}",
                "starred": starred,
                "balance": "0",
                "blockHeight": 0,
                "currencyId": f"{self.address_type}",
                "operations": [],
                "pendingOperations": [],
                "swapHistory": [],
                "unitMagnitude": 0,
                "lastSyncDate": "0"
            }
        }