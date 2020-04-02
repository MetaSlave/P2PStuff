import hashlib
import json
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

# Node Object
class Node:
	# Node ID, File Names as Keys and Files
	def __init__(self, ip):
		self.ip = ip
		self.dict = {}
	
	# Hash File Name
	def hash(self, fileName):
		return hashlib.sha256(bytes(fileName,'utf-8')).hexdigest()
	
	# Add File to Dictionary
	def addFile(self, fileName, file):
		secretKey = get_random_bytes(16)
		iv = get_random_bytes(16)
		cipher = AES.new(secretKey, AES.MODE_CBC, iv)
		ct_bytes = cipher.encrypt(pad(file.encode(), AES.block_size))
		ct = b64encode(ct_bytes).decode('utf-8')
		result = json.dumps({'iv':b64encode(iv).decode('utf-8'), 'ciphertext':ct})
		self.dict[self.hash(fileName)] = result

def getEncryptedFile(node):
	fileName = input("File Name?: ")
	try:
		print(n1.dict[hashlib.sha256(bytes(fileName,'utf-8')).hexdigest()])
	except:
		print("File Does not Exist")

n1 = Node("127.0.0.1")
n1.addFile("chicken", "bruh")
getEncryptedFile(n1)
