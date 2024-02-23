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

* This script simulates key presses on your keyboard to play the music.

* To stop the script, press the " key 2-3 times.

* First, open the game and equip your instrument.

* Then, you can start using the application.

* Remember, the application simulates key presses. If you attempt to close the game before closing the program, it will continue to press keys, potentially resulting in unexpected behavior.

* To close the program, press the designated key (").

[![GitHub Views](https://komarev.com/ghpvc/?username=MERT-CKR&label=Repo+Views)](https://github.com/MERT-CKR/SkyShettToPiano)
