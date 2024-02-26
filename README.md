# SkyShettToPiano

## This application is designed specifically for use with the Sky: Children of the Light game available on the Steam demo version.

## [you can test here without game](https://specy.github.io/skyMusic/)
## Prerequisites:
You need to have the following libraries installed:
- [pandas](https://pandas.pydata.org/)
- [keyboard](https://pypi.org/project/keyboard/)

Install them using the following commands in your command line interface:

```cmd
pip install pandas
```

```cmd
pip install keyboard
```

### Before using this application, ensure that Python is installed on your computer.

### Usage:

* Ensure that `SkySheet.py` and `database.csv` are located in the same directory.

* Visit the [Sky Music website](https://sky-music.herokuapp.com/) and navigate to the song library.

* Choose a piece of music to play and click on the download button.

* Proceed to the sheet display section.

* At the bottom of the page, you will find the music sheets. Copy the sheet and paste it into `SkySheet.py`.

* The music sheet will be automatically added to the database, allowing you to use it next time.

* To delete any saved music, open the `database.csv` file and delete the corresponding entry.

* This script automatically presses keys on your keyboard to play the music. If the focus is on a text document, it will type there.

* To stop the script, press the " key 2-3 times.

* First, open the game and equip your instrument.

* Remember, the application simulates key presses. If you attempt to close the game before closing the program, it will continue to press keys, potentially resulting in unexpected behavior.

* To close the program, press the designated key (").


### Türkçe kullanım Rehberi:
*bu uygulamayı ilk açtığınızda sizden tuş atamsı isteyecek eğer linkini verdiğim [bu sitedeki](https://sky-music.herokuapp.com/) piyanoyu kullanıyorsanız tuş atamasına bunu yapıştırın.
```SkySheet.py
q w e r t a s d f g z x c v b
```

* `SkySheet.py` ve `database.csv` dosyalarının aynı dizinde olduğundan emin olun.

* [Sky Müzik websitesine](https://sky-music.herokuapp.com/) gidin ve şarkı kütüphanesine gidin(song library).

* Çalmak istediğiniz bir müzik parçası seçin ve indirme düğmesine tıklayın.

* Ardından, müzik notalarının görüntülendiği bölüme gidin(sheet displayer).

* Sayfanın alt kısmında müzik notalarını bulacaksınız. Notaları kopyalayın ve `SkySheet.py` dosyasına yapıştırın.

* Müzik notaları otomatik olarak veritabanına eklenecek ve bir dahaki sefere kullanabileceksiniz.

* Kayıtlı herhangi bir müziği silmek için `database.csv` dosyasını açın ve ilgili girişi silin.

* Bu betik, müziği çalmak için klavyenizde tuşları otomatik olarak basar eğer pencere odağınız bir metin belgesiyse oraya yazacaktır.

* Betiği durdurmak için " tuşuna 2-3 kez basın.

* İlk olarak, oyunu açın ve enstrümanınızı kuşanın veya bu bağlantıdaki piyano üzerinden [test edin.](https://sky-music.herokuapp.com/)

* Unutmayın, uygulama klavyede tuş basmalarını simüle eder. Programı kapatmadan önce oyunu kapatmaya çalışırsanız, tuşlara basmaya devam eder ve beklenmeyen davranışlara neden olabilir.

* Programı kapatmak için belirtilen tuşa (" tuşuna) basın.
