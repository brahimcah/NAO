import unicodedata

stringVal = '192.168.1.1'

print(unicodedata.normalize('NFKD', l).encode('ascii', 'replace').decode())