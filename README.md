# Sky-AutoPianoPlayer

## This application is designed specifically for use with the Sky: Children of the Light game available on the Steam demo version.

## [you can test here without game](https://specy.github.io/skyMusic/)
## Prerequisites:
You need to have the following libraries installed:
- [pandas](https://pandas.pydata.org/), [keyboard](https://pypi.org/project/keyboard/)

Install them using the following commands in your command line interface:

```cmd
pip install pandas
```

```cmd
pip install keyboard
```

### Before using this application, ensure that Python is installed on your computer.

### Usage:

* When you first open this application, it will prompt you for key assignments. 
* If you are using the piano from [this site](https://sky-music.herokuapp.com/), paste the key assignments as follows:
```
q,w,e,r,t,a,s,d,f,g,z,x,c,v,b
```
* If you are using the in-game piano, list the letters written on the keys separated by commas.
Note: if there is a dot or comma ('.' ',' ',') character between the piano keys in the game, replace it with other keys, suggestion 'b' key
```
a,s,d,f,g,h,j,k,l
```

* If you input the keys incorrectly, you can run `reset_key_settings.py`, which will prompt you to enter the keys again.

* In the next step, the program will ask you to choose a ready-made music or enter notes manually.
* You can select a piece of music from the ready-made options or learn where to find the notes in the following step:

* Go to the [Sky Music website](https://sky-music.herokuapp.com/), select the song library from the hamburger menu.
Choose a piece of music to play and click on the download button.
Proceed to the sheet display section.
At the bottom of the page, you will find the sheet musics. Copy the sheet music and paste it into `SkySheet.py`.
The  sheet music will be automatically added to the database, allowing you to use it next time.

* To delete any saved music, open the `database.csv` file and delete the corresponding entry. It's recommended to do this using `VS CODE`.

* This script simulates key presses on your keyboard to play the music. 
* If the focus is on a text document, it will type there.

* To stop the script, press the " key 2-3 times.

* First, open the game and equip your instrument or [test it on this piano](https://sky-music.herokuapp.com/).

* Remember, the application simulates key presses. If you attempt to close the game before closing the program,  it will continue to press keys, potentially resulting in unexpected behavior.

* To close the program, press the designated key (").


# Türkçe kullanım Rehberi:
* bu uygulamayı ilk açtığınızda sizden tuş atamsı isteyecek eğer linkini verdiğim [bu sitedeki](https://sky-music.herokuapp.com/) piyanoyu kullanıyorsanız tuş atamasına bunu yapıştırın. 
```SkySheet.py
q,w,e,r,t,a,s,d,f,g,z,x,c,v,b
```
* eğer oyundaki piyanoyu kullanıyorsanız tuşların üzerinde yazan harfleri aralarında virgül ile yazın.
 Not: eğer oyundaki piyano tuşlarının arasında nokta veya virgül('.' ',') karakteri varsa bunu başka tuşlarala değiştirin öneri 'b' tuşu

* tuşları yanlış girdiyseniz`reset key settings.py` dosyasını çalıştırabilirsiniz, bu sizden tekrar tuş girmenizi isteyecektir

* sonraki adımda program sizden hazır müziklerden birini seçmenizi veya nota girmenizi isteyecek,hazır müziklerden birini seçebilirsiniz veya aşağıdaki adımda notaları nereden bulacağınızı öğrenebilirsiniz 

* [Sky Müzik websitesine](https://sky-music.herokuapp.com/) gidin hamburger menüsünden song library bölümünü seçin.
Çalmak istediğiniz bir müzik parçası seçin ve indirme düğmesine tıklayın.
Ardından, müzik notalarının görüntülendiği bölüme gidin(sheet displayer).
Sayfanın alt kısmında müzik notalarını bulacaksınız.
Notaları kopyalayın ve `SkySheet.py` dosyasına yapıştırın.
Müzik notaları otomatik olarak veritabanına eklenecek ve bir dahaki sefere kullanabileceksiniz.

* Kayıtlı herhangi bir müziği silmek için `database.csv` dosyasını açın ve ilgili girişi silin, bu işlemi `VS CODE` üzerinden yapmanız önerilir.

* Bu betik, müziği çalmak için klavyenizde tuşları otomatik olarak basar eğer pencere odağınız bir metin belgesiyse oraya yazacaktır.

* Betiği durdurmak için " tuşuna 2-3 kez basın.

* İlk olarak, oyunu açın ve enstrümanınızı kuşanın veya bu bağlantıdaki piyano üzerinden [test edin.](https://sky-music.herokuapp.com/)

* Unutmayın, uygulama klavyede tuş basmalarını simüle eder. Programı kapatmadan önce oyunu kapatmaya çalışırsanız, tuşlara basmaya devam eder ve beklenmeyen davranışlara neden olabilir.

* Programı kapatmak için belirtilen tuşa (" tuşuna) basın.
