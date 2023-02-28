from screeninfo import get_monitors


# TODO 1: Взять ширину и высоту основного монитора
def get_resolution():
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor.width, monitor.height
