#!/usr/bin/env python3
"""Generate config files and all 8 chapter level files for Ash and Iron."""
import json, os

BASE = '/home/user/GBA-Fire-Emblem-Like-Game/ash_and_iron.ltproj/game_data'

def w(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f'  wrote {os.path.basename(path)}')

ZERO = {"HP":0,"STR":0,"MAG":0,"SKL":0,"SPD":0,"LCK":0,"DEF":0,"RES":0,"CON":0,"MOV":0}

# ── Difficulty modes ─────────────────────────────────────────────────────────
w(f'{BASE}/difficulty_modes.json', [
    {"nid":"Normal","name":"Normal","color":"blue","permadeath_choice":"Classic",
     "growths_choice":"Random","rng_choice":"True Hit",
     "player_bases":ZERO,"enemy_bases":ZERO,"boss_bases":ZERO,
     "player_growths":ZERO,"enemy_growths":ZERO,"boss_growths":ZERO,
     "player_autolevels":0,"enemy_autolevels":0,"boss_autolevels":0,
     "promoted_autolevels_fraction":1.0,"start_locked":False},
    {"nid":"Hard","name":"Hard","color":"red","permadeath_choice":"Classic",
     "growths_choice":"Random","rng_choice":"True Hit",
     "player_bases":ZERO,
     "enemy_bases":{"HP":2,"STR":2,"MAG":2,"SKL":2,"SPD":2,"LCK":0,"DEF":2,"RES":2,"CON":0,"MOV":0},
     "boss_bases": {"HP":4,"STR":4,"MAG":4,"SKL":4,"SPD":2,"LCK":0,"DEF":4,"RES":4,"CON":0,"MOV":0},
     "player_growths":ZERO,
     "enemy_growths":{"HP":10,"STR":10,"MAG":10,"SKL":10,"SPD":10,"LCK":0,"DEF":10,"RES":10,"CON":0,"MOV":0},
     "boss_growths": {"HP":15,"STR":15,"MAG":15,"SKL":15,"SPD":10,"LCK":0,"DEF":15,"RES":15,"CON":0,"MOV":0},
     "player_autolevels":0,"enemy_autolevels":1,"boss_autolevels":2,
     "promoted_autolevels_fraction":1.0,"start_locked":False},
    {"nid":"Lunatic","name":"Lunatic","color":"purple","permadeath_choice":"Classic",
     "growths_choice":"Random","rng_choice":"True Hit",
     "player_bases":{"HP":-2,"STR":-1,"MAG":-1,"SKL":-1,"SPD":-1,"LCK":0,"DEF":-1,"RES":-1,"CON":0,"MOV":0},
     "enemy_bases":{"HP":4,"STR":4,"MAG":4,"SKL":4,"SPD":4,"LCK":0,"DEF":4,"RES":4,"CON":0,"MOV":0},
     "boss_bases": {"HP":8,"STR":8,"MAG":8,"SKL":8,"SPD":4,"LCK":0,"DEF":8,"RES":8,"CON":0,"MOV":0},
     "player_growths":ZERO,
     "enemy_growths":{"HP":25,"STR":25,"MAG":25,"SKL":25,"SPD":25,"LCK":0,"DEF":25,"RES":25,"CON":0,"MOV":0},
     "boss_growths": {"HP":30,"STR":30,"MAG":30,"SKL":30,"SPD":25,"LCK":0,"DEF":30,"RES":30,"CON":0,"MOV":0},
     "player_autolevels":0,"enemy_autolevels":2,"boss_autolevels":4,
     "promoted_autolevels_fraction":1.0,"start_locked":True},
])
print('difficulty_modes.json')

# ── Factions (append) ────────────────────────────────────────────────────────
with open(f'{BASE}/factions.json') as f:
    factions = json.load(f)
