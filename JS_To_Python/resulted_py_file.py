__all__ = ['resulted_py_file']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['benchmarkNeighbors', 'async', 'databases', 'neighbors2data', 'posTests', 'bodies', 'ids', 'sayHello', 'desc', 'host', 'reportError', 'testRuns', 'paths', 'benchmarkAggregation', 'benchmarkSingleRead', 'tests', 'restriction', 'benchmarkNeighbors2data', 'benchmarkShortestPath', 'benchmarkNeighbors2', 'benchmarkSingleWriteSync', 'benchmarkSingleWrite', 'debug', 'database', 'reportResult', 'benchmarkHardPath', 'underscore', 'executeTest', 'neighbors', 'argv', 'total'])
@Js
def PyJsHoisted_reportError_(err, this, arguments, var=var):
    var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
    var.registers(['err'])
    var.get('console').callprop('log', Js('ERROR %s'), var.get('err'))
    var.get('process').callprop('exit', Js(1.0))
PyJsHoisted_reportError_.func_name = 'reportError'
var.put('reportError', PyJsHoisted_reportError_)
@Js
def PyJsHoisted_executeTest_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_19_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('process').callprop('nextTick', var.get('executeTest'))
    PyJs_anonymous_19_._set_name('anonymous')
    var.get('testRuns').callprop(var.put('posTests',Js(var.get('posTests').to_number())+Js(1)), PyJs_anonymous_19_, var.get('reportError'))
