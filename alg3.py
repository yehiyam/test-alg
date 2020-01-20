import numpy as np
def start(args, hkubeApi=None):
    print('start called')
    waiter1 = hkubeApi.start_algorithm('eval-alg', [5, 6, 7], resultAsRaw=True)
    waiter2 = hkubeApi.start_stored_subpipeline('simple', {'d': [6, 'stam']})
    res = [waiter1.get(), waiter2.get()]
    print('got all results')
    ret = list(map(lambda x: {'error': x.get('error')} if x.get(
        'error') != None else {'response': x.get('response')}, res))
    a = np.arange(15).reshape(3, 5)
    ret.append({'algRes':a.tolist()})
    # ret='OK!!!'
    return ret


def exit(args):
    print('Exit Called!!!!!')
    
