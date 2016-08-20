import visa
# visa.log_to_screen()

rm = visa.ResourceManager('PowerMeter HP 437B.yaml@sim')

resource_name = "GPIB0::11::65535::INSTR"
inst = rm.open_resource(resource_name, read_termination='\n', write_termination='\r\n' if resource_name.startswith('ASRL') else '\n')

print(inst.query('*IDN?'))

print(inst.query("?"))

print(inst.write(":SIM:SET:power -1.234"))
print(inst.query("?"))
