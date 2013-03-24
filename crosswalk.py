''' Phil Larkin's Crosswalks. 2012-12-06


    Reference Web Page:

    http://www.fhwa.dot.gov/publications/research/safety/04100/04.cfm


    Original Source Code:

    def Reclass(traffic, spd, lane, med):
        if traffic <= 9000:
            return "C"
        elif (9000 < traffic <= 12000) and (lane <= 4) and not (lane >= 4 and med == "No" and spd == "35"):
            return "C"
        elif (9000 < traffic <= 12000) and lane >= 4 and med == "no" and spd == "35"):
            return "X"
        elif (12000 < traffic <= 15000) and (lane == 2):
            return "2c"
        elif (12000 < traffic <= 15000) and (lane == 3 and (spd == "30" or spd == "25")):
            return "2ca"
        elif (12000 < traffic <= 15000) and (lane == 3 and spd == "35"):
            return "2x"
        elif (12000 < traffic <= 15000) and (lane >= 4 and (spd != "60")):
            return "2xX"
    __esri_field_calculator_splitter__

    Reclass(!TrfVol2011!, !SPEED!, !Lanes!, !Median!)
    '''

tst = ( ( ('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l') ) \
      , ( ('m', 'n', 'o'), ('p', 'q', 'r'), ('s', 't', 'u'), ('v', 'w', 'x') ) \
      , ( ('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'), ('J', 'K', 'L') ) \
      , ( ('M', 'N', 'O'), ('P', 'Q', 'R'), ('S', 'T', 'U'), ('V', 'W', 'X') ) )

t3d = ( ( ('C', 'C', 'P'), ('C', 'C', 'P'), ('C', 'C', 'N'), ('C', 'P', 'N') ) \
      , ( ('C', 'C', 'P'), ('C', 'P', 'P'), ('P', 'P', 'N'), ('P', 'N', 'N') ) \
      , ( ('C', 'C', 'P'), ('C', 'P', 'N'), ('P', 'P', 'N'), ('N', 'N', 'N') ) \
      , ( ('C', 'P', 'N'), ('P', 'P', 'N'), ('N', 'N', 'N'), ('N', 'N', 'N') ) )

def valid_index(d):
    ''' Check if d is a valid index into a tuple (i.e. is d an integer). '''
    return isinstance(d, int)

def reclass(traffic, spd, lane, med):
    ''' Given traffic, speed, lanes and median, return classification.

        traffic: number
        spd    : text like '30', '35' or '40'
        lane   : integer that is 2 or greater
        med    : text--either 'Yes' or 'No'
        x, y, z: indexes into the 3-dimensional tuple, t3d
        '''
    x = 0 if lane    ==     2                   else \
        1 if lane    ==     3                   else \
        2 if lane    >=     4  and med == "Yes" else \
        3 if lane    >=     4  and med == "No"  else 'error'
    y = 0 if traffic <=  9000                   else \
        1 if traffic <= 12000                   else \
        2 if traffic <= 15000                   else \
        3 if traffic >  15000                   else 'error'
    z = 0 if spd     <=   '30'                  else \
        1 if spd     <=   '35'                  else \
        2 if spd     <=   '40'                  else 'error'

    assert valid_index(x) and valid_index(y) and valid_index(z)

    return t3d[x][y][z]

def main():
    ''' Output:
        000a 001b 002c 010d 011e 012f 020g 021h 022i 030j 031k 032l
        100m 101n 102o 110p 111q 112r 120s 121t 122u 130v 131w 132x
        200A 201B 202C 210D 211E 212F 220G 221H 222I 230J 231K 232L
        300M 301N 302O 310P 311Q 312R 320S 321T 322U 330V 331W 332X

        07000, '30', 2, '   ': 'C'
        07000, '30', 3, '   ': 'C'
        07000, '30', 4, 'Yes': 'C'
        07000, '30', 4, 'No' : 'C'
        07000, '35', 2, '   ': 'C'
        07000, '35', 3, '   ': 'C'
        07000, '35', 4, 'Yes': 'C'
        07000, '35', 4, 'No' : 'P'
        07000, '40', 2, '   ': 'P'
        07000, '40', 3, '   ': 'P'
        07000, '40', 4, 'Yes': 'P'
        07000, '40', 4, 'No' : 'N'

        10000, '30', 2, '   ': 'C'
        10000, '30', 3, '   ': 'C'
        10000, '30', 4, 'Yes': 'C'
        10000, '30', 4, 'No' : 'P'
        10000, '35', 2, '   ': 'C'
        10000, '35', 3, '   ': 'P'
        10000, '35', 4, 'Yes': 'P'
        10000, '35', 4, 'No' : 'P'
        10000, '40', 2, '   ': 'P'
        10000, '40', 3, '   ': 'P'
        10000, '40', 4, 'Yes': 'N'
        10000, '40', 4, 'No' : 'N'

        13000, '30', 2, '   ': 'C'
        13000, '30', 3, '   ': 'P'
        13000, '30', 4, 'Yes': 'P'
        13000, '30', 4, 'No' : 'N'
        13000, '35', 2, '   ': 'C'
        13000, '35', 3, '   ': 'P'
        13000, '35', 4, 'Yes': 'P'
        13000, '35', 4, 'No' : 'N'
        13000, '40', 2, '   ': 'N'
        13000, '40', 3, '   ': 'N'
        13000, '40', 4, 'Yes': 'N'
        13000, '40', 4, 'No' : 'N'

        16000, '30', 2, '   ': 'C'
        16000, '30', 3, '   ': 'P'
        16000, '30', 4, 'Yes': 'N'
        16000, '30', 4, 'No' : 'N'
        16000, '35', 2, '   ': 'P'
        16000, '35', 3, '   ': 'N'
        16000, '35', 4, 'Yes': 'N'
        16000, '35', 4, 'No' : 'N'
        16000, '40', 2, '   ': 'N'
        16000, '40', 3, '   ': 'N'
        16000, '40', 4, 'Yes': 'N'
        16000, '40', 4, 'No' : 'N'
        '''
    for x in range(4):
        for y in range(4):
            for z in range(3):
                print '%d%d%d%s' % (x, y, z, tst[x][y][z]),
        print
    print
  # print_reclass(7000, '30', 1, '   ')  # Raises AssertionError for lane = 1
    for tra in (7000, 10000, 13000, 16000):
        for spd in ('30', '35', '40'):
            for lan, med in ( (2, '   '), (3, '   '), (4, 'Yes'), (4, 'No' ) ):
                extra_space_after_no = ' ' if med == 'No' else ''
                print "%.5d, '%s', %1d, '%s'%s: '%s'" % (tra, spd, lan, med  \
                         , extra_space_after_no, reclass(tra, spd, lan, med) )
        print

if __name__ == '__main__':
    main()