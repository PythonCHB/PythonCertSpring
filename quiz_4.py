# Name: 

"""
Quiz  Week 4
"""

s = 'supercalafragilistic'
t = 'expialidocious'

print s[0]

print s[-1]

print s[:3]

print s[-3:]

print s[3:6]

print s.find('cal')

for c in s[:3]:
    print c 

fd = open('test.txt', 'w')
fd.write(s + '\n')
fd.write(t)
fd.close()

fd = open('test.txt', 'r')

for line in fd:
    pass

print line[:3]

         
