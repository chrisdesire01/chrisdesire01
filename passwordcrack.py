## password_cracker written by "CTECH".
import hashlib
while True:
try:
wordlist_user=raw_input('entre le dictionaire': )
wordlist=open(wordlist_user,'r')
hash=raw_input('sha224')
break
except:
print('pas de ficheir portant ce nom !!! \n')
for word in wordlist.readlines():
word=word.strip('\n')
wordlist_hash=hashlib.sha224(word).hexdigest()
if (hash==wordlist_hash) :
print('password FOUND ===> '+word)
break
else:
print('password NOT found !')
