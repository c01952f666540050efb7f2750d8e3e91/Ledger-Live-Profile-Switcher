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

    # Just add an account
    def add_account(self, account_object:dict):
        # Append account to account list
        self.file['data']['accounts'].append(account_object)

    def return_accountnumber(self):
        return len(self.file['data']['accounts'])
    
    def return_appjson(self):
        return self.file

    def test_ret_appjson(self, account_object:dict):
        # print(account_object)
        self.file['data']['accounts'].append(account_object)
        
        return self.file