# This file can be run to regenerate the records in weapons.py from a csv.
import csv

weapon_data = []
with open('data/tier1-weapons.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for row in data:
    weapon_data.append('Weapon("' + '", "'.join(list(row.values())) + '", "1")')

with open('data/tier2-weapons.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for row in data:
    weapon_data.append('Weapon("' + '", "'.join(list(row.values())) + '", "2")')

with open('data/tier3-weapons.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for row in data:
    weapon_data.append('Weapon("' + '", "'.join(list(row.values())) + '", "3")')

with open('data/tier4-weapons.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for row in data:
    weapon_data.append('Weapon("' + '", "'.join(list(row.values())) + '", "4")')

armor_data = []
with open('data/armor.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for row in data:
    armor_data.append('Armor("' + '", "'.join(list(row.values())) + '")')

srd_items = []
with open('data/srd_items.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for index, row in enumerate(data):
    srd_items.append('Item("' + '", "'.join(list(row.values())) + '", ' + str(index + 1) + ')')

hf_items = []
with open('data/hf_items.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for index, row in enumerate(data):
    hf_items.append('Item("' + '", "'.join(list(row.values())) + '", ' + str(index + 1) + ')')

srd_consumables = []
with open('data/srd_consumables.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for index, row in enumerate(data):
    srd_consumables.append('Consumable("' + '", "'.join(list(row.values())) + '", ' + str(index + 1) + ')')

hf_consumables = []
with open('data/hf_consumables.csv', mode='r', encoding='utf-8') as file:
  data = csv.DictReader(file)
  for index, row in enumerate(data):
    hf_consumables.append('Consumable("' + '", "'.join(list(row.values())) + '", ' + str(index + 1) + ')')

with open('weapons.py', mode='w') as file:
  file.write('class Weapon:\n')
  file.write('  def __init__(self, name, weapon_type, damage_type, trait, range, damage, burden, feature, tier):\n')
  file.write('    self.name = name\n')
  file.write('    self.weapon_type = weapon_type\n')
  file.write('    self.damage_type = damage_type\n')
  file.write('    self.trait = trait\n')
  file.write('    self.range = range\n')
  file.write('    self.damage = damage\n')
  file.write('    self.burden = burden\n')
  file.write('    self.feature = feature\n')
  file.write('    self.tier = tier\n')
  file.write('\n')
  file.write('  def __str__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('  def details(self):\n')
  file.write('    return f"{self.name} - {self.weapon_type} {self.trait} {self.range} weapon: {self.burden} {self.damage} damage"\n')
  file.write('\n')
  file.write('WEAPONS = [\n')
  for row in weapon_data:
    file.write('  ' + row + ',\n')
  file.write(']\n')

with open('armor.py', mode='w') as file:
  file.write('class Armor:\n')
  file.write('  def __init__(self, name, tier, base_thresholds, score, feature):\n')
  file.write('    self.name = name\n')
  file.write('    self.tier = tier\n')
  file.write('    self.base_thresholds = base_thresholds\n')
  file.write('    self.score = score\n')
  file.write('    self.feature = feature\n')
  file.write('  def __str__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('ARMOR = [\n')
  for row in armor_data:
    file.write('  ' + row + ',\n')
  file.write(']\n')

with open('items.py', mode='w') as file:
  file.write('class Item:\n')
  file.write('  def __init__(self, name, description, roll):\n')
  file.write('    self.name = name\n')
  file.write('    self.description = description\n')
  file.write('    self.roll = roll\n')
  file.write('\n')
  file.write('  def __str__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('  def __repr__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('CORE_ITEMS = [\n')
  for row in srd_items:
    file.write('  ' + row + ',\n')
  file.write(']\n')
  file.write('\n')
  file.write('HF_ITEMS = [\n')
  for row in hf_items:
    file.write('  ' + row + ',\n')
  file.write(']\n')


with open('consumables.py', mode='w') as file:
  file.write('class Consumable:\n')
  file.write('  def __init__(self, name, description, roll):\n')
  file.write('    self.name = name\n')
  file.write('    self.description = description\n')
  file.write('    self.roll = roll\n')
  file.write('\n')
  file.write('  def __str__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('  def __repr__(self):\n')
  file.write('    return self.name\n')
  file.write('\n')
  file.write('CORE_CONSUMABLES = [\n')
  for row in srd_consumables:
    file.write('  ' + row + ',\n')
  file.write(']\n\n')
  file.write('HF_CONSUMABLES = [\n')
  for row in hf_consumables:
    file.write('  ' + row + ',\n')
  file.write(']\n')
