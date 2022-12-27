import os
import shutil
import time
import subprocess
import sys
import multiprocessing

tempo00 = time.time()

chassis_bus = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_bus'
chassis_truck = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_truck'


rotina1 = f"Copy-Item -Path {chassis_bus} -Destination {destino} -Recurse -Force -Passthru"
rotina2 = f"Copy-Item -Path {chassis_truck} -Destination {destino} -Recurse -Force -Passthru"

def worker1(rotina1):
    completed = subprocess.run(["powershell", "-Command", rotina1], capture_output=True)


def worker2(rotina2):
    completed = subprocess.run(["powershell", "-Command", rotina2], capture_output=True)


if __name__ == "__main__":
    print("START")

    p1 = multiprocessing.Process(target=worker1,args=(rotina1,))
    p2 = multiprocessing.Process(target=worker2,args=(rotina2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    print("finished execution!")

    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))

    print(time.time() - tempo00)