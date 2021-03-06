import sys
from tools.config_clearer import clear_configs
from tools.rpc_handler import RPC_Handler
from site_packages.termcolor.termcolor import colored, cprint
from tools.justrw import Justrw
from tools.jsonrw import Jsonrw
from datetime import datetime
from tools.error_handler import ErrorLogger

blueln = lambda x: colored(x, "blue")
last_client_id = Justrw("./tools/last_client_id")


def recover():
    config_data = Jsonrw("./tools/configs.json")
    db = {
        "details": None,
        "state": None,
        "start": None,
        "end": None,
        "large_image": None,
        "large_text": None,
        "small_image": None,
        "small_text": None,
        "party_id": None,
        "party_size": None,
        "join": None,
        "spectate": None,
        "match": None,
        "buttons": None,
        "instance": None,
    }
    config_data.write(db)


try:
    if last_client_id.read() == "":
        cprint(
            "\nNever share your {0} to anyone.\nIf you share your client ID to someone, "
            "they {1} at anytime.\nYou won't be able to {2} "
            "as Discord doesn't have any options for it.\n".format(
                blueln("client ID"),
                blueln("can change your presence"),
                blueln("change your client ID"),
            )
        )
        client_id = input("Enter your bot's client ID/application ID\n> ")

    else:
        client_id = last_client_id.read()

    try:
        client_id = int(client_id)
    except ValueError:
        cprint(
            "ā Expected integer. Got {} ".format(colored(client_id, "blue")),
            "red",
        )
    else:
        try:
            rpc = RPC_Handler(client_id)
            cprint("\nā³ Starting RPC status ", "yellow")
            rpc.connect()

        except ConnectionError:
            cprint("ā Discord is not running. RPC connection cannot be started ", "red")

        else:
            cprint("ā Discord is running ", "green")

            try:
                rpc.start()
            except ValueError:
                cprint("ā Client ID is invalid ", "red")
            except AssertionError:
                print("ā Not connected to client ")
            except ConnectionResetError:
                cprint(
                    "ā Connection was reset and couldn't be completed. Maybe the client ID is invalid",
                    "red",
                )
            else:
                cprint(
                    "ā Successfully started RPC status ",
                    "green",
                )

                while 1:
                    try:
                        ran_frm = Justrw("./tools/from")
                        wanted_restart = Justrw("./tools/restarted")
                        if ran_frm.read() == "0":
                            cprint(
                                "* This program wasn't ran from main. Therefore cannot be restarted. ",
                                "yellow",
                            )
                            r = input("\n[E] Exit\n\n> ").lower()
                            if r != "e":
                                continue

                        else:
                            last_client_id.write(str(client_id))
                            print(
                                "\n[PRO!TIP] Change your configuration(./tools/configs.json) and restart to load the new configuration without "
                                "stopping the PRC connection."
                            )
                            r = input(
                                "\n[R] Restart\n[E] Exit\n[C] Reconfigure\n\n> "
                            ).lower()

                        if r.lower() in ("r", "e", "c"):
                            if r == "r":
                                wanted_restart.write("true")
                            elif r == "e":
                                wanted_restart.write("false")
                            else:
                                print("Data has been recovered")
                                recover()
                                wanted_restart.write("true")
                        else:
                            continue

                    except KeyboardInterrupt:
                        pass
                    else:
                        break

except KeyboardInterrupt:
    clear_configs()
    print("\n\nāļø Requested to exit...Exited. ")

except Exception as e:
    if not isinstance(e, KeyboardInterrupt):
        date = str(datetime.utcnow())
        err = ErrorLogger(e)
        err = err.personal_log()
        err = (
            "Filename: {}\n"
            "Error Type: {}\n"
            "Process Type: Child Process\n"
            "Description: {}\n"
            "Line No: {}\n".format(
                err["filename"],
                err["etype"],
                err["des"],
                err["lineno"],
            )
        )
        err = "~~~\n[{}]\n{}\n~~~\n\n".format(date, err)
        log = Justrw("log.txt")
        log.append(err)
        print(
            "\nChild process stopped for an undefined error. This error will be logged.\n"
            "If you want to help, please send the {}(located in current directory) to developer.\n{}\n"
            "".format(
                colored("log.txt", "blue"),
                colored(
                    "(The log does not include any personal information. Not even the directory you're in!)",
                    "yellow",
                ),
            )
        )
        clear_configs()

sys.exit()