PyJsHoisted_executeTest_.func_name = 'executeTest'
var.put('executeTest', PyJsHoisted_executeTest_)
@Js
def PyJsHoisted_benchmarkSingleRead_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'db', 'desc', 'reject', 'name', 'resolve'])
    var.get('console').callprop('log', Js('INFO executing single read with %d documents'), var.get('ids').get('length'))
    var.put('name', Js('profiles'))
    try:
        var.put('goal', var.get('ids').get('length'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_20_(err, coll, this, arguments, var=var):
            var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
            var.registers(['k', 'start', 'err', 'coll'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            var.put('start', var.get('Date').callprop('now'))
            if var.get('desc').callprop('hasOwnProperty', Js('CONCURRENCY')):
                var.get('console').callprop('log', Js('INFO using concurrency %d'), var.get('desc').get('CONCURRENCY'))
                @Js
                def PyJs_anonymous_21_(id, cb, this, arguments, var=var):
                    var = Scope({'id':id, 'cb':cb, 'this':this, 'arguments':arguments}, var)
                    var.registers(['cb', 'id'])
                    @Js
                    def PyJs_anonymous_22_(err, doc, this, arguments, var=var):
                        var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                        var.registers(['doc', 'err'])
                        if var.get('err'):
                            return var.get('cb')(var.get('err'))
                        if var.get('debug'):
                            var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                        var.put('total',Js(var.get('total').to_number())+Js(1))
                        return var.get('cb')(var.get(u"null"))
                    PyJs_anonymous_22_._set_name('anonymous')
                    var.get('desc').callprop('getDocument', var.get('db'), var.get('coll'), var.get('id'), PyJs_anonymous_22_)
                PyJs_anonymous_21_._set_name('anonymous')
                @Js
                def PyJs_anonymous_23_(err, this, arguments, var=var):
                    var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                    var.registers(['err'])
                    if var.get('err'):
                        return var.get('reject')(var.get('err'))
                    if PyJsStrictNeq(var.get('total'),var.get('goal')):
                        var.get('reject')((((Js('expecting ')+var.get('goal'))+Js(', got '))+var.get('total')))
                    var.get('reportResult')(var.get('desc').get('name'), Js('single reads'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                    return var.get('resolve')()
                PyJs_anonymous_23_._set_name('anonymous')
                var.get('async').callprop('eachLimit', var.get('ids'), var.get('desc').get('CONCURRENCY'), PyJs_anonymous_21_, PyJs_anonymous_23_)
            else:
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<var.get('ids').get('length')):
                    try:
                        @Js
                        def PyJs_anonymous_24_(err, doc, this, arguments, var=var):
                            var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                            var.registers(['doc', 'err'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if var.get('debug'):
                                var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                            var.put('total',Js(var.get('total').to_number())+Js(1))
                            if PyJsStrictEq(var.get('total'),var.get('goal')):
                                var.get('reportResult')(var.get('desc').get('name'), Js('single reads'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                                return var.get('resolve')()
                        PyJs_anonymous_24_._set_name('anonymous')
                        var.get('desc').callprop('getDocument', var.get('db'), var.get('coll'), var.get('ids').get(var.get('k')), PyJs_anonymous_24_)
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
        PyJs_anonymous_20_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('name'), PyJs_anonymous_20_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_49493721 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_49493721 is not None:
                var.own['err'] = PyJsHolder_657272_49493721
            else:
                del var.own['err']
            del PyJsHolder_657272_49493721
PyJsHoisted_benchmarkSingleRead_.func_name = 'benchmarkSingleRead'
var.put('benchmarkSingleRead', PyJsHoisted_benchmarkSingleRead_)
@Js
def PyJsHoisted_benchmarkSingleWrite_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'db', 'desc', 'reject', 'name', 'resolve'])
    if PyJsStrictEq(var.get('desc').get('createCollection'),var.get('undefined')):
        var.get('console').callprop('log', Js('INFO %s does not implement write non-sync'), var.get('desc').get('name'))
        return var.get('resolve')()
    var.get('console').callprop('log', Js('INFO executing single write with %d documents'), var.get('bodies').get('length'))
    var.put('name', Js('profiles_temp'))
    try:
        var.put('goal', var.get('bodies').get('length'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_25_(noerr, this, arguments, var=var):
            var = Scope({'noerr':noerr, 'this':this, 'arguments':arguments}, var)
            var.registers(['noerr'])
            @Js
            def PyJs_anonymous_26_(err, coll, this, arguments, var=var):
                var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
                var.registers(['coll', 'err'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                @Js
                def PyJs_anonymous_27_(err, coll, this, arguments, var=var):
                    var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
                    var.registers(['k', 'start', 'err', 'coll'])
                    if var.get('err'):
                        return var.get('reject')(var.get('err'))
                    var.put('start', var.get('Date').callprop('now'))
                    if var.get('desc').callprop('hasOwnProperty', Js('CONCURRENCY')):
                        var.get('console').callprop('log', Js('INFO using concurrency %d'), var.get('desc').get('CONCURRENCY'))
                        @Js
                        def PyJs_anonymous_28_(body, cb, this, arguments, var=var):
                            var = Scope({'body':body, 'cb':cb, 'this':this, 'arguments':arguments}, var)
                            var.registers(['cb', 'body'])
                            @Js
                            def PyJs_anonymous_29_(err, doc, this, arguments, var=var):
                                var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                                var.registers(['doc', 'err'])
                                if var.get('err'):
                                    return var.get('cb')(var.get('err'))
                                var.put('total',Js(var.get('total').to_number())+Js(1))
                                if var.get('debug'):
                                    var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                                return var.get('cb')(var.get(u"null"))
                            PyJs_anonymous_29_._set_name('anonymous')
                            var.get('desc').callprop('saveDocument', var.get('db'), var.get('coll'), var.get('underscore').callprop('clone', var.get('body')), PyJs_anonymous_29_)
                        PyJs_anonymous_28_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_30_(err, this, arguments, var=var):
                            var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if PyJsStrictNeq(var.get('total'),var.get('goal')):
                                var.get('reject')((((Js('expecting ')+var.get('goal'))+Js(', got '))+var.get('total')))
                            var.get('reportResult')(var.get('desc').get('name'), Js('single write'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                            return var.get('resolve')()
                        PyJs_anonymous_30_._set_name('anonymous')
                        var.get('async').callprop('eachLimit', var.get('bodies'), var.get('desc').get('CONCURRENCY'), PyJs_anonymous_28_, PyJs_anonymous_30_)
                    else:
                        #for JS loop
                        var.put('k', Js(0.0))
                        while (var.get('k')<var.get('bodies').get('length')):
                            try:
                                @Js
                                def PyJs_anonymous_31_(err, doc, this, arguments, var=var):
                                    var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['doc', 'err'])
                                    if var.get('err'):
                                        return var.get('reject')(var.get('err'))
                                    if var.get('debug'):
                                        var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                                    var.put('total',Js(var.get('total').to_number())+Js(1))
                                    if PyJsStrictEq(var.get('total'),var.get('goal')):
                                        var.get('reportResult')(var.get('desc').get('name'), Js('single writes'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                                        return var.get('resolve')()
                                PyJs_anonymous_31_._set_name('anonymous')
                                var.get('desc').callprop('saveDocument', var.get('db'), var.get('coll'), var.get('underscore').callprop('clone', var.get('bodies').get(var.get('k'))), PyJs_anonymous_31_)
                            finally:
                                    var.put('k',Js(var.get('k').to_number())+Js(1))
                PyJs_anonymous_27_._set_name('anonymous')
                var.get('desc').callprop('getCollection', var.get('db'), var.get('name'), PyJs_anonymous_27_)
            PyJs_anonymous_26_._set_name('anonymous')
            var.get('desc').callprop('createCollection', var.get('db'), var.get('name'), PyJs_anonymous_26_)
        PyJs_anonymous_25_._set_name('anonymous')
        var.get('desc').callprop('dropCollection', var.get('db'), var.get('name'), PyJs_anonymous_25_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_46342854 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_46342854 is not None:
                var.own['err'] = PyJsHolder_657272_46342854
            else:
                del var.own['err']
            del PyJsHolder_657272_46342854
PyJsHoisted_benchmarkSingleWrite_.func_name = 'benchmarkSingleWrite'
var.put('benchmarkSingleWrite', PyJsHoisted_benchmarkSingleWrite_)
@Js
def PyJsHoisted_benchmarkSingleWriteSync_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'db', 'desc', 'reject', 'name', 'resolve'])
    if PyJsStrictEq(var.get('desc').get('createCollectionSync'),var.get('undefined')):
        var.get('console').callprop('log', Js('INFO %s does not implement write sync'), var.get('desc').get('name'))
        return var.get('resolve')()
    var.get('console').callprop('log', Js('INFO executing single write sync with %d documents'), var.get('bodies').get('length'))
    var.put('name', Js('profiles_temp'))
    try:
        var.put('goal', var.get('bodies').get('length'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_32_(noerr, this, arguments, var=var):
            var = Scope({'noerr':noerr, 'this':this, 'arguments':arguments}, var)
            var.registers(['noerr'])
            @Js
            def PyJs_anonymous_33_(err, coll, this, arguments, var=var):
                var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
                var.registers(['coll', 'err'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                @Js
                def PyJs_anonymous_34_(err, coll, this, arguments, var=var):
                    var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
                    var.registers(['k', 'start', 'err', 'coll'])
                    if var.get('err'):
                        return var.get('reject')(var.get('err'))
                    var.put('start', var.get('Date').callprop('now'))
                    if var.get('desc').callprop('hasOwnProperty', Js('CONCURRENCY')):
                        var.get('console').callprop('log', Js('INFO using concurrency %d'), var.get('desc').get('CONCURRENCY'))
                        @Js
                        def PyJs_anonymous_35_(body, cb, this, arguments, var=var):
                            var = Scope({'body':body, 'cb':cb, 'this':this, 'arguments':arguments}, var)
                            var.registers(['cb', 'body'])
                            @Js
                            def PyJs_anonymous_36_(err, doc, this, arguments, var=var):
                                var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                                var.registers(['doc', 'err'])
                                if var.get('err'):
                                    return var.get('cb')(var.get('err'))
                                if var.get('debug'):
                                    var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                                var.put('total',Js(var.get('total').to_number())+Js(1))
                                return var.get('cb')(var.get(u"null"))
                            PyJs_anonymous_36_._set_name('anonymous')
                            var.get('desc').callprop('saveDocumentSync', var.get('db'), var.get('coll'), var.get('underscore').callprop('clone', var.get('body')), PyJs_anonymous_36_)
                        PyJs_anonymous_35_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_37_(err, this, arguments, var=var):
                            var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if PyJsStrictNeq(var.get('total'),var.get('goal')):
                                var.get('reject')((((Js('expecting ')+var.get('goal'))+Js(', got '))+var.get('total')))
                            var.get('reportResult')(var.get('desc').get('name'), Js('single write'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                            return var.get('resolve')()
                        PyJs_anonymous_37_._set_name('anonymous')
                        var.get('async').callprop('eachLimit', var.get('bodies'), var.get('desc').get('CONCURRENCY'), PyJs_anonymous_35_, PyJs_anonymous_37_)
                    else:
                        #for JS loop
                        var.put('k', Js(0.0))
                        while (var.get('k')<var.get('bodies').get('length')):
                            try:
                                @Js
                                def PyJs_anonymous_38_(err, doc, this, arguments, var=var):
                                    var = Scope({'err':err, 'doc':doc, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['doc', 'err'])
                                    if var.get('err'):
                                        return var.get('reject')(var.get('err'))
                                    if var.get('debug'):
                                        var.get('console').callprop('log', Js('RESULT'), var.get('doc'))
                                    var.put('total',Js(var.get('total').to_number())+Js(1))
                                    if PyJsStrictEq(var.get('total'),var.get('goal')):
                                        var.get('reportResult')(var.get('desc').get('name'), Js('single writes sync'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                                        return var.get('resolve')()
                                PyJs_anonymous_38_._set_name('anonymous')
                                var.get('desc').callprop('saveDocumentSync', var.get('db'), var.get('coll'), var.get('underscore').callprop('clone', var.get('bodies').get(var.get('k'))), PyJs_anonymous_38_)
                            finally:
                                    var.put('k',Js(var.get('k').to_number())+Js(1))
                PyJs_anonymous_34_._set_name('anonymous')
                var.get('desc').callprop('getCollection', var.get('db'), var.get('name'), PyJs_anonymous_34_)
            PyJs_anonymous_33_._set_name('anonymous')
            var.get('desc').callprop('createCollectionSync', var.get('db'), var.get('name'), PyJs_anonymous_33_)
        PyJs_anonymous_32_._set_name('anonymous')
        var.get('desc').callprop('dropCollection', var.get('db'), var.get('name'), PyJs_anonymous_32_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_56339867 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_56339867 is not None:
                var.own['err'] = PyJsHolder_657272_56339867
            else:
                del var.own['err']
            del PyJsHolder_657272_56339867
PyJsHoisted_benchmarkSingleWriteSync_.func_name = 'benchmarkSingleWriteSync'
var.put('benchmarkSingleWriteSync', PyJsHoisted_benchmarkSingleWriteSync_)
@Js
def PyJsHoisted_benchmarkAggregation_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['desc', 'db', 'reject', 'name', 'resolve'])
    var.get('console').callprop('log', Js('INFO executing aggregation'))
    var.put('name', Js('profiles'))
    try:
        @Js
        def PyJs_anonymous_39_(err, coll, this, arguments, var=var):
            var = Scope({'err':err, 'coll':coll, 'this':this, 'arguments':arguments}, var)
            var.registers(['coll', 'start', 'err'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            var.put('start', var.get('Date').callprop('now'))
            @Js
            def PyJs_anonymous_40_(err, result, this, arguments, var=var):
                var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                var.registers(['err', 'result'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                if var.get('debug'):
                    var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                var.get('reportResult')(var.get('desc').get('name'), Js('aggregate'), Js(1.0), (var.get('Date').callprop('now')-var.get('start')))
                return var.get('resolve')()
            PyJs_anonymous_40_._set_name('anonymous')
            var.get('desc').callprop('aggregate', var.get('db'), var.get('coll'), PyJs_anonymous_40_)
        PyJs_anonymous_39_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('name'), PyJs_anonymous_39_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_53738108 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_53738108 is not None:
                var.own['err'] = PyJsHolder_657272_53738108
            else:
                del var.own['err']
            del PyJsHolder_657272_53738108
PyJsHoisted_benchmarkAggregation_.func_name = 'benchmarkAggregation'
var.put('benchmarkAggregation', PyJsHoisted_benchmarkAggregation_)
@Js
def PyJsHoisted_benchmarkNeighbors_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'desc', 'db', 'reject', 'resolve', 'nameP', 'nameR', 'myNeighbors'])
    var.get('console').callprop('log', Js('INFO executing neighbors for %d elements'), var.get('neighbors'))
    var.put('nameP', Js('profiles'))
    var.put('nameR', Js('relations'))
    try:
        var.put('myNeighbors', Js(0.0))
        var.put('goal', var.get('neighbors'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_41_(err, collP, this, arguments, var=var):
            var = Scope({'err':err, 'collP':collP, 'this':this, 'arguments':arguments}, var)
            var.registers(['err', 'collP'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            @Js
            def PyJs_anonymous_42_(err, collR, this, arguments, var=var):
                var = Scope({'err':err, 'collR':collR, 'this':this, 'arguments':arguments}, var)
                var.registers(['k', 'start', 'err', 'collR'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                var.put('start', var.get('Date').callprop('now'))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<var.get('neighbors')):
                    try:
                        @Js
                        def PyJs_anonymous_43_(err, result, this, arguments, var=var):
                            var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err', 'result'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if var.get('debug'):
                                var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                            var.put('myNeighbors', var.get('result'), '+')
                            var.put('total',Js(var.get('total').to_number())+Js(1))
                            if PyJsStrictEq(var.get('total'),var.get('goal')):
                                var.get('console').callprop('log', Js('INFO total number of neighbors found: %d'), var.get('myNeighbors'))
                                var.get('reportResult')(var.get('desc').get('name'), Js('neighbors'), var.get('myNeighbors'), (var.get('Date').callprop('now')-var.get('start')))
                                return var.get('resolve')()
                        PyJs_anonymous_43_._set_name('anonymous')
                        var.get('desc').callprop('neighbors', var.get('db'), var.get('collP'), var.get('collR'), var.get('ids').get(var.get('k')), var.get('k'), PyJs_anonymous_43_)
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
            PyJs_anonymous_42_._set_name('anonymous')
            var.get('desc').callprop('getCollection', var.get('db'), var.get('nameR'), PyJs_anonymous_42_)
        PyJs_anonymous_41_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('nameP'), PyJs_anonymous_41_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_9192971 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_9192971 is not None:
                var.own['err'] = PyJsHolder_657272_9192971
            else:
                del var.own['err']
            del PyJsHolder_657272_9192971
PyJsHoisted_benchmarkNeighbors_.func_name = 'benchmarkNeighbors'
var.put('benchmarkNeighbors', PyJsHoisted_benchmarkNeighbors_)
@Js
def PyJsHoisted_benchmarkNeighbors2_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'desc', 'db', 'reject', 'resolve', 'nameP', 'nameR', 'myNeighbors'])
    var.get('console').callprop('log', Js('INFO executing distinct neighbors of 1st and 2nd degree for %d elements'), var.get('neighbors'))
    var.put('nameP', Js('profiles'))
    var.put('nameR', Js('relations'))
    try:
        var.put('myNeighbors', Js(0.0))
        var.put('goal', var.get('neighbors'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_44_(err, collP, this, arguments, var=var):
            var = Scope({'err':err, 'collP':collP, 'this':this, 'arguments':arguments}, var)
            var.registers(['err', 'collP'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            @Js
            def PyJs_anonymous_45_(err, collR, this, arguments, var=var):
                var = Scope({'err':err, 'collR':collR, 'this':this, 'arguments':arguments}, var)
                var.registers(['k', 'start', 'err', 'collR'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                var.put('start', var.get('Date').callprop('now'))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<var.get('neighbors')):
                    try:
                        @Js
                        def PyJs_anonymous_46_(err, result, this, arguments, var=var):
                            var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err', 'result'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if var.get('debug'):
                                var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                            var.put('myNeighbors', var.get('result'), '+')
                            var.put('total',Js(var.get('total').to_number())+Js(1))
                            if PyJsStrictEq(var.get('total'),var.get('goal')):
                                var.get('console').callprop('log', Js('INFO total number of neighbors2 found: %d'), var.get('myNeighbors'))
                                var.get('reportResult')(var.get('desc').get('name'), Js('neighbors2'), var.get('myNeighbors'), (var.get('Date').callprop('now')-var.get('start')))
                                return var.get('resolve')()
                        PyJs_anonymous_46_._set_name('anonymous')
                        var.get('desc').callprop('neighbors2', var.get('db'), var.get('collP'), var.get('collR'), var.get('ids').get(var.get('k')), var.get('k'), PyJs_anonymous_46_)
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
            PyJs_anonymous_45_._set_name('anonymous')
            var.get('desc').callprop('getCollection', var.get('db'), var.get('nameR'), PyJs_anonymous_45_)
        PyJs_anonymous_44_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('nameP'), PyJs_anonymous_44_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_7144395 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_7144395 is not None:
                var.own['err'] = PyJsHolder_657272_7144395
            else:
                del var.own['err']
            del PyJsHolder_657272_7144395
PyJsHoisted_benchmarkNeighbors2_.func_name = 'benchmarkNeighbors2'
var.put('benchmarkNeighbors2', PyJsHoisted_benchmarkNeighbors2_)
@Js
def PyJsHoisted_benchmarkNeighbors2data_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'desc', 'db', 'reject', 'resolve', 'nameP', 'nameR', 'myNeighbors'])
    var.get('console').callprop('log', Js('INFO executing distinct neighbors of 1st and 2nd degree with profiles for %d elements'), var.get('neighbors2data'))
    var.put('nameP', Js('profiles'))
    var.put('nameR', Js('relations'))
    try:
        var.put('myNeighbors', Js(0.0))
        var.put('goal', var.get('neighbors2data'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_47_(err, collP, this, arguments, var=var):
            var = Scope({'err':err, 'collP':collP, 'this':this, 'arguments':arguments}, var)
            var.registers(['err', 'collP'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            @Js
            def PyJs_anonymous_48_(err, collR, this, arguments, var=var):
                var = Scope({'err':err, 'collR':collR, 'this':this, 'arguments':arguments}, var)
                var.registers(['k', 'start', 'err', 'collR'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                var.put('start', var.get('Date').callprop('now'))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<var.get('neighbors2data')):
                    try:
                        @Js
                        def PyJs_anonymous_49_(err, result, this, arguments, var=var):
                            var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err', 'result'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if var.get('debug'):
                                var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                            var.put('myNeighbors', var.get('result'), '+')
                            var.put('total',Js(var.get('total').to_number())+Js(1))
                            if PyJsStrictEq(var.get('total'),var.get('goal')):
                                var.get('console').callprop('log', Js('INFO total number of neighbors2 with profiles found: %d'), var.get('myNeighbors'))
                                var.get('reportResult')(var.get('desc').get('name'), Js('neighbors2data'), var.get('myNeighbors'), (var.get('Date').callprop('now')-var.get('start')))
                                return var.get('resolve')()
                        PyJs_anonymous_49_._set_name('anonymous')
                        var.get('desc').callprop('neighbors2data', var.get('db'), var.get('collP'), var.get('collR'), var.get('ids').get(var.get('k')), var.get('k'), PyJs_anonymous_49_)
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
            PyJs_anonymous_48_._set_name('anonymous')
            var.get('desc').callprop('getCollection', var.get('db'), var.get('nameR'), PyJs_anonymous_48_)
        PyJs_anonymous_47_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('nameP'), PyJs_anonymous_47_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_52484734 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_52484734 is not None:
                var.own['err'] = PyJsHolder_657272_52484734
            else:
                del var.own['err']
            del PyJsHolder_657272_52484734
PyJsHoisted_benchmarkNeighbors2data_.func_name = 'benchmarkNeighbors2data'
var.put('benchmarkNeighbors2data', PyJsHoisted_benchmarkNeighbors2data_)
@Js
def PyJsHoisted_benchmarkShortestPath_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['goal', 'desc', 'db', 'reject', 'resolve', 'nameP', 'myPaths', 'nameR'])
    if PyJsStrictEq(var.get('desc').get('shortestPath'),var.get('undefined')):
        var.get('console').callprop('log', Js('INFO %s does not implement shortest path'), var.get('desc').get('name'))
        var.get('console').callprop('log', Js('INFO -----------------------------------------------------------------------------'))
        return var.get('resolve')()
    var.get('console').callprop('log', Js('INFO executing shortest path for %d paths'), var.get('paths').get('length'))
    var.put('nameP', Js('profiles'))
    var.put('nameR', Js('relations'))
    try:
        var.put('myPaths', Js(0.0))
        var.put('goal', var.get('paths').get('length'))
        var.put('total', Js(0.0))
        @Js
        def PyJs_anonymous_50_(err, collP, this, arguments, var=var):
            var = Scope({'err':err, 'collP':collP, 'this':this, 'arguments':arguments}, var)
            var.registers(['err', 'collP'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            @Js
            def PyJs_anonymous_51_(err, collR, this, arguments, var=var):
                var = Scope({'err':err, 'collR':collR, 'this':this, 'arguments':arguments}, var)
                var.registers(['k', 'start', 'err', 'collR'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                var.put('start', var.get('Date').callprop('now'))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<var.get('paths').get('length')):
                    try:
                        @Js
                        def PyJs_anonymous_52_(err, result, this, arguments, var=var):
                            var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err', 'result'])
                            if var.get('err'):
                                return var.get('reject')(var.get('err'))
                            if var.get('debug'):
                                var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                            var.put('myPaths', var.get('result'), '+')
                            var.put('total',Js(var.get('total').to_number())+Js(1))
                            if PyJsStrictEq(var.get('total'),var.get('goal')):
                                var.get('console').callprop('log', Js('INFO total paths length: %d'), var.get('myPaths'))
                                var.get('reportResult')(var.get('desc').get('name'), Js('shortest path'), var.get('goal'), (var.get('Date').callprop('now')-var.get('start')))
                                return var.get('resolve')()
                        PyJs_anonymous_52_._set_name('anonymous')
                        var.get('desc').callprop('shortestPath', var.get('db'), var.get('collP'), var.get('collR'), var.get('paths').get(var.get('k')), var.get('k'), PyJs_anonymous_52_)
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
            PyJs_anonymous_51_._set_name('anonymous')
            var.get('desc').callprop('getCollection', var.get('db'), var.get('nameR'), PyJs_anonymous_51_)
        PyJs_anonymous_50_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('nameP'), PyJs_anonymous_50_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_98920190 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_98920190 is not None:
                var.own['err'] = PyJsHolder_657272_98920190
            else:
                del var.own['err']
            del PyJsHolder_657272_98920190
PyJsHoisted_benchmarkShortestPath_.func_name = 'benchmarkShortestPath'
var.put('benchmarkShortestPath', PyJsHoisted_benchmarkShortestPath_)
@Js
def PyJsHoisted_benchmarkHardPath_(desc, db, resolve, reject, this, arguments, var=var):
    var = Scope({'desc':desc, 'db':db, 'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
    var.registers(['desc', 'db', 'reject', 'path', 'resolve', 'nameP', 'myPaths', 'nameR'])
    if PyJsStrictEq(var.get('desc').get('shortestPath'),var.get('undefined')):
        var.get('console').callprop('log', Js('INFO %s does not implement hard path'), var.get('desc').get('name'))
        var.get('console').callprop('log', Js('INFO -----------------------------------------------------------------------------'))
        return var.get('resolve')()
    var.get('console').callprop('log', Js('INFO executing hard path'))
    var.put('nameP', Js('profiles'))
    var.put('nameR', Js('relations'))
    var.put('path', Js({'from':Js('P349622'),'to':Js('P1625331')}))
    try:
        var.put('myPaths', Js(0.0))
        @Js
        def PyJs_anonymous_53_(err, collP, this, arguments, var=var):
            var = Scope({'err':err, 'collP':collP, 'this':this, 'arguments':arguments}, var)
            var.registers(['err', 'collP'])
            if var.get('err'):
                return var.get('reject')(var.get('err'))
            @Js
            def PyJs_anonymous_54_(err, collR, this, arguments, var=var):
                var = Scope({'err':err, 'collR':collR, 'this':this, 'arguments':arguments}, var)
                var.registers(['start', 'err', 'collR'])
                if var.get('err'):
                    return var.get('reject')(var.get('err'))
                var.put('start', var.get('Date').callprop('now'))
                @Js
                def PyJs_anonymous_55_(err, result, this, arguments, var=var):
                    var = Scope({'err':err, 'result':result, 'this':this, 'arguments':arguments}, var)
                    var.registers(['err', 'result'])
                    if var.get('err'):
                        return var.get('reject')(var.get('err'))
                    if var.get('debug'):
                        var.get('console').callprop('log', Js('RESULT'), var.get('result'))
                    var.put('myPaths', var.get('result'), '+')
                    var.get('console').callprop('log', Js('INFO total paths length: %d'), var.get('myPaths'))
                    var.get('reportResult')(var.get('desc').get('name'), Js('hard path'), Js(1.0), (var.get('Date').callprop('now')-var.get('start')))
                    return var.get('resolve')()
                PyJs_anonymous_55_._set_name('anonymous')
                var.get('desc').callprop('shortestPath', var.get('db'), var.get('collP'), var.get('collR'), var.get('path'), Js(0.0), PyJs_anonymous_55_)
            PyJs_anonymous_54_._set_name('anonymous')
            var.get('desc').callprop('getCollection', var.get('db'), var.get('nameR'), PyJs_anonymous_54_)
        PyJs_anonymous_53_._set_name('anonymous')
        var.get('desc').callprop('getCollection', var.get('db'), var.get('nameP'), PyJs_anonymous_53_)
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_47561718 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', Js('ERROR %s'), var.get('err').get('stack'))
            return var.get('reject')(var.get('err'))
        finally:
            if PyJsHolder_657272_47561718 is not None:
                var.own['err'] = PyJsHolder_657272_47561718
            else:
                del var.own['err']
            del PyJsHolder_657272_47561718
PyJsHoisted_benchmarkHardPath_.func_name = 'benchmarkHardPath'
var.put('benchmarkHardPath', PyJsHoisted_benchmarkHardPath_)
@Js
def PyJsHoisted_reportResult_(db, name, num, duration, this, arguments, var=var):
    var = Scope({'db':db, 'name':name, 'num':num, 'duration':duration, 'this':this, 'arguments':arguments}, var)
    var.registers(['db', 'num', 'duration', 'name'])
    var.get('console').callprop('log', Js('INFO -----------------------------------------------------------------------------'))
    var.get('console').callprop('log', Js('INFO %s: %s, %d items'), var.get('db'), var.get('name'), var.get('num'))
    var.get('console').callprop('log', Js('INFO Total Time for %d requests: %d ms'), var.get('num'), var.get('duration'))
    var.get('console').callprop('log', Js('INFO Average: %d ms'), (var.get('duration')/var.get('num')))
    var.get('console').callprop('log', Js('INFO -----------------------------------------------------------------------------'))
PyJsHoisted_reportResult_.func_name = 'reportResult'
var.put('reportResult', PyJsHoisted_reportResult_)
@Js
def PyJsHoisted_sayHello_(name, this, arguments, var=var):
    var = Scope({'name':name, 'this':this, 'arguments':arguments}, var)
    var.registers(['name'])
    var.get('console').callprop('log', ((Js('Hello, ')+var.get('name'))+Js('!')))
PyJsHoisted_sayHello_.func_name = 'sayHello'
var.put('sayHello', PyJsHoisted_sayHello_)
Js('use strict')
var.put('underscore', var.get('require')(Js('underscore')))
var.put('async', var.get('require')(Js('async')))
def PyJs_LONG_3_(var=var):
    def PyJs_LONG_2_(var=var):
        def PyJs_LONG_1_(var=var):
            def PyJs_LONG_0_(var=var):
                return var.get('require')(Js('yargs')).callprop('usage', Js('Usage: $0 <command> [options]')).callprop('command', Js('arangodb'), Js('ArangoDB benchmark')).callprop('command', Js('arangodb-mmfiles'), Js('ArangoDB benchmark')).callprop('command', Js('mongodb'), Js('MongoDB benchmark')).callprop('command', Js('neo4j'), Js('neo4j benchmark')).callprop('command', Js('orientdb'), Js('orientdb benchmark')).callprop('command', Js('postgresql'), Js('postgresql JSON benchmark'))
            return PyJs_LONG_0_().callprop('command', Js('postgresql_tabular'), Js('postgresql tabular benchmark')).callprop('demand', Js(1.0)).callprop('option', Js('t'), Js({'alias':Js('tests'),'demand':Js(False),'default':Js('all'),'describe':Js('tests to run separated by comma: shortest, neighbors, neighbors2, neighbors2data, singleRead, singleWrite, aggregation, hardPath, singleWriteSync'),'type':Js('string')}))
        return PyJs_LONG_1_().callprop('requiresArg', Js('t')).callprop('option', Js('s'), Js({'alias':Js('restrict'),'demand':Js(False),'default':Js(0.0),'describe':Js('restrict to that many elements (0=no restriction)'),'type':Js('integer')})).callprop('requiresArg', Js('s')).callprop('option', Js('l'), Js({'alias':Js('neighbors'),'demand':Js(False),'default':Js(1000.0),'describe':Js('look at that many neighbors'),'type':Js('integer')}))
    return PyJs_LONG_2_().callprop('requiresArg', Js('l')).callprop('option', Js('ld'), Js({'alias':Js('neighbors2data'),'demand':Js(False),'default':Js(100.0),'describe':Js('look at that many neighbors2 with profiles'),'type':Js('integer')})).callprop('requiresArg', Js('ld')).callprop('option', Js('a'), Js({'alias':Js('address'),'demand':Js(False),'default':Js('127.0.0.1'),'describe':Js('server host'),'type':Js('string')}))
var.put('argv', PyJs_LONG_3_().callprop('requiresArg', Js('a')).callprop('boolean', Js('d')).callprop('help', Js('h')).callprop('epilog', Js('copyright 2015 Claudius Weinberger')).get('argv'))
var.put('databases', var.get('argv').get('_'))
var.put('tests', var.get('argv').get('t'))
var.put('debug', var.get('argv').get('d'))
var.put('restriction', var.get('argv').get('s'))
var.put('neighbors', var.get('argv').get('l'))
var.put('neighbors2data', var.get('argv').get('ld'))
var.put('host', var.get('argv').get('a'))
var.get('console').callprop('log', (Js('Debug:')+var.get('debug')))
var.put('total', Js(0.0))
if (PyJsStrictEq(var.get('tests').get('length'),Js(0.0)) or PyJsStrictEq(var.get('tests'),Js('all'))):
    var.put('tests', Js([Js('warmup'), Js('shortest'), Js('neighbors'), Js('neighbors2'), Js('singleRead'), Js('singleWrite'), Js('singleWriteSync'), Js('aggregation'), Js('hardPath'), Js('neighbors2data')]))
else:
    @Js
    def PyJs_anonymous_4_(e, this, arguments, var=var):
        var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['e'])
        return var.get('e').callprop('trim')
    PyJs_anonymous_4_._set_name('anonymous')
    var.put('tests', var.get('tests').callprop('split', Js(',')).callprop('map', PyJs_anonymous_4_))
    var.get('console').callprop('log', var.get('tests'))
var.put('database', var.get('databases').get('0'))
pass
try:
    var.put('desc', var.get('require')(((Js('./')+var.get('database'))+Js('/description'))))
except PyJsException as PyJsTempException:
    PyJsHolder_657272_90678437 = var.own.get('err')
    var.force_own_put('err', PyExceptionToJs(PyJsTempException))
    try:
        var.get('console').callprop('log', Js('ERROR database %s is unknown (%s)'), var.get('database'), var.get('err'))
        var.get('process').callprop('exit', Js(1.0))
    finally:
        if PyJsHolder_657272_90678437 is not None:
            var.own['err'] = PyJsHolder_657272_90678437
        else:
            del var.own['err']
        del PyJsHolder_657272_90678437
var.put('ids', var.get('require')(Js('./data/ids100000')))
var.put('bodies', var.get('require')(Js('./data/bodies100000')))
var.put('paths', var.get('require')(Js('./data/shortest1000')))
if (var.get('restriction')>Js(0.0)):
    var.put('ids', var.get('ids').callprop('slice', Js(0.0), var.get('restriction')))
    var.put('bodies', var.get('bodies').callprop('slice', Js(0.0), var.get('restriction')))
var.put('posTests', (-Js(1.0)))
var.put('testRuns', Js([]))
var.get('console').callprop('log', Js('INFO using server address %s'), var.get('host'))
@Js
def PyJs_anonymous_5_(db, this, arguments, var=var):
    var = Scope({'db':db, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'db', 'test'])
    @Js
    def PyJs_anonymous_6_(resolve, reject, this, arguments, var=var):
        var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
        var.registers(['resolve', 'reject'])
        var.get('console').callprop('log', Js('INFO start'))
        return var.get('resolve')()
    PyJs_anonymous_6_._set_name('anonymous')
    var.get('testRuns').callprop('push', PyJs_anonymous_6_)
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('tests').get('length')):
        try:
            var.put('test', var.get('tests').get(var.get('j')))
            if PyJsStrictEq(var.get('test'),Js('warmup')):
                @Js
                def PyJs_anonymous_7_(resolve, reject, this, arguments, var=var):
                    var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                    var.registers(['resolve', 'start', 'reject'])
                    var.put('start', var.get('Date').callprop('now'))
                    @Js
                    def PyJs_anonymous_8_(err, this, arguments, var=var):
                        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                        var.registers(['err'])
                        if var.get('err'):
                            return var.get('reject')(var.get('err'))
                        var.get('reportResult')(var.get('desc').get('name'), Js('warmup'), Js(0.0), (var.get('Date').callprop('now')-var.get('start')))
                        return var.get('resolve')()
                    PyJs_anonymous_8_._set_name('anonymous')
                    var.get('desc').callprop('warmup', var.get('db'), PyJs_anonymous_8_)
                PyJs_anonymous_7_._set_name('anonymous')
                var.get('testRuns').callprop('push', PyJs_anonymous_7_)
            else:
                if PyJsStrictEq(var.get('test'),Js('singleRead')):
                    @Js
                    def PyJs_anonymous_9_(resolve, reject, this, arguments, var=var):
                        var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                        var.registers(['resolve', 'reject'])
                        var.get('benchmarkSingleRead')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                    PyJs_anonymous_9_._set_name('anonymous')
                    var.get('testRuns').callprop('push', PyJs_anonymous_9_)
                else:
                    if PyJsStrictEq(var.get('test'),Js('singleWrite')):
                        @Js
                        def PyJs_anonymous_10_(resolve, reject, this, arguments, var=var):
                            var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                            var.registers(['resolve', 'reject'])
                            var.get('benchmarkSingleWrite')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                        PyJs_anonymous_10_._set_name('anonymous')
                        var.get('testRuns').callprop('push', PyJs_anonymous_10_)
                    else:
                        if PyJsStrictEq(var.get('test'),Js('singleWriteSync')):
                            @Js
                            def PyJs_anonymous_11_(resolve, reject, this, arguments, var=var):
                                var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                var.registers(['resolve', 'reject'])
                                var.get('benchmarkSingleWriteSync')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                            PyJs_anonymous_11_._set_name('anonymous')
                            var.get('testRuns').callprop('push', PyJs_anonymous_11_)
                        else:
                            if PyJsStrictEq(var.get('test'),Js('aggregation')):
                                @Js
                                def PyJs_anonymous_12_(resolve, reject, this, arguments, var=var):
                                    var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['resolve', 'reject'])
                                    var.get('benchmarkAggregation')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                PyJs_anonymous_12_._set_name('anonymous')
                                var.get('testRuns').callprop('push', PyJs_anonymous_12_)
                            else:
                                if PyJsStrictEq(var.get('test'),Js('neighbors')):
                                    @Js
                                    def PyJs_anonymous_13_(resolve, reject, this, arguments, var=var):
                                        var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                        var.registers(['resolve', 'reject'])
                                        var.get('benchmarkNeighbors')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                    PyJs_anonymous_13_._set_name('anonymous')
                                    var.get('testRuns').callprop('push', PyJs_anonymous_13_)
                                else:
                                    if PyJsStrictEq(var.get('test'),Js('neighbors2')):
                                        @Js
                                        def PyJs_anonymous_14_(resolve, reject, this, arguments, var=var):
                                            var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                            var.registers(['resolve', 'reject'])
                                            var.get('benchmarkNeighbors2')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                        PyJs_anonymous_14_._set_name('anonymous')
                                        var.get('testRuns').callprop('push', PyJs_anonymous_14_)
                                    else:
                                        if PyJsStrictEq(var.get('test'),Js('neighbors2data')):
                                            @Js
                                            def PyJs_anonymous_15_(resolve, reject, this, arguments, var=var):
                                                var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                                var.registers(['resolve', 'reject'])
                                                var.get('benchmarkNeighbors2data')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                            PyJs_anonymous_15_._set_name('anonymous')
                                            var.get('testRuns').callprop('push', PyJs_anonymous_15_)
                                        else:
                                            if PyJsStrictEq(var.get('test'),Js('shortest')):
                                                @Js
                                                def PyJs_anonymous_16_(resolve, reject, this, arguments, var=var):
                                                    var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                                    var.registers(['resolve', 'reject'])
                                                    var.get('benchmarkShortestPath')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                                PyJs_anonymous_16_._set_name('anonymous')
                                                var.get('testRuns').callprop('push', PyJs_anonymous_16_)
                                            else:
                                                if PyJsStrictEq(var.get('test'),Js('hardPath')):
                                                    @Js
                                                    def PyJs_anonymous_17_(resolve, reject, this, arguments, var=var):
                                                        var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                                                        var.registers(['resolve', 'reject'])
                                                        var.get('benchmarkHardPath')(var.get('desc'), var.get('db'), var.get('resolve'), var.get('reject'))
                                                    PyJs_anonymous_17_._set_name('anonymous')
                                                    var.get('testRuns').callprop('push', PyJs_anonymous_17_)
                                                else:
                                                    var.get('console').callprop('error', Js('ERROR unknown test case %s'), var.get('test'))
        finally:
                var.put('j',Js(var.get('j').to_number())+Js(1))
    @Js
    def PyJs_anonymous_18_(resolve, reject, this, arguments, var=var):
        var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
        var.registers(['resolve', 'reject'])
        var.get('console').callprop('log', Js('DONE'))
        var.get('process').callprop('exit', Js(0.0))
    PyJs_anonymous_18_._set_name('anonymous')
    var.get('testRuns').callprop('push', PyJs_anonymous_18_)
    var.get('executeTest')()
PyJs_anonymous_5_._set_name('anonymous')
var.get('desc').callprop('startup', var.get('host'), PyJs_anonymous_5_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
resulted_py_file = var.to_python()