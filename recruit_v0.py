import numpy as np
import pandas as pd
from amplpy import AMPL

# v0: given gold, honour and people , armour. Calculate the optimal number of troops ---- DONE ----
# v1: you can buy and sell armour.
# v3: v2 + you can sell other resources

"""
    If you are not using amplpy.modules (e.g. highs, coin), and the AMPL installation directory
    is not in the system search path, add it as follows:  
    from amplpy import add_to_path
    add_to_path(r"full path to the AMPL installation directory")
"""

def get_optimal_troops(avaliable_gold, avaliable_honour, avaliable_people, avaliable_bow,
                       avaliable_crossbow, avaliable_spear, avaliable_mace, avaliable_pike, avaliable_sword, avaiable_leather, avaliable_plate):

    troops_stats = pd.read_csv("sh_legends_troops_stats.csv")

    troops = AMPL()
    troops.read("recruit_v0.mod")
    troops.option["solver"] = "highs"


    health = troops_stats['Hit points'].values
    damage = troops_stats['Damage'].values
    avg_vuln = (troops_stats['Miss Arm'] + troops_stats['Blade Arm'] + troops_stats['Imp Arm']).values / 3
    eff_vuln = avg_vuln.sum() / health
    agility = troops_stats['Run'].values

    troops.set["U"] = troops_stats['Type'].values
    troops.param["health"] = health / health.mean()
    troops.param["damage"] = damage / damage.mean()
    troops.param["vuln"] = eff_vuln
    troops.param["agility"] = agility / agility.mean()
    troops.param["gold_cost"] = troops_stats['Gold Cost'].values
    troops.param["hon_cost"] = troops_stats['Honour Cost'].values


    troops.param["avaliable_gold"] = avaliable_gold
    troops.param["avaliable_honour"] = avaliable_honour
    troops.param["avaliable_people"] = avaliable_people
    troops.param["avaliable_bow"] = avaliable_bow
    troops.param["avaliable_crossbow"] = avaliable_crossbow
    troops.param["avaliable_spear"] = avaliable_spear
    troops.param["avaliable_mace"] = avaliable_mace
    troops.param["avaliable_pike"] = avaliable_pike
    troops.param["avaliable_sword"] = avaliable_sword
    troops.param["avaiable_leather"] = avaiable_leather
    troops.param["avaliable_plate"] = avaliable_plate

    troops.solve()

    return troops.var["x"].to_dict()

t = get_optimal_troops(10000,10000,50,
                       5,0,0,0,0,0,0,0)

print(t)