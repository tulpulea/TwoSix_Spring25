import argparse
import json

import requests

from RegAPI import RegAPI

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="apikeys.txt")

args = parser.parse_args()

def writeKeys(keyset):
    with open(args.file, "w") as file:
        for key in keyset:
            file.write(f"{key}\n")

print("Loading...")
with open(args.file, "r") as file:
    keys = [key.strip() for key in file]

keyset = set(keys)
if len(keyset) < len(keys):
    remove = input(f"{len(keys) - len(keyset)} duplicate keys found. Remove them? [y/n]")

    if remove.lower() == "y":
        writeKeys(keyset)

def validateKey(key):
    testURL = 'https://api.regulations.gov/v4/comments/NARA-05-0005-0002'
    with open("testRes.json", "r") as f:
        testRes = json.load(f)
    api = RegAPI(apikeys=[key])
    try:
        res = api.url(testURL).get()
        return testRes == res
    except Exception as e:
        print(f"Failed with exception {e}")
        return False

removeSet = []
for key in keyset:
    isValid = validateKey(key)
    if not isValid:
        removeInvalid = input(f"Key {key} is not valid! Remove it? [y/n]")
        if removeInvalid.lower() == "y":
            removeSet.append(key)
    else:
        print(f"[✓] {key}")

if len(removeSet) > 0:
    for key in removeSet:
        keyset.remove(key)
    writeKeys(keyset)

print(f"{len(keyset)} valid keys")
