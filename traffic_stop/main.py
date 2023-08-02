interface_wanted = 'eth0'
traffic_limit_GB = 1000
execommand = 'shutdown now'
from datetime import date
import subprocess
import json
def gaintraffic():
    vnprocess = subprocess.run('vnstat --json m ', shell=True,capture_output=True)
    if vnprocess.returncode != 0:
        raise Exception("vnstat error")
    else:
        vnstdout = vnprocess.stdout

    currentmonth = date.today().strftime("%m")
    if currentmonth[0] == '0':
        currentmonth = int(currentmonth[1:])
    currentyear = int(date.today().strftime("%Y"))
    vninterfaces = (json.loads(vnstdout.decode('utf-8')))['interfaces']
    for interface in vninterfaces:
        if interface['name'] == interface_wanted:
            for i in interface['traffic']['month']:
                if i['date']['year'] == currentyear and i['date']['month'] == currentmonth:
                    interface_month_traffic_bytes = int(i['tx'] + i['rx'])
            interface_month_traffic_GB = interface_month_traffic_bytes/1000/1000/1000
            return (interface_month_traffic_GB)

def detect_limit(interface_month_traffic_GB):
    if interface_month_traffic_GB <= traffic_limit_GB:
        print('traffic did not exceed at date %s' % date.today().isoformat(), 'usage: %sGB'% interface_month_traffic_GB)
        return
    else:
        executecommand()

def executecommand():
    subprocess.run(execommand,shell=True)

def main():
    detect_limit(gaintraffic())

main()
