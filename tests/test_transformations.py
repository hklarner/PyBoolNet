

import PyBoolNet


def test_buffer():

    primes = PyBoolNet.Repository.get_primes("raf")
    primes_ = PyBoolNet.transformations.buffer(primes=primes, buffer_type="edge")

    ig = PyBoolNet.InteractionGraphs.primes2igraph(primes)
    ig_ = PyBoolNet.InteractionGraphs.primes2igraph(primes_)

    assert len(ig_.edges) == 2 * len(ig.edges)

    primes_ = PyBoolNet.transformations.buffer(primes=primes, buffer_type="node")
    ig_ = PyBoolNet.InteractionGraphs.primes2igraph(primes_)

    assert len(ig_.nodes) == 2 * len(ig.nodes)


def test_negate():

    primes = PyBoolNet.Repository.get_primes("raf")
    primes_ = PyBoolNet.transformations.negate(primes=primes)
