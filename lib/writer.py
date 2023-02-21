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
    # Copy the file app.json and replace it with copy_of_app.json
    shutil.copy(f"{windows_filepath}\\app.json", f"{windows_filepath}\\copy_of_app.json")

def appjson_exists():
    file_list = os.listdir(f"{windows_filepath}")
    if "app.json" in file_list:
        return True
    else:
        return False