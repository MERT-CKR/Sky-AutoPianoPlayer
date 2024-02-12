# SkyShettToPiano

## This application is designed specifically for use with the Sky: Children of the Light game available on the Steam demo version.

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

### Usage:

1. Ensure that `SkySheet.py` and `database.csv` are located in the same directory.

2. Visit the [Sky Music website](https://sky-music.herokuapp.com/) and navigate to the song library.

3. Choose a piece of music to play and click on the download button.

4. Proceed to the sheet display section.

5. At the bottom of the page, you will find the music sheets. Copy the sheet and paste it into `SkySheet.py`.

6. The music sheet will be automatically added to the database, allowing you to use it next time.

7. To delete any saved music, open the `csv` file and delete the corresponding entry.

8. This script simulates key presses on your keyboard to play the music.

9. To stop the script, press the " key 2-3 times.

10. First, open the game and equip your instrument.

11. Then, you can start using the application.

12. Remember, the application simulates key presses. If you attempt to close the game before closing the program, it will continue to press keys, potentially resulting in unexpected behavior.

13. To close the program, press the designated key (").
