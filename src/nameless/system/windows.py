from nameless.system.base import System


class WindowsSystem(System):
    """Windows backend. Not implemented yet.

    To port it, override open_app, notify, and _set_volume.
    Override _set_volume, not set_volume, so the 0-100 clamping in base.py applies.
    """

    name = "Windows"
