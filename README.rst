contrapy
========

Contracts for Python 3

Examples
--------

.. code:: python

    from contrapy import check, isint, isfloat, arg, ret
    
    @check
    def int_incr(n : isint) -> isint:
        return n + 1

    pos_float = arg( any(float, int), gt_0 = lambda n: n > 0) )
    ret_gt_n = ret( isfloat, gt_0 = lambda r: r > 0, gt_n = lambda r, n: r > n )

    @check
    def rand_incr(n : pos_float) -> ret_gt_n:
        return n + random.random()