existing = {fc['nid'] for fc in factions}
for fc in [
    {"nid":"Valdres","name":"Valdres Royal Guard","desc":"Kira's loyal companions.","icon_nid":"KnightEmblem","icon_index":[0,0]},
    {"nid":"Solara","name":"Solaran Empire","desc":"The eastern theocracy that invaded Valdres.","icon_nid":"KnightEmblem","icon_index":[0,0]},
    {"nid":"Rebel","name":"Valdres Rebels","desc":"Opportunistic traitors seeking to surrender.","icon_nid":"BanditEmblem","icon_index":[0,0]},
    {"nid":"Confederation","name":"Oras Confederation","desc":"The mercantile Confederation of Oras.","icon_nid":"NeutralEmblem","icon_index":[0,0]},
]:
    if fc['nid'] not in existing:
        factions.append(fc)
with open(f'{BASE}/factions.json','w') as f:
    json.dump(factions, f, indent=4)
print('factions.json')

# ── Support pairs (append) ───────────────────────────────────────────────────
def sreq(c, b, a):
    def r(rank, pts):
        return {"support_rank":rank,"requirement":pts,"gate":"",
                "damage":0.5,"resist":0.5,"accuracy":2.5,"avoid":2.5,
                "crit":2.5,"dodge":2.5,"attack_speed":0.0,"defense_speed":0.0}
    return [r("C",c), r("B",b), r("A",a)]

with open(f'{BASE}/support_pairs.json') as f:
    pairs = json.load(f)
existing_p = {(p['unit1'],p['unit2']) for p in pairs}
for p in [
    {"unit1":"Kira","unit2":"Brennan","one_way":False,"requirements":sreq(20,50,80)},
    {"unit1":"Kira","unit2":"Lysa","one_way":False,"requirements":sreq(20,50,80)},
    {"unit1":"Kira","unit2":"Mira","one_way":False,"requirements":sreq(25,55,90)},
    {"unit1":"Brennan","unit2":"Lysa","one_way":False,"requirements":sreq(25,60,95)},
    {"unit1":"Oswin","unit2":"Tessara","one_way":False,"requirements":sreq(30,65,100)},
    {"unit1":"Caela","unit2":"Soren","one_way":False,"requirements":sreq(30,65,100)},
    {"unit1":"Mira","unit2":"Fionn","one_way":False,"requirements":sreq(25,55,90)},
    {"unit1":"Aldric","unit2":"Kira","one_way":True,"requirements":sreq(20,50,80)},
]:
    if (p['unit1'],p['unit2']) not in existing_p:
        pairs.append(p)
with open(f'{BASE}/support_pairs.json','w') as f:
    json.dump(pairs, f, indent=4)
print('support_pairs.json')

# ── Level helpers ─────────────────────────────────────────────────────────────
def pu(nid, pos):
    return {"nid":nid,"team":"player","ai":"None","roam_ai":None,"ai_group":None,
            "starting_position":pos,"starting_traveler":None,"generic":False}

def eu(nid, pos, ai="Guard"):
    return {"nid":nid,"team":"enemy","ai":ai,"roam_ai":None,"ai_group":None,
            "starting_position":pos,"starting_traveler":None,"generic":False}

def ge(nid, lvl, klass, faction, items, ai="Attack", pos=None):
    return {"nid":nid,"variant":None,"level":lvl,"klass":klass,"faction":faction,
            "starting_items":[[i,False] for i in items],"starting_skills":[],
            "team":"enemy","ai":ai,"roam_ai":None,"ai_group":"",
            "starting_position":pos or [0,0],"starting_traveler":None,"generic":True}

MUSIC = {"player_phase":"Distant Roads","enemy_phase":"Shadow of the Enemy",
         "other_phase":None,"enemy2_phase":None,"player_battle":"Attack",
         "enemy_battle":"Defense","other_battle":None,"enemy2_battle":None}

