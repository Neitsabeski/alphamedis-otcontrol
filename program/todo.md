# TO DO LIST
> PROJECT : Office Tarification Control

## README
- [ ] Create MD readme to project

## MAIN
### Credits
- [x] Import read and display Credits
- [ ] Function to draw credits
- [ ] If not exist, create credits 

## CONFIG
- [x] Config class
- [x] Import settings from a config file
- [x] If not exist, create a config file
- [x] Change settings
- [x] Debug
- [ ] Convert file format
    `config.json -> config.cfg`

## GUI
- [x] Create a window interface
- [x] section
- - [x] Label
- - [x] Path
- - [x] Import file
- - [x] Formalise
- - - [ ] Display effective rows
- - [x] Logs
- - [x] Compare
- [x] Dialogs
- [x] Info Hover widgets
- [x] Change translation
- [ ] Use respond object

### TOOLS
- [x] Class tools

## TRANSLATION
- [x] Add translations file
- [ ] Convert file format
    `translation.py -> translation.json`
- [ ] Create class translation
- [ ] Hide exception lang
- [ ] Function default translation if translation not exist
- [ ] Edit structure
    - before
        ```
        section 1
            element
                lang_1
                    translation
                lang_2
                    translation
        section 2
            ...
        ```
    - after
        ```
            lang_1
                section 1
                    element
                        translation
                section 2
                    ...
            lang_2
                ...
        ```

## FILES
- [x] Create class
- [x] Show infos
- [x] Formalise
- - [ ] row in matrix() 
- - [ ] FOR ROW : If cell is empty, continue
- [x] Static method compare files
- [ ] Add respond to functions
- [ ] Function to use in formalise

### OBJECT RESPOND
- [ ] Create class

### CLASS FILEA
- [ ] Formalise function

### CLASS FILEB
- [X] Formalise function
