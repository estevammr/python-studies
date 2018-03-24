files = open('/home/www/python-studies/scripts/file.txt', 'w')
files.write('File write by python.')
files.close()

files = open('/home/www/python-studies/scripts/file.txt', 'a')
files.write('\nAnother string append.')
files.close()

'''With method'''

with open('/home/www/python-studies/scripts/file.txt', 'a') as files:
    files.write('\nThe with method.')

'''Exercise'''

ids = ['B3', '\nB4', '\nB5', '\nB6']

with open('/home/www/python-studies/scripts/testing.txt', 'w') as files:
    for item in ids:
        files.write(item)