def level(nid, name, tilemap, obj_s, obj_w, obj_l, units, regions=None, groups=None):
    return [{"nid":nid,"name":name,"tilemap":tilemap,"bg_tilemap":None,"party":"Kira",
             "music":MUSIC,"objective":{"simple":obj_s,"win":obj_w,"loss":obj_l},
             "roam":False,"roam_unit":None,"go_to_overworld":False,"should_record":True,
             "tags":[],"units":units,"regions":regions or [],"unit_groups":groups or [],"ai_groups":[]}]

LD = f'{BASE}/levels'
os.makedirs(LD, exist_ok=True)

# ── Chapter 1 ─────────────────────────────────────────────────────────────────
w(f'{LD}/1.json', level("1","Chapter 1 — The Walls of Edenmere","Ch1_Edenmere",
    "Seize the south gate","Kira seizes the south gate","Kira or Aldric dies",
    [pu("Kira",[3,7]),pu("Brennan",[3,8]),pu("Lysa",[2,8]),
     eu("Draven",[13,9],"Guard"),
     ge("101",3,"Fighter","Solara",["Iron_Axe"],"Attack",[8,4]),
     ge("102",3,"Fighter","Solara",["Iron_Axe"],"Attack",[9,4]),
     ge("103",3,"Soldier","Solara",["Iron_Lance"],"Attack",[10,3]),
     ge("104",2,"Fighter","Solara",["Iron_Axe"],"Attack",[11,4]),
     ge("105",4,"Cavalier","Solara",["Iron_Lance"],"Attack",[14,5]),],
    regions=[{"nid":"SouthGate","position":[13,9],"size":[1,1],
              "region_type":"event","sub_nid":"1_Seize","condition":"True"}],
    groups=[{"nid":"OswinGroup","units":["Oswin"],"positions":{"Oswin":[12,3]}}]))

# ── Chapter 2 ─────────────────────────────────────────────────────────────────
w(f'{LD}/2.json', level("2","Chapter 2 — Mercy Road","Ch2_MercyRoad",
    "Rout all enemies","All enemies defeated","Kira or Aldric dies",
    [pu("Kira",[2,8]),pu("Brennan",[1,8]),pu("Lysa",[1,7]),pu("Oswin",[3,8]),
     ge("201",5,"Fighter","Rebel",["Iron_Axe"],"Attack",[8,5]),
     ge("202",5,"Soldier","Rebel",["Iron_Lance"],"Attack",[9,5]),
     ge("203",4,"Soldier","Rebel",["Iron_Lance"],"Attack",[10,4]),
     ge("204",5,"Knight","Rebel",["Iron_Lance"],"Guard",[13,6]),
     ge("205",4,"Fighter","Rebel",["Iron_Axe"],"Attack",[14,5]),
     ge("206",5,"Archer","Rebel",["Iron_Bow"],"Attack",[12,3]),],
    groups=[{"nid":"MiraGroup","units":["Mira"],"positions":{"Mira":[7,5]}}]))

# ── Chapter 3 ─────────────────────────────────────────────────────────────────
w(f'{LD}/3.json', level("3","Chapter 3 — The Crossing at Vel Bridge","Ch3_VelBridge",
    "Defeat boss or seize the bridge","Defeat Horst or seize the bridge","Kira or Aldric dies",
    [pu("Kira",[2,8]),pu("Brennan",[1,8]),pu("Lysa",[1,7]),
     pu("Oswin",[3,8]),pu("Mira",[2,7]),
     eu("Horst",[12,5],"Guard"),
     ge("301",6,"Soldier","Rebel",["Iron_Lance"],"Attack",[7,6]),
     ge("302",6,"Fighter","Rebel",["Iron_Axe"],"Attack",[8,6]),
     ge("303",5,"Archer","Rebel",["Iron_Bow"],"Attack",[9,5]),
     ge("304",5,"Cavalier","Rebel",["Iron_Lance"],"Attack",[10,5]),
     ge("305",6,"Knight","Rebel",["Iron_Lance"],"Guard",[11,6]),],
    regions=[{"nid":"BridgeSeize","position":[12,5],"size":[1,1],
              "region_type":"event","sub_nid":"3_Seize","condition":"True"}],
    groups=[{"nid":"CaelaGroup","units":["Caela"],"positions":{"Caela":[4,7]}},
            {"nid":"SorenGroup","units":["Soren"],"positions":{"Soren":[5,6]}}]))

