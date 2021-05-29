from tools.justrw import Justrw


def clear_configs():
    _from = Justrw("./tools/from")
    last_client_id = Justrw("./tools/last_client_id")
    restarted = Justrw("./tools/restarted")

    _from.write("0")
    last_client_id.write("")
    restarted.write("false")
