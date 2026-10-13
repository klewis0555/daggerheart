# Generic functions to help with sorting / randomization
from armor import *
from consumables import *
from items import *
from weapons import *

from prettytable import PrettyTable
from random import randint

# BASIC ARMOR TABLE
def armor_table(tier: str | None = None):
  alist = []
  atable = PrettyTable()

  default_tier = ['1','2','3','4']
  if tier not in default_tier:
    tier = None
  
  tier_parameter = tier or default_tier
  atable.field_names = ["Name", "Threshold", "Score", "Feature"]
  atable.align["Feature"] = 'l'
  atable.max_width["Feature"] = 150
  for item in ARMOR:
    if item.tier in tier_parameter:
      alist.append(item)
      atable.add_row([item.name, item.base_thresholds, item.score, item.feature])

  return alist, atable

# BASIC WEAPON TABLE
def weapon_table(
  tier: str | None = None,
  trait: str | None = None,
  dtype: str | None = None,
  wtype: str | None = None,
):
  wlist = []
  wtable = PrettyTable()

  default_tier = ['1','2','3','4']
  if tier not in default_tier:
    tier = None
  tier_parameter = tier or default_tier

  default_trait = ["Agility", "Strength", "Finesse", "Instinct", "Presence", "Knowledge"]
  if trait not in default_trait:
    trait = None
  trait_parameter = trait or default_trait

  default_dtype = ["Magical", "Physical"]
  if dtype not in default_dtype:
    dtype = None
  dtype_parameter = dtype or default_dtype

  default_wtype = ["Primary", "Secondary"]
  if wtype not in default_wtype:
    wtype = None
  wtype_parameter = wtype or default_wtype

  wtable.field_names = ["Name", "Trait", "Range", "Details", "Feature"]
  wtable.align["Feature"] = 'l'
  wtable.max_width["Feature"] = 110
  for item in WEAPONS:
    if (
      item.tier in tier_parameter
      and item.trait in trait_parameter
      and item.damage_type in dtype_parameter
      and item.weapon_type in wtype_parameter
    ):
      wlist.append(item)
      wtable.add_row([item.name, item.trait, item.range, f"T{item.tier} {item.damage_type} {item.weapon_type} Weapon", item.feature])

  return wlist, wtable

# Prints all current values for certain weapon attributes
def print_weapon_values():
  weapon_type = set()
  damage_type = set()
  trait = set()
  range = set()
  burden = set()
  tier = set()

  for item in WEAPONS:
    weapon_type.add(item.weapon_type)
    damage_type.add(item.damage_type)
    trait.add(item.trait)
    range.add(item.range)
    burden.add(item.burden)
    tier.add(item.tier)

  print(f"Weapon Types: {weapon_type}")
  print(f"Damage Types: {damage_type}")
  print(f"Traits: {trait}")
  print(f"Ranges: {range}")
  print(f"Burdens: {burden}")
  print(f"Tiers: {tier}")

# Returns a random item. Table param is either CORE or HF
def get_random_item(min: int | None = 0, max: int | None = 59, table: str | None = None):
  ITEMS = [CORE_ITEMS, HF_ITEMS]
  if (
    not isinstance(min, int)
    or min > max
    or min < 0
  ):
    min = 0
  if (
    not isinstance(max, int)
    or max < min
    or max > 59
  ):
    max = 59

  source = randint(0,1)
  if table == 'CORE':
    source = 0
  elif table == 'HF':
    source = 1

  return ITEMS[source][randint(min,max)]

def get_random_consumable(min: int | None = 0, max: int | None = 59, table: str | None = None):
  ITEMS = [CORE_CONSUMABLES, HF_CONSUMABLES]
  if (
    not isinstance(min, int)
    or min > max
    or min < 0
  ):
    min = 0
  if (
    not isinstance(max, int)
    or max < min
    or max > 59
  ):
    max = 59

  source = randint(0,1)
  if table == 'CORE':
    source = 0
  elif table == 'HF':
    source = 1

  return ITEMS[source][randint(min,max)]
