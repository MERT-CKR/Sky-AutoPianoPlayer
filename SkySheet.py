import time
import keyboard

print("çalmak istediğiniz müziğin notalarını giriniz (notanız yoksa 0 a basın): ")

sixMetin = """ 
A3B3 . B2 . A3B1 . A3B3 . B2 . A3B1 . A3B2 . B1 . A3A5 . A3B2 . B1 . A3A5 . A1B5 . B4 . A3B3 . A1B5 . B4 . A3B3 . A3B4 . B3 . A3B2 . A3B4 . B3 . A3B2 . A2C1 . B5 . A3B2 . A2C1 . B5 . A3B2 . 
B1B5 . 
A4B4 . 
A3B3 . 
A2B2 . 
A3B1 A5 B1 B2 A3B3 B2 B1 A5 A3B1 A5 B1 B2 A3B3 B2 A5 B2 A1A3 A1 A3 A1 A3 A1 A3A5 . A1A3 A1 A3 A1 A3 A1 A3 A1 B1B3 B2 B3 B4 B3B5 B4 B3 B2 B1B3 B2 B3 B4 B3B5 B4 B3 B2 B1B5 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 A2C1 B5 A4B4 B5 A3B2 . B1 A2C1 B5 A4B4 B5 A4B4 B3 A2B2 B1 A1B1B5 . A4B1B4 . A2B1C1 . B1B5C3 . A3B3 . B2 . A2B1 . A3B3 . B2 . A2B1 . A3B2 . B1 . A3A5 . A3B2 . B1 . A3A5 . A1B5 . B4 . A3B3 . A1B5 . B4 . A3B3 . A3B4 . B3 . A3B2 . A3B4 . B3 . A3B2 . A2C1 . B5 . A3B2 . A2C1 . B5 . A3B2 . 
B1B5 . A4B4 . A3B3 . A2B2 . 
A3B1 A5 B1 B2 A3B3 B2 B1 A5 A3B1 A5 B1 B2 A3B3 B2 A5 B2 A1A3 A1 A3 A1 A3 A1 A3A5 . A1A3 A1 A3 A1 A3 A1 A3 A1 B1B3 B2 B3 B4 B3B5 B4 B3 B2 B1B3 B2 B3 B4 B3B5 B4 B3 B2 B1B5 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 B1 A3 A2C1 B5 A4B4 B5 A3B2 . B1 A2C1 B5 A4B4 B5 A4B4 B3 A2B2 B1 A1B1B5 . A4B1B4 . A2B1C1 . B1B3B5C3
"""

six2Metin = """ 
B1B3 . B2 . A3B1 . B1B3 . B2 . A3B1 . 
A3B2 . B1 . A3A5 . 
A3B2 . B1 . A3A5 . A1B5 . B4 . A3B3 . A1B5 . B4 . A3B3 . A3B4 . B3 . A5B2 . A3B4 . B3 . A5B2 . A4C1 . B5 . B1B2 . A4C1 . B5 . B1B2 . A3B5 . B1B4 . A3B3 . A3B2 . A3B1 A5 B1 B2 A3B3 B2 B1 A5 A3B1 A5 B1 B2 A3B3 B2 B1 B2 A3 . 
A5 . A3 . A3 . A1B3 B2 A3B3 B4 A5B5 B4 A3B3 B2 A1B3 B2 A3B3 B4 A5B5 B4 A3B3 B2 A3B5 . A5 . A4C1 B5 B1B4 B5 B2 . B1 A4C1 B5 B1B4 B5 B4 B3 B2 B1 A3B5 . B4 . A3B3 . B2 . A3B1B3 . B2 . A3B1 . B1 . A3B1B3 . B2 . A3B1 . B1 . A3A5B2 . B1 . A3A5 . A3 . A3B2 . B1 . A3A5 . A3 . A1A3B5 . B4 . A3B3 . A1 . A1A3B5 . B4 . A3B3 . A1 . A3A5B4 . B3 . A5B2 . A3 . A3A5B4 . B3 . A5B2 . A3 . A4B1C1 . B5 . A4B2 . B1 . A4B1C1 . B5 . A4B2 . B1 . A3B1B5 . B4 . A3B3 . B2 . A3B1 A5 B1 B2 A3B3 B2 B1 A5 A3B1 A5 B1 B2 A3B3 B2 B1 B2 A3 . A3 . A5 . A3 . A3 . A1B3 B2 A3B3 B4 A5B5 B4 A3B3 B2 A1B3 B2 A3B3 B4 A5B5 B4 A3B3 B2 A3B5 . A5 . B2 . A3B5 . A5 . A4C1 B5 B1B4 B5 B1 . B1 A4C1 B5 B1B4 B5 B4 B3 A4B2 B1 A3B5 . B1B4 . A3B3 . B2 . B3C5 . B2C4 . B1C3 . B3C5 . B2C4 . B1C3 . B2C4 . B1C3 . A5C2 . B2C4 . B1C3 . A5C2 . A3B5 . A2B4 . A1B3 . A3B5 . A2B4 . A1B3 . A2B4 . A1B3 . B2 . A2B4 . A1B3 . B2 . A4C1 . A3B5 . B2 . A4C1 . A3B5 . B2 . A3B5 . A2B4 . A1B3 . B2 . B1


"""

