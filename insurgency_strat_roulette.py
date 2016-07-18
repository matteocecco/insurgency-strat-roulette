import random

loadout = {'Primary': ["MP5K", "UMP-45", "MP-40", "Sterling", "AC-556", "Mk18", "M4A1", "M1 Carbine", "SKS", "AKS-74U",
                       "M16A4", "Galil SAR", "AKM", "AK-74", "Galil", "L1A1 SLR", "M14 EBR", "FAL", "M249", "RPK",
                       "M590", "TOZ", "M40A1", "Mosin", "Nothing"],
           'Sidearm': ["Makarov", "M45A1", "M9", "Model 10", "M1911", "Nothing"],
           'Optics': ["Holo", "Kobra", "Red dot", "2x Red dot", "C79 scope", "PO 4x24", "Nothing"],
           'Barrel': ["Heavy Barrel", "Suppressor", "Nothing"],
           'Underbarrel': ["Foregrip", "Bipod", "M203", "GP-25", "Nothing"],
           'Siderail': ["Flashlight", "Laser Sight", "Nothing"],
           'Ammo': ["Standard Ammo", "Tracer Ammo", "AP Ammo", "HP Ammo"],
           'Armor': ["Light Armor", "Heavy Armor", "Nothing"],
           'Explosives': ["Flare gun", "Flashbang", "Smoke", "Frag grenade", "Molotov", "Nothing"]}

loadout_list = ['Primary', 'Sidearm', 'Optics', 'Barrel', 'Underbarrel', 'Siderail', 'Ammo', 'Armor', 'Explosives']

def strat_roulette(loadout_list, loadout):
    for element in loadout_list:
        for key in loadout:
            if key == element:
                selected = random.choice(loadout[key])
                print("\t%s :\t%s" % (key, selected))
        
while True:
    print ("\tGood luck!\n\tIf something can't be attached, count it as Nothing\n")
    strat_roulette(loadout_list, loadout)
    ok = raw_input()
    