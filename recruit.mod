# SETS

set U; # units
set A; # armours

# VARIABLES

var x{U} >= 0 integer;
var y{A} >= 0 integer; # items in the armory to buy
var z{A} >= 0 integer; # items in the armory to sell

# PARAMETERS

param health{U}; # health of the unit
param damage{U}; # damage the unit inflicts
param vuln{U}; # velnerability of the unit to blades, arrows and missiles
param agility{U}; # agility of the unit
param gold_cost{U}; # cost of the unit in gold
param hon_cost{U}; # cost of the unit in honour

param buy{A}; # buy price for a certain item in the armory
param sell{A}; # sell price for a certain item in the armory

param avaliable_gold;
param avaliable_honour;
param avaliable_people;
param avaliable_bow;
param avaliable_crossbow;
param avaliable_spear;
param avaliable_mace;
param avaliable_pike;
param avaliable_sword;
param avaliable_leather;
param avaliable_plate;


# OBJECTIVE FUNCTION


minimize objective_function: sum{u in U}x[u]*(vuln[u] - health[u] - damage[u] - agility[u] );


# CONSTRAINTS

subject to capital_constraints: sum{u in U} x[u] * gold_cost[u] <= avaliable_gold + (sum{a in A} z[a]*sell[a]) - (sum{a in A} y[a]*buy[a]);
subject to honour_constraint: sum{u in U} x[u] * hon_cost[u] <= avaliable_honour;
subject to people_constraint: sum{u in U} x[u] <= avaliable_people;

subject to bow_constraint: x['Archer'] <= avaliable_bow + y['Bow'] - z['Bow'];
subject to crossbow_constraint: x['Crossbowman'] <= avaliable_crossbow + y['Crossbow'] - z['Crossbow'];
subject to spearman_constraint: x['Spearman'] <= avaliable_spear + y['Spear'] - z['Spear'];
subject to pikeman_constrain: x['Pikeman'] <= avaliable_pike + y['Pike'] - z['Pike'];
subject to maceman_constraint: x['Maceman'] <= avaliable_mace + y['Mace'] - z['Mace'];
subject to sword_constraint: x['Swordsman'] + x['Knight'] <= avaliable_sword + y['Sword'] - z['Sword'];
subject to leather_constraint: x['Crossbowman'] + x['Maceman'] <= avaliable_leather + y['Leather'] - z['Leather'];
subject to plate_constraint: x['Swordsman'] + x['Knight'] + x['Pikeman'] <= avaliable_plate + y['Plate'] - z['Plate'];

subject to bow_sell_constraint: z['Bow'] <= avaliable_bow + y['Bow'];
subject to crossbow_sell_constraint: z['Crossbow'] <= avaliable_crossbow + y['Crossbow'] ;
subject to spear_sell_constraint: z['Spear'] <= avaliable_spear + y['Spear'] ;
subject to mace_sell_constraint: z['Mace'] <= avaliable_mace + y['Mace'] ;
subject to pike_sell_constraint: z['Pike'] <= avaliable_pike + y['Pike'] ;
subject to sword_sell_constraint: z['Sword'] <= avaliable_sword + y['Sword'] ;
subject to leather_sell_constraint: z['Leather'] <= avaliable_leather + y['Leather'] ;
subject to plate_sell_constraint: z['Plate'] <= avaliable_plate + y['Plate'] ;