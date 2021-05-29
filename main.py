import os, sys
from tools.config_clearer import clear_configs
from tools.justrw import Justrw
from tools.jsonrw import Jsonrw
from tools.clear import clear
from site_packages.termcolor.termcolor import cprint, colored
from datetime import datetime
from tools.error_handler import ErrorLogger

try:
    while 1:
        data = Justrw("./tools/restarted")
        frm = Justrw("./tools/from")
        frm.write("main")
        if data.read() == "true":
            data.write("false")
            clear()
            print(f"{os.getcwd()}>")
            cprint("✔ Restarted successfully ", "green")

        exit_status = os.system("python3 ./.runner.py")

        if exit_status not in (2, 0):
            print("❌ The program stopped with some other error. ")
            break

        else:
            if Justrw("./tools/restarted").read() == "true":
                continue
            break

except Exception as e:
    date = str(datetime.utcnow())
    err = ErrorLogger(e)
    err = err.full_log()
    err = (
        "Filename: {}\n"
        "Error Type: {}\n"
        "Process Type: Parent Process\n"
        "Description: {}\n"
        "Line No: {}".format(err["filename"], err["etype"], err["des"], err["lineno"])
    )
    err = "~~~\n[{}]\n{}\n~~~\n\n".format(date, err)
    log = Justrw("log.txt")
    log.append(err)
    print(
        "\nParent program stopped for an undefined error. This error will be logged.\n"
        "If you want to help, please send the {}(located in current directory) file to developer.\n{}\n"
        "".format(
            colored("log.txt", "blue"),
            colored(
                "(The log does not include any personal information. Not even the directory you're in!)",
                "yellow",
            ),
        )
    )

else:
    sys.exit()
finally:
    clear_configs()
