import sys
from tools.rpc_handler import RPC_Handler
from site_packages.termcolor.termcolor import colored, cprint
from tools.justrw import Justrw
from tools.jsonrw import Jsonrw
from datetime import datetime
from tools.error_handler import ErrorLogger

blueln = lambda x: colored(x, "blue")
configs = Jsonrw("./tools/configs.json")

try:
    if configs.read()["last_client_id"] is None:
        cprint(
            "\nNever share your {0} to anyone.\nIf you share your client ID to someone, "
            "they {1} at anytime.\nYou won't be able to {2} "
            "as Discord doesn't have any options for it.\n".format(
                blueln("client ID"),
                blueln("can change your presence"),
                blueln("change your client ID"),
            )
        )
        client_id = input("Enter your bot's client ID\n> ")

    else:
        client_id = configs.read()["last_client_id"]

    try:
        client_id = int(client_id)
    except ValueError:
        cprint(
            "❌ Expected integer. Got {} ".format(colored(client_id, "blue")),
            "red",
        )
    else:
        try:
            rpc = RPC_Handler(client_id)
            cprint("\n⏳ Starting RPC status ", "yellow")
            rpc.connect()

        except ConnectionError:
            cprint("❌ Discord is not running. RPC connection cannot be started ", "red")

        else:
            cprint("✔ Discord is running ", "green")

            try:
                rpc.start()
            except ValueError:
                cprint("❌ Client ID is invalid ", "red")
            except AssertionError:
                print("❌ Not connected to client ")
            else:
                cprint(
                    "✔ Successfully started RPC status ",
                    "green",
                )

                while 1:
                    try:
                        ran_frm = Justrw("./tools/from")
                        data = Justrw("./tools/restarted")
                        if ran_frm.read() == "0":
                            cprint(
                                "* This program wasn't ran from main. Therefore cannot be restarted. ",
                                "yellow",
                            )
                            r = input("\n[E] Exit\n\n> ")
                        else:
                            d = configs.read()
                            d["last_client_id"] = client_id
                            configs.write(d)
                            print(
                                "\n[PRO!TIP] Change your configuration file(./tools/configs.json) and restart to load the new configuration without "
                                "stopping the PRC connection."
                            )
                            r = input("\n[R] Restart\n[E] Exit\n\n> ").lower()

                        if r.lower() in ("r", "e"):
                            if r == "r":
                                data.write("true")
                            else:
                                data.write("false")
                        else:
                            continue

                    except KeyboardInterrupt:
                        pass
                    else:
                        break

except KeyboardInterrupt:
    print("\n\n✔️ Requested to exit...Exited. ")

except Exception as e:
    if not isinstance(e, KeyboardInterrupt):
        date = str(datetime.utcnow())
        err = ErrorLogger(e)
        err = err.personal_log()
        err = (
            "Filename: {}\n"
            "Error Type: {}\n"
            "Process Type: Parent Process\n"
            "Description: {}\n"
            "Line No: {}".format(
                err["filename"], err["etype"], err["des"], err["lineno"]
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

sys.exit()
