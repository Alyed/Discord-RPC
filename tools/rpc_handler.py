class RPC_Handler:
    from site_packages.pypresence.exceptions import InvalidPipe, InvalidID
    from site_packages.pypresence import Presence
    from tools.jsonrw import Jsonrw

    def __init__(self, client_id: int):
        self.__rpc = RPC_Handler.Presence(client_id)
        self.__status = False

    def connect(self):
        if not self.__status:
            try:
                self.__rpc.connect()

            except RPC_Handler.InvalidPipe:
                raise ConnectionError("Discord is not running")

            except Exception as e:
                if not isinstance(e, RPC_Handler.InvalidID):
                    raise e

        else:
            print("❗Already connected")

    def start(self):
        configs = RPC_Handler.Jsonrw("./tools/configs.json").read()

        try:
            self.__rpc.update(
                state=configs["state"],
                details=configs["details"],
                start=configs["start"],
                end=configs["end"],
                large_image=configs["large_image"],
                large_text=configs["large_text"],
                small_image=configs["small_image"],
                small_text=configs["small_text"],
                party_id=configs["party_id"],
                party_size=configs["party_size"],
                join=configs["join"],
                spectate=configs["spectate"],
                match=configs["match"],
                buttons=configs["buttons"],
                instance=configs["instance"],
            )

        except AssertionError:
            raise AssertionError("Are you connected to the client?")

        except RPC_Handler.InvalidID:
            raise ValueError("Invalid client ID")

        else:
            self.__status = True

    def close(self):
        if self.__status:
            self.__rpc.close()
        else:
            print("❗RPC Status is already turned off")
