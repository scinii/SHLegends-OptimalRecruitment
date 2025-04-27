import pandas as pd
from amplpy import AMPL
from collections import Counter

"""
    available_resources = {
    "available_gold": ,
    "available_honour": , 
    "available_people": , 
    "available_bow": ,
    "available_crossbow": , 
    "available_spear": , 
    "available_mace": , 
    "available_pike": , 
    "available_sword": , 
    "available_leather": , 
    "available_plate": 
    }

"""


def get_optimal_troops(resources:dict, prioritize = "balanced") :

    """
    :param resources: dictionary for the number of available resources.
    :param prioritize:
    :return: The optimal number of troops to recruit.
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

    troops.param["available_gold"] = resources["available_gold"]
    troops.param["available_honour"] = resources["available_honour"]
    troops.param["available_people"] = resources["available_people"]

    troops.param["available_bow"] = resources["available_bow"]
    troops.param["available_crossbow"] = resources["available_crossbow"]
    troops.param["available_spear"] = resources["available_spear"]
    troops.param["available_mace"] = resources["available_mace"]
    troops.param["available_pike"] = resources["available_pike"]
    troops.param["available_sword"] = resources["available_sword"]
    troops.param["available_leather"] = resources["available_leather"]
    troops.param["available_plate"] = resources["available_plate"]

    if prioritize == "balanced":

        troops.param["defence_coeff"] = 1
        troops.param["damage_coeff"] = 1
        troops.param["agility_coeff"] = 1

    elif prioritize == "defensive":

        troops.param["defence_coeff"] = 2
        troops.param["damage_coeff"] = 0.5
        troops.param["agility_coeff"] = 0.5

    elif prioritize == "aggressive":

        troops.param["defence_coeff"] = 0.5
        troops.param["damage_coeff"] = 2
        troops.param["agility_coeff"] = 0.5

    else:

        troops.param["defence_coeff"] = 0.5
        troops.param["damage_coeff"] = 0.5
        troops.param["agility_coeff"] = 2

    troops.solve(verbose=True)

    create_troops = troops.var["x"].to_dict()
    buy_armory = troops.var["y"].to_dict()
    sell_armory = troops.var["z"].to_dict()
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



    return troops


available_resources = {
    "available_gold": 40000,
    "available_honour": 0,
    "available_people": 10,
    "available_bow": 1,
    "available_crossbow": 1,
    "available_spear": 1,
    "available_mace": 1,
    "available_pike": 1,
    "available_sword": 1,
    "available_leather": 1,
    "available_plate": 1
    }

get_optimal_troops(available_resources,"agile")

