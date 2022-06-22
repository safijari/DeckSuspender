import os
import time

# try:
#     os.unlink("/tmp/report")
# except Exception:
#     pass

# def indicate(msg):
#     with open("/tmp/report", "a") as f:
#         f.write(str(time.time()) + " " + msg + "\n")
import sys

sys.path.append("/home/deck/.local/lib/python3.10/site-packages/")
import psutil

# indicate("loaded psutil")

import json

from pprint import pprint
import sys
import signal
import os
import itertools


def get_first_match(substr):
    for child in psutil.process_iter():
        if (
            substr in child.name().lower()
            or substr in " ".join(child.cmdline()).lower()
        ) and ("reaper SteamLaunch" in child.cmdline()):
            return child


def get_all_steam_apps():
    res = []
    for child in psutil.process_iter():
        if "reaper" == child.name() and "SteamLaunch" in child.cmdline():
            res.append(child)
    return res


# indicate("got to class")
class Plugin:
    async def kill(self, pid, cmd):
        proc = psutil.Process(pid)
        sig = signal.SIGSTOP if cmd == "stop" else signal.SIGCONT
        for child in proc.children(recursive=True):
            os.kill(child.pid, sig)
        os.kill(proc.pid, sig)

    async def get_procs(self):
        # indicate("called get procs")
        apps = get_all_steam_apps()
        # indicate(str(apps))
        return json.dumps([[app.pid, app.cmdline()[-1], app.status()] for app in apps])

    async def _main(self):
        pass
