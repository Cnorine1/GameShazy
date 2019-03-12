import json
# from library import *
from levelLibrary import *
import random


##Create Levels here with this level maker! Just make a dictionary with spawn times and enemies, and the background elements.
#then run the script, make sure to not overwrite a file unintentially.




levelName="level1.json" #level follwed level_number
writeLocation = "levels/"+levelName
data = {
    "time":{ 0: #time zero
            {"player":{ #starting info if dead
                "health":1,
                "location":[500,700],
                "image":"SweetShip.png",
                "weapon": "blue_lazer",
                "scheme": "arrows",
                },
            # "enemy":{
            #     "class": ["@s7-mv-5-1-0"],
            #     "health": 1
            #     },
            "background": "Asteroid.png"
            
            },
            3: #time zero
            {"enemy":{
                "class": ["@s3-db-3-20-0-DTwaveBeam"],
                }
            },
           
       
    },
    "end": {"time":80, "boss":False} #this gives the ending parameters
        #if time=None, then boss=imageName of poss sprite, once defeated


}

clusterDIC_FULL ={
    0:"full",
    1:"L3",
    2:"L4",
    3:"L5",
    4:"R3",
    5:"R4",
    6:"R5",
    7:"M3",
    8:"M4",
    9:"M5",
    10:"ML3",
    11:"ML4",
    12:"ML5",
    13:"MR3",
    14:"MR4",
    15:"MR5"

}

#RUSH Left side
ClusterDIC_Left ={
    0:"L3",
    1:"L4",
    2:"L5",
    3:"ML3",
    4:"ML4",
    5:"ML5"
}
ClusterDIC_Right ={
    0:"R3",
    1:"R4",
    2:"R5",
    3:"MR3",
    4:"MR4",
    5:"MR5"
}
# for i in range(3,7):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s8-db-3-1-0-DTspitfire"]}}

# for i in range(11,15):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s5-db-3-1-0-DTwaveBeam"]}}

# for i in range(22,26):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s8-db-3-1-0-DTchargeShot"]}}

# for i in range(31,35):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s5-db-3-1-0-DThealth"]}}

# for i in range(41,45):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s8-db-3-1-0-DTcommon"]}}

for i in range(8,38):#5 enemies in line
    go = random.randint(0,100)
    if(go>80):
        select = go % 16
        data["time"][i] = {"enemy":{ "class": cluster(selection=clusterDIC_FULL[select],b="db",s="3",h="1",d="DTempty")}}


data["time"][40] = {"enemy":{  "class": [ #a look at every enemy type/skin.
                    # "@s1-db-7-400-0-DTcommon",
                    # "@s2-d-1-400--DTcommon",
                    # "@s3-c-1-400-0-DTcommon",
                    "@s5-s-1-10-0-DTspitfire",
                    # "@s7-cz-1-400-0-DTcommon",
                    # # "@s8-cr-3-400-0-DTcommon",
                    # "@s9-cr-1-400-0-DTcommon",
                    # "@s10-mv-1-400-0-DTcommon",
                    # "@s12-db-1-400-0-DTcommon",
                    # "@s13-ds-1-400-0-DTcommon",
                    # "@s14-db-7-400-0-DTcommon"
                ]}}

data["time"][45] = {"enemy":{  "class": [ #a look at every enemy type/skin.
                    # "@s1-db-7-400-0-DTcommon",
                    # "@s2-d-1-400--DTcommon",
                    # "@s3-c-1-400-0-DTcommon",
                    # "@s5-s-1-400-50-DTspitfire",
                    # "@s7-cz-1-400-0-DTcommon",
                    # # "@s8-cr-3-400-0-DTcommon",
                    # "@s9-cr-1-400-0-DTcommon",
                    "@s10-mv-2-25-0-DTspitfire",
                    # "@s12-db-1-400-0-DTcommon",
                    # "@s13-ds-1-400-0-DTcommon",
                    # "@s14-db-7-400-0-DTcommon"
                ]}}

data["time"][50] = {"enemy":{  "class": [ #a look at every enemy type/skin.
                    # "@s1-db-7-400-0-DTcommon",
                    # "@s2-d-1-400--DTcommon",
                    "@s3-c-5-100-0-DTempty",
                    # "@s5--1-400-50-DTspitfire",
                    # "@s7-cz-1-400-0-DTcommon",
                    "@s8-cr-2-50-0-DTspitfire",
                    # "@s9-cr-1-400-0-DTcommon",
                    # "@s10-mv-1-400-0-DTcommon",
                    # "@s12-db-1-400-0-DTcommon",
                    # "@s13-ds-1-400-0-DTcommon",
                    # "@s14-db-7-400-0-DTcommon"
                ]}}



for i in range(60,80):#5 enemies in line
    go = random.randint(0,100)
    if(go<40):
        select = go % 16
        data["time"][i] = {"enemy":{ "class": cluster(selection=clusterDIC_FULL[select],b="ds",s="3",h="3",d="DTempty")}}
    if(go>80):
        select = (go + 5) % 16
        data["time"][i] = {"enemy":{ "class": cluster(selection=clusterDIC_FULL[select],b="c",s="3",h="3",d="DTcoin")}}





