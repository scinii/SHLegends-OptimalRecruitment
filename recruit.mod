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
param vuln{U}; # vulnerability of the unit to blades, arrows and missiles
param agility{U}; # agility of the unit
param gold_cost{U}; # cost of the unit in gold
param hon_cost{U}; # cost of the unit in honour

param buy{A}; # buy price for a certain item in the armory
param sell{A}; # sell price for a certain item in the armory

param available_gold;
param available_honour;
param available_people;
param available_bow;
param available_crossbow;
param available_spear;
param available_mace;
param available_pike;
param available_sword;
param available_leather;
param available_plate;

param defence_coeff;
param damage_coeff;
param agility_coeff;


# OBJECTIVE FUNCTION


minimize objective_function: sum{u in U}x[u]*(defence_coeff*(vuln[u] - health[u]) - damage_coeff*damage[u] - agility_coeff*agility[u]) + sum{a in A} (y[a]-z[a]) ;


# CONSTRAINTS

subject to capital_constraints: sum{u in U} x[u] * gold_cost[u] <= available_gold + (sum{a in A} z[a]*sell[a]) - (sum{a in A} y[a]*buy[a]);
subject to honour_constraint: sum{u in U} x[u] * hon_cost[u] <= available_honour;
subject to people_constraint: sum{u in U} x[u] <= available_people;

subject to bow_constraint: x['Archer'] <= available_bow + y['Bow'] - z['Bow'];
subject to crossbow_constraint: x['Crossbowman'] <= available_crossbow + y['Crossbow'] - z['Crossbow'];
subject to spearman_constraint: x['Spearman'] <= available_spear + y['Spear'] - z['Spear'];
subject to pikeman_constrain: x['Pikeman'] <= available_pike + y['Pike'] - z['Pike'];
subject to maceman_constraint: x['Maceman'] <= available_mace + y['Mace'] - z['Mace'];
subject to sword_constraint: x['Swordsman'] + x['Knight'] <= available_sword + y['Sword'] - z['Sword'];
subject to leather_constraint: x['Crossbowman'] + x['Maceman'] <= available_leather + y['Leather'] - z['Leather'];
subject to plate_constraint: x['Swordsman'] + x['Knight'] + x['Pikeman'] <= available_plate + y['Plate'] - z['Plate'];

subject to bow_sell_constraint: z['Bow'] <= available_bow + y['Bow'];
subject to crossbow_sell_constraint: z['Crossbow'] <= available_crossbow + y['Crossbow'] ;
subject to spear_sell_constraint: z['Spear'] <= available_spear + y['Spear'] ;
subject to mace_sell_constraint: z['Mace'] <= available_mace + y['Mace'] ;
subject to pike_sell_constraint: z['Pike'] <= available_pike + y['Pike'] ;
subject to sword_sell_constraint: z['Sword'] <= available_sword + y['Sword'] ;
subject to leather_sell_constraint: z['Leather'] <= available_leather + y['Leather'] ;
subject to plate_sell_constraint: z['Plate'] <= available_plate + y['Plate'] ;