amelieMetin = """
A1 . A3B3 B2 B1B3 . B5A3 C1 B5A1 A3 B1 A3 . A1 A3B2 B1 A5B2 B3A3 B4 A1B3 . A5 A3 . B2 B2A3 B1 B2A5 B5A3 C1 B5B2 A3 A5 A3 . B2 B2A2 B1 B2A5 A2 B2 A2 . A5 A2 . 
A1C3 . A3 B1 A3B5 . A1 . A3 . B1 A3 . C2 A1 . A3 A5 A3B5 A1 . A3 A5 A3 . B2C4 . A3 A5 B5A3 B2 A3 A5 C2A3 C3 . C4B2 A2 . A5 . A2B4 B2 A2 . A5 A2 . C5A1 A3 B1 C3A3 . A1 A3 B1 A3 A1C5 A3 A5 C2A3 A1 A3 A5 A3 B2C4 A3 A5 C2A3 B2 A3 A5 A3C2 C3 B2C4 A2 . A5 A3C2 . A2 . B2 A2 . A5 . A2 . A1 A3 B1
"""
carolMetin = """
C5 C4 C5 C3 C5 C4 C5 C3 C5 C4 C5 C3 C5 C4 C5 C3 C1C5 C4 C5 C3 B5C5 C4 C5 C3 B4C5 C4 C5 C3 B3C5 C4 C5 C3 B1B5 B4 B5 B3 A5B5 B4 B5 B3 A4B5 B4 B5 B3 A3B5 B4 B5 B3 B1B5 B4 B5 B3 A5B5 B4 B5 B3 A4B5 B4 B5 B3 A3B5 B4 B5 B3 B3C3 B3C3 B3C3 B2C2 B1C1 A5B5 A5B5 A5B5 A4B4 A3B3 A4B4 A4B4 A4B4 A5B5 A4B4 A3B3 A2B2 A3B3 A1B1 A3 A4 A5 B1 B2 B3 B4 B5 B4 B3 A4 A5 B1 B2 B3 B4 B5 B5 B4 B3 B3 B2 B3 B1 B3 B2 B3 B1 B3 B2 B3 . A1 A3 B1 . B3C3 B2C2 B1C1 A5B5 A4B4 A3B3 A2B2 A3B1 B3C3
"""

coldMetin = """
A4B1 A4B1 A4B1 A4B1 A5B2 A5B2 A5B2 A5B2 A1A5 A1A5 A1A5 A1A5 A3B1 A3B1 A3B1 A3B1 A1A4B1 A1A4B1 A1A4B1 A1A4B1 A2A5B2 A2A5 A2A5 A2A5B2 A1A3A5 A1A3A5 A1A3A5 A1A3A5 A1A3B1 A1A3B1 A1A3B1 A1A3B1B5 A1A3B1B5 A1A3B1B5 A1A4B1B5 A1A4B1B5 A1A4B1 A1A4B1C1 A2A5B2B4 A2A5B2 A2A5B2 A2A5B2B4 A2A5B2B4 A2A5B2B3 A1A3A5B4 A1A3A5B4 A1A3A5B3 A1A3A5B4 A1A3A5B5 A1A3A5B3 A1A3B2 A1A3B1 A1A3B5 A1A3B5 A1A3B5 A1A4B1B5 A1A4B1 A1A4B1 A1A4B1 C1 A1A4B1 A2A5B4 A2A5B2 A2A5B2 A2B4 A2A5B2 A2A5B2 A2A5B2B3 B3 B5 A1A3A5B5 A1A3A5B3 A1A3A5B5 A1A3A5 A1A3A5B5 A1A4B1B4 B3 A1A4B1B3 A1A3B1 A1A3B1 A1A3B1 B1 A1A3B1 A1A4B1 A1A4B1 A1A4B1 A4B1B5 A2A4B2 A2A5B2C2 A2A5B2 A2A5B2 A2A5B2 C2 A2A5B2C2 A2A5B2C2 A1A3A5C2 A1A3A5 A1A3A5B5 A5 A1A3A5C2 A1A3A5C1 A1A3B1B5 A3B1B5 A1A4B1B5 A1A4B1B5 A1A4B1B5 A1A4B1B5 A4 A1B1B5 B5 A1A4B1 C1 A2A5B2 B4 A2A5B2 A2A5B2 A2A5B2 A2A5B2B3 B3 A1A3A5B5 B4 A1A3A5B3 A1A3A5B3 A1A3A5 B5 B1 A1A3B4 B1B3 A1A3B1B3 A1A3B1B3 A1A3B1 A1A3B1 A1A3B1 B3 A1A4B1B3 A4 A1A4B1 A1A4B1 C2 A1A4B1 A2A5B2C2 A2A5B2C2 A2A5B2B4 A2A5B2B5 A2A5B2C1
"""

metin = input()
if metin == """0""":
    print("Hazır müzkilerden seçin")
    liste = ("1. Little Nightmares six's Music box\n2. Six's Music box(V2)\n3. Amelie\n4. Carol of the bells\n5. Coldplay: Viva la Vida (1,2,3,4,5)")
    print(liste)
    selection = int(input())
    print("oynatma hızını giriniz")
    hiz = float(input("Hızı girin:1,2,3,4,5 \nÖnerilen 2 veya 3: "))
    hiz = hiz/10
    print(hiz)
    print("başlıyor...")
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    
    
    if selection == 1:
        metin = sixMetin 
    elif selection == 2:
        metin = six2Metin
    elif selection == 3:
        metin = amelieMetin
    elif selection == 4:
        metin = carolMetin
    elif selection == 5:
        metin = coldMetin

metin = metin.replace(".","x").lower()



sheet = "a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5".split()
key = "y u ı o p h j k l ş n m ö ç b".split()


for i in range(len(sheet)):
    metin = metin.replace(sheet[i], key[i])


# print(metin.split())

for i in range(len(sheet)):
    metin = metin.replace(sheet[i], key[i])


# print(metin.split())

for i in metin.split():
    if i == "x":
        time.sleep(0.5)
        pass
    else:
        for char in i:
            keyboard.press(char)
        time.sleep(0.3)  # Her karakterin ardından 0.1 saniye bekle
        for char in i:
            
            keyboard.release(char)
            print(i)

input()