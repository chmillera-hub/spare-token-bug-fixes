import quiet_first                                           # must be the first import of the file
import noisy_module
def target(q):
    q.put(noisy_module.work(21))
