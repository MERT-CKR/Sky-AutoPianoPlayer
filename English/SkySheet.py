import time
import keyboard
import pandas as pd
data = pd.read_csv("database.csv")

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
    sheets = sheets.replace(".","x").lower()
    cords = "a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5".split()
    key = "y u ı o p h j k l ş n m ö ç b".split()
    for i in range(len(cords)):
        sheets = sheets.replace(cords[i], key[i])


    for i in sheets.split():
        if keyboard.is_pressed('"'):
            print('pressed " key,loop is getting end.')
            break
        if i == "x":
            time.sleep(speed+0.22)
            pass
        else:
            for char in i:
                keyboard.press(char)
                print(i)
            time.sleep(speed)
            for char in i:
                keyboard.release(char)

    endTime = time.time()
    duration = endTime - startTime
    duration = str(duration)[:4]
    print(f"Playback duration: {duration} sec")

                

def setSpeed():
    speed = float(input("enter play speed as (1,2,3,4,5) (1 quick, 5 slow)\nSuggestion 2 or 3: "))
    if speed <0 or speed >=10:
        print("speed set as 3, you entered a wrong value")
        speed = 3
    speed = speed / 10
    print("Speed setted:", speed)
    return speed

    

def Run():
    print("Enter sheets here. if you don't have press 0: ")

    sheets = input()
    if sheets == "0":
        print("Choose one of the preloaded music.")
        showList()
        selection = int(input())
        playMusic(bring(selection),setSpeed())
        
    else:
        name = input("Enter name of music: ")
        try:
            write(" "+name, sheets)
            print("added to your preloaded songs library")
        except:
            print("something went wrong")
            pass

        playMusic(sheets,setSpeed())
        

while True:
   
    Run()
    keepContinue = int(input("Press 1 to restart the program: "))
    if keepContinue != 1:
        break
