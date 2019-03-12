#!/usr/bin/env python3

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns')
protoa.append('dns')
print(proto)
proto2 = [22, 80, 443, 53]
proto.extend(proto2)
protoa.append(proto2)
print (proto)
print(protoa)

# pop last before item
proto.pop(-2)
print (proto)

#insert element in poition 1
protoa.insert(1, 345)
print (protoa)
