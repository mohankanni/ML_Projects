# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal) 
import hashlib
import base64

#Convert Input to Bytes ,followed SHA digest and Encode it with Base64

print(hashlib.sha1(bytes(passw, 'utf-8')).digest())
hash_obj = hashlib.sha1(bytes(passw, 'utf-8')).digest()
encoded = base64.b64encode(hashlib.sha1(bytes(passw, 'utf-8')).digest())
print("-----------------------------------------------")
print("{SHA}" + str(encoded.decode()))
print(type(encoded))
# {SHA}HjFbn6JevD1jMk9NRpsXrcEM+s8=
# {SHA}HjFbn6JevD1jMk9NRpsXrcEM+s8=