import time
import keyboard
import pandas as pd
import json


data = pd.read_csv("database.csv")

def bring(id):
    sheet_value = data.loc[id-1, 'sheet']
    return sheet_value

def showList():
    column_values = data["name"].tolist()
    for i, value in enumerate(column_values):
        # Her bir değerin ID'si +1 artsın (index 0 dan başladığı için)
        id = i + 1
        print(f"{id}: {value}")

def write(name, sheet):
    global data
    id = data['ID'].max() + 1
    new_data = pd.DataFrame({"ID": [id], "name": [name], "sheet": [sheet]})
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv("database.csv", index=False)


def countDown():
    print("başlıyor...")
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
    key = "y u ı o p h j k l ş n m ö ç b".split()# buraya kendi klavyenizdeki piyano tuşlarını yazın ("." karakteri desteklenmiyor o yüzden "." olan yeri "b" ile değiştirdim, oyundaki kontrollerden ". notasını b ile değişirin")
    for i in range(len(cords)):
        sheets = sheets.replace(cords[i], key[i])


    for i in sheets.split():
        if keyboard.is_pressed('"'):
            print('" tuşuna basıldı. Döngü sona eriyor.')
            break
        if i == "x":
            time.sleep(speed+0.22)  # notalardaki "." olan yerlerde beklenecek süre
            pass
        else:
            for char in i:
                keyboard.press(char)
                print(i)
            time.sleep(speed)  # Her karakterin ardından girilen hız kadar bekle
            for char in i:
                keyboard.release(char)

    endTime = time.time()
    duration = endTime - startTime
    duration = str(duration)[:4]
    print(f"çalma süresi: {duration} sn")

                

def setSpeed():
    speed = float(input("Oynatma hızını giriniz (1,2,3,4,5) (1 hızlı, 5 yavaş)\nÖnerilen 2 veya 3: "))
    if speed <0 or speed >=10:
        print("yanlış bir hız girdiğiniz için hız 3 olarak ayarlandı")
        print("bu hızlar programın çalışmamasına veya aşırı yavaş çalışmasına neden olabilirdi")
        speed = 3
    speed = speed / 10
    print("Hız ayarlandı:", speed)
    return speed

    

def Run():
    print("çalmak istediğiniz müziğin notalarını giriniz (notanız yoksa 0 a basın): ")

    sheets = input()
    if sheets == "0":
        print("Hazır müziklerden seçin")
        showList()
        selection = int(input())
        playMusic(bring(selection),setSpeed())
        
    else:
        name = input("müziğin adını girin: ")
        try:
            write(" "+name, sheets)
            print("Hazır Müziklere eklendi")
        except:
            print("notalar kaydedilirken bir sorun oluştu")
            pass

        playMusic(sheets,setSpeed())
        

while True:
   
    Run()
    keepContinue = int(input("Programı yeniden başlatmak için 1'e basın: "))
    if keepContinue != 1:
        break
