
import hashlib

print('\n=== PY GERADOR DE HASHES ===')

msg = input("\nMENSAGEM: ")

sha512(msg)








def sha512(msg):
    return hashlib.sha512( str( msg ).encode("utf-8") ).hexdigest()

def sha256(msg):
    return hashlib.sha256( str( msg ).encode("utf-8") ).hexdigest()

def md5(msg):
    return hashlib.md5( str( msg ).encode("utf-8") ).hexdigest()