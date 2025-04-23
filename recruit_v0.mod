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

# OBJECTIVE FUNCTION


minimize objective_function: sum{u in U}x[u]*(vuln[u] - health[u] - damage[u] - agility[u] );


# CONSTRAINTS

subject to capital_constraints: sum{u in U} x[u] * gold_cost[u] <= avaliable_gold;
subject to honour_constraint: sum{u in U} x[u] * hon_cost[u] <= avaliable_honour;
subject to people_constraint: sum{u in U} x[u] <= avaliable_people;