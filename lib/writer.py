# Imports
import json
import os
import shutil

# Constant
windows_filepath = os.getenv('APPDATA')+"\\Ledger Live\\"

def write_file(data:dict, filename: str):
    # Take the file
    with open(f"{windows_filepath}/{filename}", "w") as outfile:
        json.dump(data, outfile)

def load_json(filename:str):
    with open(f"{windows_filepath}/{filename}.json") as openfile:
        return json.load(openfile)

def write_json(data:dict):
    write_file(
        data,
        "app.json"
    )

def copy_appjson():
    # Copy the file app.json and replace it with copy_of_app.json
    shutil.copy(f"{windows_filepath}\\app.json", f"{windows_filepath}\\copy_of_app.json")

def appjson_exists():
    file_list = os.listdir(f"{windows_filepath}")
    if "app.json" in file_list:
        return True
    else:
        return False
    
def appjson_copy_exists():
    file_list = os.listdir(f"{windows_filepath}")
    if "copy_of_app.json" in file_list:
        return True
    else:
        return False
    
def inject_appjson(appjson: dict):
    # If we find the json file
    if appjson_exists:
        # backup the app.json
        copy_appjson()

        # Write json to file
        write_json(appjson)

        # Test print
        print("Completed!")
    else:
        print("Something went wrong!")

def replace_appjson():
    shutil.move(f"{windows_filepath}\\copy_of_app.json", f"{windows_filepath}\\app.json")

def restore_appjson():
    if appjson_copy_exists:
        shutil.copy(f"{windows_filepath}\\copy_of_app.json", f"{windows_filepath}\\app.json")