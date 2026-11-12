import warnings
def target(q):
    warnings.filterwarnings("ignore", category=UserWarning)   # runs in the child before the import below
    import noisy_module
    q.put(noisy_module.work(21))
