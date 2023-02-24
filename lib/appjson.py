from lib.accounts import accounts

class appjson:
    def __init__(self):
        self.file = {
            "data": {
                "settings": {
                    "hasCompletedOnboarding": True
                },
                "user": {
                    "id": "_"
                },
                "accounts": []
            }
        }

    def test_ret_appjson(self, account_object:dict):
        # print(account_object)
        self.file['data']['accounts'].append(account_object)
        
        return self.file