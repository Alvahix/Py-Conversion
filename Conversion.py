from pint import *
from time import *

version = 1.00
m = strftime('%H%M')
m_int = int(m)
greet = 'Hello'
when = 'day'
if 0000 <= m_int <= 1159:
    greet = 'Good morning,'
    when = 'day'
elif 1200 <= m_int <= 1659:
    greet = 'Good afternoon,'
    when = 'afternoon'
elif 1700 <= m_int <= 2359:
    greet = 'Good evening,'
    when = 'evening'

print('\n' + greet + ' I\'m I.D.A., Integrated Developing Assistant. This is the unit conversion edition of me. Which unit are you converting from? Please spell out the entire unit name.')
while True:
    origin = input()
    if origin in ['done', 'Done', 'DONE']:
        break
    elif origin in ['Version', 'version', 'VERSION']:
        print('Version: ', version)
        print('\nEnter a unit to convert:')
        continue
    elif origin.endswith('s'):
        origin = origin
    else:
        origin = origin + 's'
    print('\nSounds good, how many ' + origin + '?')
    num = input()
    # TODO make program look for number and not string: while type(num) != float or type(num) != int:
    #     print('Please enter a number')
    #     print(type(num))
    #     num = input()
    num_str = str(num)
    num_float = float(num)
    # TODO add 'one' unit suppor with no 's' if num == 1:
    #    origin = origin
    print('\nOkay, you\'re converting ' + num_str + ' ' + origin + ' to what unit?')
    destination = input()

    if destination.endswith('s'):
        destination = destination
    else:
        destination = destination + 's'

    ureg = UnitRegistry()
    unit_origin = num_float * getattr(ureg, origin)
    unit_destination = unit_origin.to(getattr(ureg, destination))
    step_str = str(unit_destination)
    print('\n', unit_origin, 'is ' + step_str + 's.')
    print('\nWhats another unit you need converted? If none, simply type \'done\'.')

print('Thanks for using I.D.A. unit conversion edition. Have a nice ' + when + '!')
