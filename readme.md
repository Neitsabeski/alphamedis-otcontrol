# READ ME
> PROJECT : Office Tarification Control

                   _       _                              _ _     
             /\   | |     | |                            | (_)    
            /  \  | |_ __ | |__   __ _ _ __ ___   ___  __| |_ ___ 
           / /\ \ | | '_ \| '_ \ / _` | '_ ` _ \ / _ \/ _` | / __|
          / ____ \| | |_) | | | | (_| | | | | | |  __/ (_| | \__ \
         /_/    \_\_| .__/|_| |_|\__,_|_| |_| |_|\___|\__,_|_|___/
                    | |                                           
                    |_|
                                                        by Gardier Sebastien

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Project](#project)
5. [Execution](#execution)
6. [Credits](#credits)

## General Info

### Presentation

Alphamedis needs to automate the process of verifying billing inputs and outputs from the pricing office

### Utility

This utility is able to
- import .csv files
- keep needed content
- formalise content
- compare both content
- export result file

## Technologies

### Utility

* [CSV](https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba)
    Microsoft Excel (inputs)
    * fileA.csv
    * fileB.csv
* [Batch](https://www.tutorialspoint.com/batch_script/index.html)
    (Launcher)
    * Create batch file to have a shortcut to Launch py application
        ```
        @echo off
        mode con: cols=81
        cd /d ".\program"
        "..\python\App\python.exe" ".\main.py"
        pause
        ```
* [Python 3](https://docs.python.org/3/)
    (Utility)
    * [Tkinter](https://docs.python.org/3/library/tkinter.html) 
        : Display Window and widgets
    * [CSV]('')
        : Read lines
        ```
        def read_file_rows(self):
            lines = []
            try:
                with open(self.filepath, 'r') as file:
                    lines = file.readlines()
            ...
        ```
    * [OS](https://docs.python.org/3/library/os.html)
        : Path files
        ```
        file_name = os.path.basename(file_path)
        ```
    * [Date time](https://docs.python.org/3/library/datetime.html)
        : Operation Logs and Date time structure
        ```
        def insert_log(self, data, text_widget):
            now = datetime.datetime.now()
            time = "{}:{}:{}".format(now.hour, now.minute, now.second)
            ...
        ```


### Tools

* [Github](https://github.com/Neitsabeski/alphamedis-otcontrol/) Project Repository
* [IDLE](https://portablepython.com/)
    * [Portable Python 3.10.5](https://sourceforge.net/projects/portable-python/files/Portable%20Python%203.10/)
    * [Portable Python 3.2.5](https://portablepython.com/) Dev version
* [ChatGPT](https://chat.openai.com/) Dev Assistant
* [Draw.io](https://app.diagrams.net/) Analysis diagrams

### Features

* Importing files
* Reading files
* Formalising files
* Comparing files
* Respond object
* Credits formula encoder/decoder
* Config controler
* Changing translation

## Installation

* [Project](https://github.com/Neitsabeski/alphamedis-otcontrol/)
* [Portable Python 3](https://portablepython.com/3.2.5.1/)
    ```
    /!\ Version 3.2.5.1, newest version is dowloadable (3.10.5)
    ```
* [CSV](https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba)
* Config file


## Project

### Repository

Project : https://github.com/Neitsabeski/alphamedis-otcontrol/

### Structure

```
|- utility.shortcut
|- autoRun.bat
|- program /
    |- readme.md
    |- main.py
        |- credits.txt
        |- gui.py
            |- config.py
            |   |- config.json
            |
            |- translations.py
            |- tools.py
            |- files.py
                |- fileA
                |   |- fileA.csv
                |
                |- fileB
                    |- fileB.csv
```


## Execution

1. Prepare input files
2. Settings /optional `"debug": true`
3. Launch utility (i or ii)
    1. Portable Python IDLE
    2. AutoRun
4. Use Utility

## Credits

