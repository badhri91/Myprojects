#!/usr/bin/env python3

switch = { 'hostname':'swi', 'ip':'10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}
print (switch['hostname'])
print(switch['ip'])




print("First test - .get()")
print(switch.get('lynx'))

print("Second test - .get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print("Third test - .get()")
print(switch.get('version'))

print("Fourth test - .keys()")
print(switch.keys())

print("Third test - .get()")
print(switch.values())



