# Imports
import json
import os
import shutil

# Constant
windows_filepath = os.getenv('APPDATA')+"\\Ledger Live\\"

def write_file(data:dict, path:str, filename: str):
    # Take the file
    with open(f"{path}/{filename}.json", "w") as outfile:

        # Write to filepath
        outfile.write(json.dumps(data))

def copy_appjson():
    pass
