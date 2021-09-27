def postalcodes(cfrom = '79-900', cto = '80-155'):
    start = int(cfrom.replace('-',''))
    end = int(cto.replace('-',''))
    code = start
    while code <= end:
        yield code
        code += 1
        if code > 99999:
            break

for code in postalcodes():
    c = '{:5d}'.format(code).replace(' ','0')
    print(c[:2]+'-'+c[-3:])
