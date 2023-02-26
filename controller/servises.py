from ui.console_interface import show_info


def help_info():
    show_info()


def get_all():
    pass


def get_by_id():
    pass


def add_item():
    pass


def update_item():
    pass


def delete_item():
    pass


SERVICES = {
    0: help_info,
    1: get_all,
    2: get_by_id,
    3: add_item,
    4: update_item,
    5: delete_item
}