# ── Chapter 4 ─────────────────────────────────────────────────────────────────
w(f'{LD}/4.json', level("4","Chapter 4 — City of Oras","Ch4_CityOras",
    "Seize the embassy","Kira seizes the Oras embassy","Kira or Aldric dies",
    [pu("Kira",[2,7]),pu("Brennan",[1,7]),pu("Lysa",[1,6]),
     pu("Oswin",[3,7]),pu("Mira",[2,6]),pu("Caela",[3,6]),pu("Soren",[4,7]),
     ge("401",8,"Myrmidon","Solara",["Steel_Sword"],"Attack",[10,5]),
     ge("402",8,"Myrmidon","Solara",["Steel_Sword"],"Attack",[11,5]),
     ge("403",7,"Soldier","Solara",["Steel_Lance"],"Attack",[12,4]),
     ge("404",8,"Archer","Solara",["Steel_Bow"],"Attack",[12,6]),
     ge("405",9,"Mage","Solara",["Fire"],"Attack",[14,5]),
     {"nid":"Inquisitor_Spy","variant":None,"level":9,"klass":"Assassin",
      "faction":"Solara","starting_items":[["Killing_Edge",False]],"starting_skills":[],
      "team":"enemy","ai":"Guard","roam_ai":None,"ai_group":None,
      "starting_position":[13,3],"starting_traveler":None,"generic":False},],
    regions=[{"nid":"Embassy","position":[14,2],"size":[1,1],
              "region_type":"event","sub_nid":"4_Seize","condition":"True"}],
    groups=[{"nid":"FionnGroup","units":["Fionn"],"positions":{"Fionn":[9,5]}},
            {"nid":"TessaraGroup","units":["Tessara"],"positions":{"Tessara":[14,7]}}]))

# ── Chapter 5 ─────────────────────────────────────────────────────────────────
w(f'{LD}/5.json', level("5","Chapter 5 — The Sunken Keep","Ch5_SunkenKeep",
    "Defeat the Inquisitor","Defeat Inquisitor Voss","Kira or Aldric dies",
    [pu("Kira",[2,9]),pu("Brennan",[1,9]),pu("Lysa",[1,8]),
     pu("Oswin",[3,9]),pu("Mira",[2,8]),pu("Caela",[4,9]),
     pu("Soren",[3,8]),pu("Fionn",[4,8]),pu("Tessara",[5,9]),
     eu("Inquisitor",[8,2],"Guard"),
     ge("501",9,"Shaman","Solara",["Flux"],"Attack",[6,5]),
     ge("502",9,"Shaman","Solara",["Flux"],"Attack",[7,5]),
     ge("503",10,"Knight","Solara",["Steel_Lance"],"Guard",[5,4]),
     ge("504",8,"Myrmidon","Solara",["Steel_Sword"],"Attack",[7,6]),
     ge("505",8,"Archer","Solara",["Steel_Bow"],"Attack",[8,6]),],
    groups=[{"nid":"VelaGroup","units":["Vela"],"positions":{"Vela":[8,8]}}]))

