These are the base packages that are keeping Discord RPC(or the `main.py`) running.
If you are a developer and willing to change or modify the files, please proceed with caution.



# About

#### clear.py
 Clears the entire output of a terminal. It is based on distribution. So if you are on Windows, it will execute `cls` to the terminal and this will clear the whole output. The same goes for Linux with their specific command to clear the output. Currently, it supports only Windows and Unix operating systems.

#### configs.json
 It is the file where all of the user-related data are kept. Users can edit them according to their needs. On every run and restart, those data will be loaded. So that you can edit the data and can restart the script without disconnecting the RPC connection at all. Do check the `https://www.discord.com/developers` to know exactly how to modify the data to get the desired result.

#### error_handler.py
 An error handler module that will handle the error and return the output respecting or omitting user privacy. By default, it is configured to return information related to errors respecting user privacy. The error logs are saved to `log.txt` in the parent folder.

#### from
 This file lets the child program know if it was run from the parent program or from the child program itself.

#### jsonrw.py
 A module for reading and writing a JSON file.

#### justrw.py
 A module for writing string data type to a file.

#### restarted
 This file lets the parent program know if the child program requested restart or exit.

#### rpc_handler
 This is the main module that controls the entire connection to the Discord application.



# Credit

This program was never possible without these open-source packages. Thanks to the devs for making it this far!

#### **Packages used in this project**
> *PyPresence*\
> *Termcolor*
