import visa
import traceback
import sys
# visa.log_to_screen()

rm = visa.ResourceManager('default.yaml@sim')
# print(rm.list_resources())

print(rm)

'''
Using a clean pyvenv with Python 3.5.1+ on Ubuntu 16.04
venv/bin/activate
pip install pyvisa-sim
wget [hgrecco/pyvisa-sim/master/pyvisa-sim/default.yaml](https://raw.githubusercontent.com/hgrecco/pyvisa-sim/master/pyvisa-sim/default.yaml)

'''

# list_resources to not probe
listv = [
    'ASRL1::INSTR',
    'USB0::0x1111::0x2222::0x1234::0::INSTR',
    'TCPIP0::localhost::inst0::INSTR',
    'TCPIP0::localhost::10001::SOCKET',
    'GPIB0::8::65535::INSTR',
    'USB0::0x1111::0x2222::0x4445::RAW',
]

print(listv)
lists = []
for item in rm.list_resources():
    lists.append(item)
    # Append items to a mutable list

for item in listv:
    # print(item)
    if item in lists:
        # print(item)
        lists.remove(item)
        # Remove items in listv from the lists


for resource_name in lists:
    print("\n......................")
    inst = rm.open_resource(resource_name, read_termination='\n', write_termination='\r\n' if resource_name.startswith('ASRL') else '\n')
    # inst = rm.open_resource(each)
    print(resource_name)
    print(inst)

    try:
        print(inst.query('*IDN?'))
        # print(inst.read())  # HP 437B returns measurement with a inst.read()
    except visa.VisaIOError:  # This was found with print(dir(visa))
        traceback.print_exc(file=sys.stdout)
    print()
print("...")
