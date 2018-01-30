import inspect
import types

def check(*contracts):

    def contractify(obj):
        if type(obj) is type:
            return lambda val: isinstance(val, obj)
        if isinstance(obj, types.FunctionType):
            return obj
        if isinstance(obj, (bool, int, float, str, bytes)):
            return lambda val: val == obj
        return lambda val: False

    def apply_contracts(contracts, values):
        for arglist, contract in contracts:
            args = [values.get(name) for name in arglist]
            if not contract(*args):
                raise Exception(f'contract violated {contract}')

    contracts = [
        (
            tuple(map(lambda name: name if name != '_return' else 'return',
                      inspect.signature(contract).parameters.keys())
            ),
            contractify(contract)
        )
        for contract in contracts
    ]

    def _decorator(func):
        signature = inspect.signature(func)

        for argname, contract in func.__annotations__.items():
            contracts.append((
                (argname,),
                contractify(contract)
            ))

        check_before = [
            (args, contract)
            for args, contract in contracts if 'return' not in args
        ]

        check_after = [
            (args, contract)
            for args, contract in contracts if 'return' in args
        ]

        def _wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            apply_contracts(check_before, bound.arguments)
            value = func(*args, **kwargs)
            bound.arguments['return'] = value
            apply_contracts(check_after, bound.arguments)

            return value
        return _wrapper
    return _decorator
