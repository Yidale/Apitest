#codin:utf-8


class global_var:
    ID = 0
    name = 1
    run = 2
    url = 3
    request_way = 4
    header = 5
    depend_id = 6
    depend_data = 7
    depend_val = 8
    request_val = 9
    expect = 10
    result = 11


def get_id():
    return global_var.ID


def get_name():
    return global_var.name


def get_run():
    return global_var.run


def get_url():
    return global_var.url


def get_request_way():
    return global_var.request_way


def get_header():
    return global_var.header


def get_depend_id():
    return global_var.depend_id


def depend_data():
    return global_var.depend_data


def depend_val():
    return global_var.depend_val


def request_val():
    return global_var.request_val


def expect():
    return global_var.expect


def result():
    return global_var.result

def head_value():
    header = {
        "UserInfo": "hIS%2FHeyHeVjdQy9KipWYJCcEaw9HZg%2FGDO8cq2IVdRYmR475itRzJCYXIPE6rgqgsJgFYrKkqE1BQbmppys%2BaPi%2FciXr9e4SFK7XsbGRmsM%3D",
        "smidV2": "201803152041205e8daffc2c5c1537590e1d9a4d79c2e000fc5afe8625d3170",
        "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1521260348",
        "kd_user_id": "5857de9a-0876-4d3e-9fca-9e40c05687eb",
        "dc_session_id": "10_1521259762863.151357",
        "uuid_tt_dd": "-193880757346153672_20170530",
        "UserName": "Yi_da"
    }

print(type(get_id()))
