import time
import keyboard
import pandas as pd
import os
import json

with open("settings.json", "r", encoding="utf-8") as file:
    data = json.load(file)


if data["settings"][0]["firstTime"] == 1:
    pass
else:
    print("its look like you're new here")

    data["settings"][0]["firstTime"] = 1

    print("When you equip your instrument in Sky, enter the letters on the buttons in order.")
    print("E.g.: (y, u, i, o, ...)")
    print("Note: You can only use 15-button instrument.")
    print('If one of the letters on your buttons is ".", change it to another key from Settings>Controls (suggestion: b). Otherwise, that button will not be pressed.')

    newKeys = input()
    newKeys = newKeys.replace(",", " ")

    if newKeys == "":
        data["settings"][0]["keys"] = data["settings"][0]["Default_keys"]
    else:
        data["settings"][0]["keys"] = newKeys

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("key asignment sucsessfull")
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
    print("Starting...")
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
    for i in range(len(cords)):
        sheets = sheets.replace(cords[i], key[i])

    
    for i in sheets.split():
            if i !="?":
                print(i)
            if keyboard.is_pressed('"'):
                print('pressed " key,loop is getting end.')
                break
            if i == "?":
                print("wait")
                time.sleep(speed+0.15)
                pass
            else:
                if keyboard.is_pressed('"'):
                    print('pressed " key,loop is getting end.')
                    break
                for char in i:
                    keyboard.press(char)
                    
                time.sleep(speed)
                for char in i:
                    keyboard.release(char)

                

    endTime = time.time()
    duration = endTime - startTime
    duration = str(duration)[:4]
    print(f"Playback duration: {duration} sec")

                

def setSpeed():
    speed = float(input("enter play speed as (1,2,3,4,5) (1 quick, 5 slow)\nSuggestion 2 or 3:\n"))
    if speed <0 or speed >=10:
        print("speed set as 3, you entered a wrong value")
        speed = 3
    speed = speed / 10
    print("Speed setted:", speed)
    return speed

    

def Run():
    print("Enter sheets here. if you don't have press 0:\n")

    sheets = input()
    if sheets == "0":
        print("Choose one of the preloaded music\n")
        showList()
        selection = int(input())
        playMusic(bring(selection),setSpeed())
        
    else:
        name = input("Enter name of music:\n")
        try:
            write(" "+name, sheets)
            print("added to your preloaded songs library")
        except:
            print("something went wrong:/")
            pass

        playMusic(sheets,setSpeed())
        

while True:
   
    Run()
    keepContinue = input("Press 1 to restart the program:\n")
    if keepContinue != "1":
        break
