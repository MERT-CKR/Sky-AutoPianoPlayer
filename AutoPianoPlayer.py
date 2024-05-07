import time
import keyboard
import pandas as pd
import os
import json

with open("settings.json", "r", encoding="utf-8") as file:
    data = json.load(file)


current_directory = os.getcwd()
jsonFilePath = os.path.join(current_directory,"translations.json")

#if you user enter wrong value. call input again
def inputForce(prompt, Typ=int):
    while True:
        try:
            Input0 = Typ(input(prompt))
            return Input0
        except ValueError:
            print(_("invalid_prompt"))

def load_translations():
    if data["settings"][0]["firstTime"] == 0 or data["settings"][0]["language"]=="":
        print("Select your language: \n1.Türkçe \n2.English")
        lang = inputForce(">> ")
        if lang == 1:
            user_locale = "tr"
        elif lang == 2:
            user_locale = "en"

        data["settings"][0]["language"] = user_locale

        with open('settings.json', 'w', encoding="utf-8") as dosya:
            json.dump(data, dosya, indent=4,ensure_ascii=False)
    else:
        user_locale = data["settings"][0]["language"]


    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    global _
    _ = lambda key: translations['languages'][key][user_locale]



load_translations()
if data["settings"][0]["firstTime"] == 1:
    pass
else:
    print(_("first_opening"))

    data["settings"][0]["firstTime"] = 1

    print(_("tutorial3"))
    print(_("tutorial4"))
    print(_("tutorial1"))
    print(_("tutorial2"))

    newKeys = inputForce(">> ",str)
    newKeys = newKeys.replace(",", " ")

    if newKeys == "":
        data["settings"][0]["keys"] = data["settings"][0]["Default_keys"]
    else:
        data["settings"][0]["keys"] = newKeys

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(_("key_assigned"))
key =  data["settings"][0]["keys"]
key = key.split()


current_directory = os.getcwd()
fpath = os.path.join(current_directory, "database.csv")
data = pd.read_csv(fpath)

def bring(id):
    sheet_value = data.loc[id-1, 'sheet']
    return sheet_value

def showList():
    column_values = data["name"].tolist()
    for i, value in enumerate(column_values):
        id = i + 1
        print(f"{id}: {value}")

def write(name, sheet):
    global data
    id = data['ID'].max() + 1
    new_data = pd.DataFrame({"ID": [id], "name": [name], "sheet": [sheet]})
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv("database.csv", index=False)


def countDown():
    print(_("starting"))
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

def playMusic(sheets,speed):
    countDown()
    startTime = time.time()
    sheets = sheets.replace(".","?").lower()
    cords = "a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5".split()
    oldSheets = sheets.split()
    for i in range(len(cords)):
        sheets = sheets.replace(cords[i], key[i])

    for i in sheets.split():
           
            if i !="?":
                print(i)
            if keyboard.is_pressed('"'):
                print(_("loop_ending"))
                break
            if i == "?":
                print("wait")
                time.sleep(speed+0.1)
                pass
            else:
                if keyboard.is_pressed('"'):
                    print(_("loop_ending"))
                    break
                for char in i:
                    keyboard.press(char)
                    
                time.sleep(speed)
                for char in i:
                    keyboard.release(char)



    endTime = time.time()
    duration = endTime - startTime
    duration = str(duration)[:4]
    print(_("play_time"))
    print(">> ",duration,"\n\n")

                

def adjustSpeed():
    print(_("play_speed"))

    speed = inputForce(">> ",float)
    if speed <0 or speed >=10:
        print(_("invalid_play_speed"))
        speed = 3
    speed = speed / 10
    print(_("speed_adjusted"))
    print(">>",speed)
    return speed

    

def Run():
    print(_("do_you_have_sheets"))
    validChars ="A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5, ,.,0".split(",")

    sheets = inputForce(">> ",str)

    for s1 in sheets.split():
        if s1 not in validChars:
            raise ValueError(_("wrong_char"),(s1))
    
    if sheets == "0":
        print(_("choose_preloaded_music"))
        showList()
        selection = inputForce("\n>> ")
        playMusic(bring(selection),adjustSpeed())
        
    else:
        print(_("enter_music_name"))
        name = inputForce("",str)
        try:
            write(" "+name, sheets)
            print(_("added_to_preloaded_library"))
        except:
            print(_("not_added_to_preloaded_lib"))
            pass
    
        playMusic(sheets,adjustSpeed())
        

while True:
   
    Run()
    print(_("restart"))
    keepContinue = input(">> ")
    if keepContinue != "1":
        break
