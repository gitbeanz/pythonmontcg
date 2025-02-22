import sys, os, random, json
from packinfo import Pack_Info
from packresults import Pack_Results

def game_loop(whale_mode):
    rip_quantity = "1"
    pack = get_pack()
    if (whale_mode is False):
        while True:
            rip_quantity = input('how many packs we ripping?: ')
            if (int(rip_quantity) and int(rip_quantity)>0):
                break
            else:
                print("Oops! We need a number!")
    rip_packs(pack, int(rip_quantity), whale_mode)
    print ("Total Price: $",int(rip_quantity)*7)

def rip_packs(pack, rip_quantity, whale_mode):
    rarities = ["Common", "Double Rare", "Shiny", "Shiny Super Rare", "Super Rare", "Art Rare", "Ultra Rare", "Special Art Rare"]
    hits = ["Shiny Super Rare", "Art Rare", "Ultra Rare", "Special Art Rare"]
    clear_terminal()
    if (whale_mode is False):
        print("Ripping", rip_quantity, "packs of", pack.set_name)
    tries = 0
    pack_list = []
    if (whale_mode is False):
        for i in range(0,rip_quantity):
            pack_results = rip_pack(pack)
            pack_list.append(pack_results)
            tries += 1
            print("\npack #", tries)
            for p in pack_results:
                print(p)
    else:
        whale = input("What card are we hunting? ")
        while True:
            pack_results = rip_pack(pack)
            pack_list.append(pack_results)
            tries += 1
            print("\npack #", tries)
            for p in pack_results:
                print(p)
            if whale in pack_results:
                break

        print("WOW! ITS", whale)
        print("WE PULLED IT! it only took", tries, "packs...So like..$", 7 * tries)
            
    if (whale_mode is False):
        print("")
        print("TOTAL RUN")
        for rarity in rarities:
            print(rarity,":", len([c for pck in pack_list for c in pck if rarity in c]))
        print("\nHITS")
        for hit in hits:
            print(hit,":", [c for pck in pack_list for c in pck if hit in c])
    


    
    

def rip_pack(pack):
    with open('sv4aset.json', 'r') as pokemon_info:
        pokemon = json.load(pokemon_info)

    pack_results = []
    # grab commons
    for i in range(0,pack.set_quantity-2):
        chosen_mon = random.choice([mon for mon in pokemon if mon["rarity"] == "Common"])
        pack_results.append(chosen_mon["rarity"] + " "+ chosen_mon["name"])

    #last 2!
    rarity_level_one = determine_rarity(pack.info["odds"])

    if rarity_level_one == "Double Rare":
        rarity_level_one = random.choice(["Double Rare", "Common"])

    rarity_level_two = determine_rarity(pack.info["odds"])

    #print(rarity_level_one, rarity_level_two)

    rare_mon_one = random.choice([mon for mon in pokemon if mon["rarity"] == rarity_level_one])
    rare_mon_two = random.choice([mon for mon in pokemon if mon["rarity"] == rarity_level_two])


    for m in [rare_mon_one, rare_mon_two]:
        pack_results.append(m["rarity"] + " " + m["name"])

    return (pack_results)

def determine_rarity(odds):
    if (random.randint(1,odds["Special Art Rare"]) == 1):
        return "Special Art Rare"
    elif (random.randint(1,odds["Art Rare"]) == 1):
        return "Art Rare"
    elif (random.randint(1, odds["Ultra Rare"]) == 1):
        return "Ultra Rare"
    elif (random.randint(1, odds["Super Rare"]) == 1):
        return "Super Rare"
    elif (random.randint(1, odds["Shiny Super Rare"]) == 1):
        return "Shiny Super Rare"
    elif (random.randint(1, odds["Shiny"]) == 1):
        return "Shiny"
    else:
        return "Double Rare"


    
def get_pack():
    #we will need to process this through a json or something similar later
    with open('sv4asetinfo.json', 'r') as paf_info:
        info = json.load(paf_info)
    PAF = Pack_Info("Shiny Treasure", "SV4a: Shiny Treasure", "SV4a", 10, info)
    return PAF

def cont():
    print("Press enter to continue...")
    if (sys.version_info[0] < 3):
        raw_input()
    else:
        input()
    clear_terminal()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    game_loop(False)