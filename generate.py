"""
This script generates several files/images used throughout the documentation

Author: Redstone⁴
"""
import json
import os
from os import path

# Define paths to project that we use as reference
DATA_PACK_ROOT = path.join('..', 'Lockdown', 'src', 'Data-Pack')
RESOURCE_PACK_ROOT = path.join('..', 'Lockdown', 'src', 'Resource-Pack')

# Obtain the translation key table
with open(path.join(RESOURCE_PACK_ROOT, 'Lockdown', 'assets', 'minecraft', 'lang', 'en_us.json'), mode='r') as rf:
    translations = json.load(rf)

# Scan the item modifiers determine what pages need to exist
items = dict()
item_modifier_dir = path.join(DATA_PACK_ROOT, 'Lockdown', 'data', 'lockdown', 'item_modifier', 'item')
for item in os.listdir(item_modifier_dir):
    if not path.isfile(path.join(item_modifier_dir, item)):
        continue

    with open(path.join(item_modifier_dir, item), mode='r') as rf:
        data = json.load(rf)

    # Obtain information about item from file, including:
    # * Item model
    # * Item name translation key
    model = data[0]['components']['minecraft:item_model']
    name_key = data[0]['components']['minecraft:item_name']['translate']
    items[path.splitext(item)[0]] = {'model': model, 'name': translations[name_key]}


# Create files for every found item
FEATURES_DIR = path.join('Lockdown', 'docs', 'features')
for item, properties in items.items():
    # Create wiki page
    if not path.exists(path.join(FEATURES_DIR, item + '.md')):
        with open(path.join(FEATURES_DIR, item + '.md'), mode='w') as wf:
            wf.write(f"""\
# {properties['name']}

![{properties['name']}](item/{item}.png)

(Description)

## Crafting

![Recipe for the {properties['name'].lower()}](recipe/{item}.png)

## History



""")

    # Create texture used in wiki page


    # Print entry to paste into "Features" section of mkdocs.yml
    print(f"    - features/{item}.md")

