import sys
# Detecter le type de OS....
if sys.platform == "win32":
print 'you are running WINDOWS OS.'
pathmodule = ntpath
elif sys.platform == "mac":
print 'you are running MAC OS.'
pathmodule = macpath
else:
print 'you are running a UNIX based OS.'
sys.exit()
