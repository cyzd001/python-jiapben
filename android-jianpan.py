from appium import webdriver


keycode = {}
keycode['KEYCODE_UNKNOWN'] = '0'
keycode['KEYCODE_MENU'] = '1'
keycode['KEYCODE_SOFT_RIGHT'] = '2'
keycode['KEYCODE_HOME'] = '3'
keycode['KEYCODE_BACK'] = '4'
keycode['KEYCODE_CALL'] = '5'
keycode['KEYCODE_ENDCALL'] = '6'
keycode['0'] = '7'
keycode['1'] = '8'
keycode['2'] = '9'
keycode['3'] = '10'
keycode['4'] = '11'
keycode['5'] = '12'
keycode['6'] = '13'
keycode['7'] = '14'
keycode['8'] = '15'
keycode['9'] = '16'
keycode['a'] = '29'
keycode['b'] = '30'
keycode['c'] = '31'
keycode['d'] = '32'
keycode['e'] = '33'
keycode['f'] = '34'
keycode['g'] = '35'
keycode['h'] = '36'
keycode['i'] = '37'
keycode['j'] = '38'
keycode['k'] = '39'
keycode['l'] = '40'
keycode['m'] = '41'
keycode['n'] = '42'
keycode['o'] = '43'
keycode['p'] = '44'
keycode['q'] = '45'
keycode['r'] = '46'
keycode['s'] = '47'
keycode['t'] = '48'
keycode['u'] = '49'
keycode['v'] = '50'
keycode['w'] = '51'
keycode['x'] = '52'
keycode['y'] = '53'
keycode['z'] = '54'




def shuru(asdf):
    m = asdf
    for i in m:
        driver.press_keycode(i)
print(shuru('123sss'))
