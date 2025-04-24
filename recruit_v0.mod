# SETS

set U; # units 

# VARIABLES

var x{U} >= 0 integer;

# PARAMETERS

param health{U}; # health of the unit
param damage{U}; # damage the unit inflicts
param vuln{U}; # velnerability of the unit to blades, arrows and missiles
param agility{U}; # agility of the unit
param gold_cost{U}; # cost of the unit in gold
param hon_cost{U}; # cost of the unit in honour
param avaliable_gold;
param avaliable_honour;
param avaliable_people;
param avaliable_bow;
param avaliable_crossbow;
param avaliable_spear;
param avaliable_mace;
param avaliable_pike;
param avaliable_sword;
param avaiable_leather;
param avaliable_plate;


# OBJECTIVE FUNCTION


minimize objective_function: sum{u in U}x[u]*(vuln[u] - health[u] - damage[u] - agility[u] );


# CONSTRAINTS

subject to capital_constraints: sum{u in U} x[u] * gold_cost[u] <= avaliable_gold;
subject to honour_constraint: sum{u in U} x[u] * hon_cost[u] <= avaliable_honour;
subject to people_constraint: sum{u in U} x[u] <= avaliable_people;

subject to bow_constraint: x['Archer'] <= avaliable_bow;
subject to crossbow_constraint: x['Crossbowman'] <= avaliable_crossbow;
subject to spearman_constraint: x['Spearman'] <= avaliable_spear;
subject to pikeman_constrain: x['Pikeman'] <= avaliable_pike;
subject to maceman_constraint: x['Maceman'] <= avaliable_mace;
subject to sword_constraint: x['Swordsman'] + x['Knight'] <= avaliable_sword;
subject to leather_constraint: x['Crossbowman'] + x['Maceman'] <= avaiable_leather;
subject to plate_constraint: x['Swordsman'] + x['Knight'] + x['Pikeman'] <= avaliable_plate;