# data["time"][79] = {"boss_sprite":{  "image":"boss.png", "class": [ENEMY_camperMid]}}




# for i in range(11,16):#5 enemies in line
#     data["time"][i] = {"enemy":{ "class": ["@s11-db-3-2-0","@s12-db-3-2-0"],"health":1}}


# for i in range(16,30,1):#16 random fast movers
#     n = str(random.randint(1,14))
#     data["time"][i] = {"enemy":{ "class": ["@s"+n+"-db-5-1-0"],"health":1}}



# for i in range(33,53,1):#20 random fast straffers
#     n = str(random.randint(1,14))
#     data["time"][i] = {"enemy":{ "class": ["@s"+n+"-ds-5-1-0"],"health":1}}

# for i in range(55,70,3):#5 mrvectors
#     n = str(random.randint(1,14))
#     data["time"][i] = {"enemy":{ "class": ["@s"+n+"-mv-5-1-0"],"health":1}}


# #RUSH generator
# for i in range(51,60):
#     s1 = str((i%4)+1)
#     s2 = str((i%4)+2)
#     s3 = str((i%6)+5)
#     s4 = str((i%4)+9)
#     s5 = str((i%4)+11)
#     spd1 = str(random.randint(1,(i%10+1)))
#     data["time"][i] = {"enemy":{"class":["@s"+s2+"-cr-3-1", "@s"+s1+"-c-4-1", "@s6-d-"+spd1+"-1", "@s"+s2+"-cr-4-1", "@s"+s1+"-c-3-1"],"health": 1},}


# #RUSH generator
# for i in range(61,90):
#     s1 = str((i%4)+1)
#     s2 = str((i%4)+2)
#     s3 = str((i%6)+5)
#     s4 = str((i%4)+9)
#     s5 = str((i%4)+11)
    
#     spd1 = str(random.randint(1,(i%10+1)))
#     data["time"][i] = {"enemy":{"class":["@s"+s1+"-d-3-2", "@s"+s5+"-d-4-3", "@s"+s4+"-s-"+spd1+"-5", "@s"+s2+"-c-4-3", "@s"+s3+"-cr-3-2"],"health": 1},}


# #RUSH generator
# for i in range(91,130,2):
#     s1 = str((i%4)+1)
#     s2 = str((i%4)+2)
#     s3 = str((i%6)+5)
#     s4 = str((i%4)+9)
#     s5 = str((i%4)+11)
    
#     spd1 = str(random.randint(1,(i%10+1)))
#     spd2 = str(random.randint(1,(i%10+1)))
#     spd3 = str(random.randint(1,(i%10+1)))
#     spd4 = str(random.randint(1,(i%10+1)))
#     data["time"][i] = {"enemy":{"class":["@s"+s1+"-d-"+spd2+"-2", "@s"+s5+"-c-"+spd3+"-2", "@s"+s4+"-s-"+spd1+"-6", "@s"+s2+"-d-"+spd3+"-2", "@s"+s3+"-d-"+spd4+"-2"],"health": 1},}
#     data["time"][i+1] = {"enemy":{"class":["@s"+s1+"-s-"+spd2+"-2", "@s"+s5+"-d-"+spd3+"-2", "@s"+s4+"-d-"+spd1+"-6", "@s"+s2+"-cr-"+spd3+"-2", "@s"+s3+"-c-"+spd4+"-2"],"health": 1},}
# #RUSH generator
# for i in range(131,150,2):
#     sc1 = str((i%4)+1)
#     sc2 = str((i%4)+2)
#     sc3 = str((i%6)+5)
#     sc4 = str((i%4)+9)
#     sc5 = str((i%4)+11)

#     sectorLoc = [sc1,sc2,sc3,sc4,sc5]
#     s1=sectorLoc.pop(random.randint(1,4))
#     s2=sectorLoc.pop(random.randint(1,3))
#     s3=sectorLoc.pop(random.randint(1,2))
#     s4=sectorLoc.pop(random.randint(1,1))
#     s5=sectorLoc.pop()

    
#     spd1 = str(random.randint(3,(i%10+3)))
#     spd2 = str(random.randint(3,(i%10+3)))
#     spd3 = str(random.randint(3,(i%10+3)))
#     spd4 = str(random.randint(3,(i%10+3)))
#     data["time"][i] = {"enemy":{"class":["@s"+s1+"-d-"+spd2+"-2", "@s"+s5+"-c-"+spd3+"-2", "@s"+s4+"-s-"+spd1+"-100", "@s"+s2+"-cz-"+spd3+"-2", "@s"+s3+"-cr-"+spd4+"-2"],"health": 1},}
#     data["time"][i+1] = {"enemy":{"class":["@s"+s1+"-c-"+spd2+"-2", "@s"+s5+"-d-"+spd3+"-2", "@s"+s4+"-d-"+spd1+"-2", "@s"+s2+"-d-"+spd3+"-2", "@s"+s3+"-s-"+spd4+"-100"],"health": 1},}

print(JSONCHECKER(data,False))

#When we execute levelMaker in Python, it saves a copy of the script we build
with open (writeLocation,"w") as write_file:
    json.dump (data, write_file, indent=4, sort_keys=True )


print(data)
