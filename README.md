# DeskCleaner

This project uses a program named Watchdog which looks for file system events and interacts with the OS file explorer events. Once an a file or folder is modified, the system logs it as an event and matches its extension (with pathlib) to its respectable folder location (i.e file.pdf --> pdf folder, etc). Folders that are repeats are then duplicated numerically (i.e file.png --> duplicate --> file1.png --> file2.png, etc).

Pathlib allows program compatibility across all operating systems.

Contains a separate batch file to run from CLI.

Shutil library allows movement of a file from one location to another.

## Structure

DeskCleaner uses a dictionary of all of the different extensions available for files in the windows OS. It then searches for the matching extension in the modified file and then applies its value which is the rest of the location to the file folders. For example,

 file.png --> loops through dictionary keys of file extensions --> if file>.png< == dict.key --> accesses the values --> ~/Desktop/path/to/your/made/files

 My files were personally structured as:

 C:\Users\User\
--> Desktop 
    --> Roberto
        --> media
            --> audio
                images
                video
        --> other
            --> compressed
                executables
                fonts
                internet
        --> programming
            --> c&c++
                database
                html&css
                javascript
                python
                shell
        --> text
            --> microsoft
                --> excel
                    powerpoint
                    word
                other
                --> system
                pdf
                text

## Sources

1. Resource that helped find all compatible file extensions
    https://www.computerhope.com/issues/ch001789.htm

2. Watchdog Documentation
    https://pythonhosted.org/watchdog/index.html

3. Pathlib Documentation
    https://docs.python.org/3/library/pathlib.html

4. Shutil Documentation
    https://docs.python.org/3/library/shutil.html

