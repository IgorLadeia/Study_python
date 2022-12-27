import os
import shutil
import time
import subprocess
import sys
import multiprocessing

coisa = time.time()

chassis_bus = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_bus'
chassis_truck = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\chassi_truck'
cab = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\cab'
DT_assembly_aud = r"\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\'DT Assembly Audit protocol'"
DT_assembly_axle = r"\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\'DT Axle Assembly'"
DT_assembly_centralgear = r"\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\'DT Centralgear Assembly'"
engine = r'\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim\engine'
destino = r'C:\Users\ifrtef\Desktop\scim'

rotina1 = f"Copy-Item -Path {chassis_bus} -Destination {destino} -Recurse -Force -Passthru"
rotina2 = f"Copy-Item -Path {chassis_truck} -Destination {destino} -Recurse -Force -Passthru"
rotina3 = f"Copy-Item -Path {cab} -Destination {destino} -Recurse -Force -Passthru"
rotina4 = f"Copy-Item -Path {DT_assembly_aud} -Destination {destino} -Recurse -Force -Passthru"
rotina5 = f"Copy-Item -Path {DT_assembly_axle} -Destination {destino} -Recurse -Force -Passthru"
rotina6 = f"Copy-Item -Path {DT_assembly_centralgear} -Destination {destino} -Recurse -Force -Passthru"
rotina7 = f"Copy-Item -Path {engine} -Destination {destino} -Recurse -Force -Passthru"




def worker1(rotina1):
    completed = subprocess.run(["powershell", "-Command", rotina1], capture_output=True)


def worker2(rotina2):
    completed = subprocess.run(["powershell", "-Command", rotina2], capture_output=True)


def worker3(rotina3):
    completed = subprocess.run(["powershell", "-Command", rotina3], capture_output=True)


def worker4(rotina4):
    completed = subprocess.run(["powershell", "-Command", rotina4], capture_output=True)


def worker5(rotina5):
    completed = subprocess.run(["powershell", "-Command", rotina5], capture_output=True)


def worker6(rotina6):
    completed = subprocess.run(["powershell", "-Command", rotina6], capture_output=True)


def worker7(rotina7):
    completed = subprocess.run(["powershell", "-Command", rotina7], capture_output=True)


if __name__ == "__main__":
    print("START")
    #
    # p1 = multiprocessing.Process(target=worker1,args=(rotina1,))
    # p2 = multiprocessing.Process(target=worker2,args=(rotina2,))
    # p3 = multiprocessing.Process(target=worker3,args=(rotina3,))
    # p4 = multiprocessing.Process(target=worker4,args=(rotina4,))
    p5 = multiprocessing.Process(target=worker5,args=(rotina5,))
    p6 = multiprocessing.Process(target=worker6,args=(rotina6,))
    # p7 = multiprocessing.Process(target=worker7,args=(rotina7,))

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    p5.start()
    p6.start()
    # p7.start()
    #
    # print("ID of process p1: {}".format(p1.pid))
    # print("ID of process p2: {}".format(p2.pid))
    # print("ID of process p1: {}".format(p3.pid))
    # print("ID of process p2: {}".format(p4.pid))
    print("ID of process p1: {}".format(p5.pid))
    print("ID of process p2: {}".format(p6.pid))
    # print("ID of process p1: {}".format(p7.pid))

    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    p5.join()
    p6.join()
    # p7.join()

    print("finished execution!")

    # print("Process p1 is alive: {}".format(p1.is_alive()))
    # print("Process p2 is alive: {}".format(p2.is_alive()))
    # print("Process p3 is alive: {}".format(p3.is_alive()))
    # print("Process p4 is alive: {}".format(p4.is_alive()))
    print("Process p5 is alive: {}".format(p5.is_alive()))
    print("Process p6 is alive: {}".format(p6.is_alive()))
    # print("Process p7 is alive: {}".format(p7.is_alive()))

print(time.time() - coisa)
