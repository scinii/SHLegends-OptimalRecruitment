import numpy as np
import pandas as pd
from amplpy import AMPL

# v0: given gold and honour. Calculate the optimal number of troops.
# v1: v0 +  you are also given armour conditions.
# v2: v1 + you can buy and sell armour.
# v3: v2 + you can buy and sell other resources
# v4: v3 + you schedule the people working as well
# sh_troops_recruitment_v0
"""
    If you are not using amplpy.modules (e.g. highs, coin), and the AMPL installation directory
    is not in the system search path, add it as follows:  
    from amplpy import add_to_path
    add_to_path(r"full path to the AMPL installation directory")
"""

def get_optimal_troops(avaliable_gold, avaliable_honour):

    troops_stats = pd.read_csv("sh_legends_troops_stats.csv")
    troops = AMPL()
    troops.read("recruit_v0.mod")
    troops.option["solver"] = "highs"

    troops.set["U"] = troops_stats['Type'].values
    troops.param["health"] = troops_stats['Hit points'].values
    troops.param["damage"] = troops_stats['Damage'].values
    troops.param["vuln"] = (troops_stats['Miss Arm'] + troops_stats['Blade Arm'] + troops_stats['Imp Arm']).values
    troops.param["agility"] = troops_stats['Run'].values
    troops.param["gold_cost"] = troops_stats['Gold Cost'].values
    troops.param["hon_cost"] = troops_stats['Honour Cost'].values
    troops.param["avaliable_gold"] = avaliable_gold
    troops.param["avaliable_honour"] = avaliable_honour

    troops.solve()

    return troops

t = get_optimal_troops(10000,1000000)

print( t.var["x"].to_dict() )