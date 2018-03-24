files = open('/home/www/python-studies/scripts/file.txt', 'w')
files.write('File write by python.')
files.close()

files = open('/home/www/python-studies/scripts/file.txt', 'a')
files.write('\nAnother string append.')
files.close()

'''With method'''

with open('/home/www/python-studies/scripts/file.txt', 'a') as files:
    files.write('\nThe with method.')