# ── Chapter 6 ─────────────────────────────────────────────────────────────────
w(f'{LD}/6.json', level("6","Chapter 6 — The Betrayal at Thornpass","Ch6_Thornpass",
    "Defeat Commander Garan","Defeat Commander Garan","Kira, Aldric, or the caravan is destroyed",
    [pu("Kira",[2,9]),pu("Brennan",[1,9]),pu("Lysa",[1,8]),
     pu("Oswin",[3,9]),pu("Mira",[2,8]),pu("Caela",[4,9]),
     pu("Soren",[3,8]),pu("Fionn",[4,8]),pu("Tessara",[5,9]),pu("Vela",[5,8]),
     eu("Garan",[13,3],"Guard"),
     ge("601",12,"Cavalier","Rebel",["Steel_Lance"],"Attack",[8,5]),
     ge("602",12,"Cavalier","Rebel",["Steel_Sword"],"Attack",[9,5]),
     ge("603",11,"Knight","Rebel",["Steel_Lance"],"Guard",[10,4]),
     ge("604",12,"Archer","Rebel",["Steel_Bow"],"Attack",[10,6]),
     ge("605",12,"Mage","Rebel",["Thunder"],"Attack",[11,3]),
     ge("606",13,"Paladin","Rebel",["Silver_Lance"],"Attack",[12,4]),]))

# ── Chapter 7 ─────────────────────────────────────────────────────────────────
w(f'{LD}/7.json', level("7","Chapter 7 — Before the Throne","Ch7_RoyalPalace",
    "Seize the throne","Kira seizes the Valdres throne","Kira or Aldric dies",
    [pu("Kira",[2,9]),pu("Brennan",[1,9]),pu("Lysa",[1,8]),
     pu("Oswin",[3,9]),pu("Mira",[2,8]),pu("Caela",[4,9]),
     pu("Soren",[3,8]),pu("Fionn",[4,8]),pu("Tessara",[5,9]),
     pu("Vela",[5,8]),pu("Aldric",[6,9]),
     eu("Varek",[8,2],"Guard"),
     ge("701",14,"General","Solara",["Steel_Lance","Hand_Axe"],"Guard",[6,4]),
     ge("702",14,"General","Solara",["Steel_Lance"],"Guard",[7,4]),
     ge("703",13,"Paladin","Solara",["Silver_Sword"],"Attack",[8,5]),
     ge("704",13,"Swordmaster","Solara",["Steel_Sword"],"Attack",[8,6]),
     ge("705",12,"Sage","Solara",["Elfire"],"Attack",[7,3]),],
    regions=[{"nid":"Throne7","position":[8,1],"size":[1,1],
              "region_type":"event","sub_nid":"7_Seize","condition":"True"}]))

# ── Chapter 8 ─────────────────────────────────────────────────────────────────
w(f'{LD}/8.json', level("8","Chapter 8 — Ash and Iron","Ch8_Edenmere_Siege",
    "Defeat the Ashen Knight","Defeat Varek","Kira or Aldric dies",
    [pu("Kira",[2,9]),pu("Brennan",[1,9]),pu("Lysa",[1,8]),
     pu("Oswin",[3,9]),pu("Mira",[2,8]),pu("Caela",[4,9]),
     pu("Soren",[3,8]),pu("Fionn",[4,8]),pu("Tessara",[5,9]),
     pu("Vela",[5,8]),pu("Aldric",[6,9]),
     eu("Varek",[8,2],"Guard"),
     ge("801",16,"General","Solara",["Silver_Lance","Hand_Axe"],"Guard",[6,3]),
     ge("802",16,"General","Solara",["Silver_Lance"],"Guard",[7,3]),
     ge("803",15,"Paladin","Solara",["Silver_Sword","Javelin"],"Attack",[8,5]),
     ge("804",15,"Paladin","Solara",["Silver_Lance","Javelin"],"Attack",[9,5]),
     ge("805",15,"Swordmaster","Solara",["Silver_Sword"],"Attack",[9,6]),
     ge("806",14,"Sage","Solara",["Elfire"],"Attack",[7,4]),
     ge("807",15,"Sniper","Solara",["Silver_Bow"],"Attack",[10,3]),],
    regions=[{"nid":"VarekBattle","position":[8,2],"size":[1,1],
              "region_type":"event","sub_nid":"8_VarekDeath","condition":"True"}]))

print("\nAll config + level files done!")
