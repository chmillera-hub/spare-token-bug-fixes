import noisy_module                                          # import at the top: runs when the child loads this file
def target(q):
    q.put(noisy_module.work(21))
