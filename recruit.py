import pandas as pd
from amplpy import AMPL
from collections import Counter

"""
    avaliable_resources = {
    "avaliable_gold": ,
    "avaliable_honour": , 
    "avaliable_people": , 
    "avaliable_bow": ,
    "avaliable_crossbow": , 
    "avaliable_spear": , 
    "avaliable_mace": , 
    "avaliable_pike": , 
    "avaliable_sword": , 
    "avaiable_leather": , 
    "avaliable_plate": 
    }

"""


def get_optimal_troops(resources:dict):

    """
    :param resources: the number of avaliable resources. It must be a dictionary (see above for details).
    :return: The optimal number of troops to recruit.mod given the avaliable resources (which you can buy and sell).
    """

    troops_stats = pd.read_excel("sh_legends_data.xlsx", engine='openpyxl', sheet_name = "troops_stats")
    armory_data = pd.read_excel("sh_legends_data.xlsx", engine='openpyxl', sheet_name="armory_data")
    troops = AMPL()
    troops.read("recruit.mod")
    troops.option["solver"] = "highs"

    health = troops_stats['Hit points'].values
    damage = troops_stats['Damage'].values
    avg_vuln = (troops_stats['Miss Arm'] + troops_stats['Blade Arm'] + troops_stats['Imp Arm']).values / 3 # average vulnerability for different weapons
    eff_vuln = avg_vuln.sum() / health # effective vulnerability ( scalarization w.r.t health ). It measures how fast you lose health when hit.
    agility = (troops_stats['Run'].values + troops_stats['Walk'].values) / 2 # running and walking speed average

    troops.set["U"] = troops_stats['Type'].values
    troops.set["A"] = armory_data['Type'].values

    # scalarize all columns (except vulnerability) in order for them to be of similar order
    troops.param["health"] = health / health.mean()
    troops.param["damage"] = damage / damage.mean()
    troops.param["vuln"] = eff_vuln
    troops.param["agility"] = agility / agility.mean()
    troops.param["gold_cost"] = troops_stats['Gold Cost'].values
    troops.param["hon_cost"] = troops_stats['Honour Cost'].values

    troops.param["buy"] = armory_data["Buy Price"].values
    troops.param["sell"] = armory_data["Sell Price"].values

    troops.param["avaliable_gold"] = resources["avaliable_gold"]
    troops.param["avaliable_honour"] = resources["avaliable_honour"]
    troops.param["avaliable_people"] = resources["avaliable_people"]

    troops.param["avaliable_bow"] = resources["avaliable_bow"]
    troops.param["avaliable_crossbow"] = resources["avaliable_crossbow"]
    troops.param["avaliable_spear"] = resources["avaliable_spear"]
    troops.param["avaliable_mace"] = resources["avaliable_mace"]
    troops.param["avaliable_pike"] = resources["avaliable_pike"]
    troops.param["avaliable_sword"] = resources["avaliable_sword"]
    troops.param["avaliable_leather"] = resources["avaiable_leather"]
    troops.param["avaliable_plate"] = resources["avaliable_plate"]

    troops.solve()

    return troops


avaliable_resources = {
    "avaliable_gold": 400,
    "avaliable_honour": 50,
    "avaliable_people": 150,
    "avaliable_bow": 1,
    "avaliable_crossbow": 100,
    "avaliable_spear": 1,
    "avaliable_mace": 1,
    "avaliable_pike": 1,
    "avaliable_sword": 1,
    "avaiable_leather": 0,
    "avaliable_plate": 1
    }

troops_names = pd.read_excel("sh_legends_data.xlsx", engine='openpyxl', sheet_name = "troops_stats")["Type"].values
armory_names = pd.read_excel("sh_legends_data.xlsx", engine='openpyxl', sheet_name="armory_data")

result = get_optimal_troops(avaliable_resources)

create_troops = result.var["x"].to_dict()
buy_armory = Counter(result.var["y"].to_dict())
sell_armory = result.var["z"].to_dict()
net_armory = Counter(buy_armory)
net_armory.subtract(sell_armory)

print("You should buy the following troops:")
for key_troops, value_troops in create_troops.items():
    if value_troops != 0:
        print(f"{key_troops}: {value_troops}")

print("You should do the following in the armory:")
for key_armory, value_armory in net_armory.items():
    if value_armory != 0:
        print(f"{key_armory}: {value_armory}")