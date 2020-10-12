import re

#create regex object for phone number.
phoneRegex = re.compile(r'([+91]+)\s?(\d{10})')

#create regex object for email address.
emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+
            @
            [a-zA-Z0-9.-]+
            (\.[a-zA-Z]{2,4})
            )''',re.VERBOSE)


text = ''
with open('phone&emails.txt','r') as ptr_file:
    text+=' '.join(ptr_file.readlines())
ptr_file.close()

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ' '.join(groups)
    matches.append(phoneNum)

for groups in  emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    print('\n'.join(matches))
    pass
else:
    print('no phone and email found.')