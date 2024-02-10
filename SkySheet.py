import time
import keyboard
import sheets


muzikler = {
    1:sheets.sixMetin,
    2:sheets.six2Metin,
    3:sheets.amelieMetin,
    4:sheets.carolMetin,
    5:sheets.coldMetin,
    6:sheets.naruto,
    7:sheets.japanese,
    8:sheets.stillDRE,
    9:sheets.erased,
    10:sheets.faded,
    11:sheets.canCAnikina,
    12:sheets.harryPotter,
    13:sheets.happyBirthDay,
    14:sheets.deathNote,
    15:sheets.countingStar


}

# def log(name,value):
    
#     dir_path = os.path.dirname(os.path.abspath(__file__))
    
#     log_file_name = "sheets.py"
#     log_file_path = os.path.join(dir_path, log_file_name)
    
#     # Loglama işlemi
#     log_message = f'{name} = """{value}""" '
#     with open(log_file_path, "a", encoding='utf-8') as log_file:
#         log_file.write(log_message + "\n")
    
#     print("Loglama işlemi tamamlandı.")


def geriSay():
    print("başlıyor...")
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

def playMusic(metin,hiz):
    geriSay()

    startTime = time.time()

    metin = metin.replace(".","x").lower()

    sheet = "a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5".split()
    key = "y u ı o p h j k l ş n m ö ç b".split()# buraya kendi klavyenizdeki piyano tuşlarını yazın ("." karakteri desteklenmiyor o yüzden "." olan yeri "b" ile değiştirdim, oyundaki kontrollerden ". notasını b ile değişirin")
    
    for i in range(len(sheet)):
        metin = metin.replace(sheet[i], key[i])


    for i in metin.split():
        if keyboard.is_pressed('"'):
            print('" tuşuna basıldı. Döngü sona eriyor.')
            break
        if i == "x":
            time.sleep(hiz+0.22)  # notalardaki "." olan yerlerde beklenecek süre
            pass
        else:
            for char in i:
                keyboard.press(char)
                print(i)
            time.sleep(hiz)  # Her karakterin ardından girilen hız kadar bekle
            for char in i:
                keyboard.release(char)

    endTime = time.time()
    duration = endTime - startTime
    duration = str(duration)[:4]
    print(f"çalma süresi: {duration} sn")

                

def hizAyarla():
    hiz = float(input("Oynatma hızını giriniz (1,2,3,4,5) (1 hızlı, 5 yavaş)\nÖnerilen 2 veya 3: "))
    if hiz <0 or hiz >=10:
        print("yanlış bir hiz girdiğiniz için hız 3 olarak ayarlandı")
        print("bu hızlar programın çalışmamasına veya aşırı yavaş çalışmasına neden olabilirdi")
        hiz = 3
    hiz = hiz / 10
    print("Hız ayarlandı:", hiz)
    return hiz

    

def programiCalistir():
    print("çalmak istediğiniz müziğin notalarını giriniz (notanız yoksa 0 a basın): ")

    metin = input()
    if metin == "0":
        print("Hazır müziklerden seçin")
        liste = sheets.liste
        print(liste)
        selection = int(input())
        playMusic(muzikler[selection],hizAyarla())
        
    else:
        # name = input("müziğin adını girin: ")
        # log(name,metin)
        playMusic(metin,hizAyarla())
        
        



while True:
   
    programiCalistir()
    devamEt = int(input("Programı yeniden başlatmak için 1'e basın: "))
    if devamEt != 1:
        break
