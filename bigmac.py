import random
import subprocess
import getopt
import sys

net_adapter = sys.argv[1]

change = 0;

if(len(sys.argv) >= 3):
    change = sys.argv[2]

def new_mac():
    mac = [
            0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)
        ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

cat_args = "/sys/class/net/" + net_adapter + "/address"

old_mac = subprocess.Popen(["cat", cat_args], stdout=subprocess.PIPE)
(curr_mac, err) = old_mac.communicate()


if(change and change == "new"):
    # execute code for mac change with subprocess

if(!change):
    print curr_mac

