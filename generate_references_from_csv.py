# This file can be run to regenerate the records in weapons.py from a csv.
import csv

data = []
with open('csv_data/tier1-weapons.csv', mode='r', encoding='utf-8') as file:
  csv_data = csv.DictReader(file)
  for row in csv_data:
    data.append('Weapon("' + '", "'.join(list(row.values())) + '", 1)')

with open('csv_data/tier2-weapons.csv', mode='r', encoding='utf-8') as file:
  csv_data = csv.DictReader(file)
  for row in csv_data:
    data.append('Weapon("' + '", "'.join(list(row.values())) + '", 2)')

with open('csv_data/tier3-weapons.csv', mode='r', encoding='utf-8') as file:
  csv_data = csv.DictReader(file)
  for row in csv_data:
    data.append('Weapon("' + '", "'.join(list(row.values())) + '", 3)')

with open('csv_data/tier4-weapons.csv', mode='r', encoding='utf-8') as file:
  csv_data = csv.DictReader(file)
  for row in csv_data:
    data.append('Weapon("' + '", "'.join(list(row.values())) + '", 4)')

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
  file.write('WEAPONS = [\n')
  for row in data:
    file.write('  ' + row + ',\n')
  file.write(']\n')