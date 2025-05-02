#  Optimal Recruitment Tool for Stronghold Legends

##  Inputs

The tool uses two datasets (that can be found in the installation folder):

### Troop Data
| Type        | Hit Points | Damage | Miss Armor | Blade Armor | Impact Armor | Walk Speed | Run Speed | Gold Cost | Honour Cost |
|-------------|------------|--------|------------|-------------|--------------|------------|-----------|-----------|-------------|
| Spearman    | 3000        | 6      | 1          | 1           | 1            | 2          | 4         | 6         | 0           |
| Archer      | 3000        | 2      | 1          | 2           | 2            | 2          | 5         | 12        | 0           |
| Crossbowman | 6000        | 2      | 0.5        | 1.2         | 1.2          | 1.5        | 2.5       | 12        | 0           |
| Pikeman     | 18000       | 4      | 0.5        | 0.15        | 0.15         | 1.5        | 2.5       | 10        | 0           |
| Maceman     | 6000        | 15     | 0.75       | 0.5         | 0.5          | 3          | 8         | 10        | 0           |
| Swordsman   | 15000       | 20     | 0.1        | 0.25        | 0.25         | 1          | 2         | 40        | 5           |
| Knight      | 20000       | 70     | 0.06       | 0.2         | 0.2          | 3          | 8         | 200       | 50          |

### Resource Data
| Type        | Sell Price | Buy Price |
|-------------|------------|-----------|
| Bow         | 15         | 30        |
| Crossbow    | 15         | 30        |
| Spear       | 10         | 15        |
| Mace        | 42         | 44        |
| Pike        | 18         | 20        |
| Sword       | 42         | 48        |
| Leather     | 12         | 15        |
| Plate       | 44         | 50        |

### Available Resources
The available resources (to the player) are passed in a dictionary:

```python
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
```
### Recruitment Type
The user may choose for the recruitment to be:
1) Balanced: equal weights for defense, attack and agility.
2) Defensive: maximize health and minimize vulnerability.
3) Aggressive: prioritize damage.
4) Agile: prioritize speed.


##  (Sample) Output

```python
You should buy the following troops:
Spearman: 98

You should do the following in the armory:
Bow: -1
Crossbow: -100
Mace: -1
Pike: -1
Plate: -1
Spear: 98
Sword: -1
```

If the value is negative then we are selling.

## TODO

- [ ] Implement GUI.

