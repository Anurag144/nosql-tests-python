import js2py

# 1) Execute js string

code1 = 'function f(x) { return x + x; }'
f = js2py.eval_js(code1)

print(f(3))


#======================================================
code2 = '''
    function sayHi(name){ console.log("hi " + name); }
    '''
sayHi = js2py.eval_js(code2)

sayHi('Anurag')

#=======================================================

# 2) Translate *.js into *.py

js2py.translate_file('../Benchmark.js', 'resulted_py_file.py')

from resulted_py_file import *

resulted_py_file.sayHello('John')


