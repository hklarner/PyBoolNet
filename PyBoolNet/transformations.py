

import re
from typing import List

import PyBoolNet


def buffer(primes: dict, buffer_type: str, buffer_prefix: str = "b_") -> dict:
    """
    Creates a Boolean network from `primes` by buffering edges or nodes.

    **arguments**:
        * *primes*: prime implicants
        * *buffer_type* (str): either `"edge"` or `"node"`
        * *buffer_prefix* (str): prefix for creation of buffer variable names

    **returns**:
        * *new_primes* (dict): the primes of the buffered network

    **example**::

        >>> primes = Repository.get_primes("raf")
        >>> ig = primes2igrgaph(primes)
        >>> primes_ = buffer(primes, "edge")
        >>> ig_ = primes2igrgaph(primes_)
        >>> 2 * len(ig.edges) == len(ig.edges)
        True
    """

    assert buffer_type in ["edge", "node"], "invalid buffer type"

    p = re.compile(r"^%s\d+$" % buffer_prefix)

    assert all(buffer_prefix not in v or p.match(v) for v in primes), "invalid buffer prefix"

    igraph = PyBoolNet.InteractionGraphs.primes2igraph(primes)

    buffered_variables = [v for v in primes if v.startswith(buffer_prefix)]
    buffer_count = 0 if not buffered_variables else max(int(v.replace(buffer_prefix, "")) for v in buffered_variables)
    buffer_count += 1

    new_primes = {k: {} for k in primes}

    if buffer_type == "node":

        buffer_nodes = [v for v in igraph.nodes if igraph.out_degree(v) > 0]
        buffer_map = {v: "%s%i" % (buffer_prefix, buffer_count+i) for i, v in enumerate(sorted(buffer_nodes))}

        for v in primes:
            for a in [0, 1]:
                new_primes[v][a] = [{buffer_map[u]: b for u, b in space.items()} for space in primes[v][a]]

        for v, buff_v in buffer_map.items():
            new_primes[buff_v] = [[{v: 0}], [{v: 1}]]

        print("created node buffer variables: %i" % len(buffer_map))

    elif buffer_type == "edge":
        buffer_map = {(u, v): "%s%i" % (buffer_prefix, buffer_count+i) for i, (u, v) in enumerate(igraph.edges())}

        for v in primes:
            for a in [0, 1]:
                new_primes[v][a] = [{buffer_map[(u, v)]: b for u, b in space.items()} for space in primes[v][a]]

        for u, v in igraph.edges():
            new_primes[buffer_map[(u, v)]] = [[{u: 0}], [{u: 1}]]

        print("created edge buffer variables: %i" % len(buffer_map))

    return new_primes


def negate(primes: dict, names: List[str] = None, copy: bool = True) -> dict:
    """
    Creates a Boolean network from `primes` by negating the update functions given in `names`.
    If `names` is `None` then all functions are negated.

    **arguments**:
        * *primes*: prime implicants
        * *names* (List[str]): either `"edge"` or `"node"`

    **returns**:
        * *new_primes* (dict): the primes of the buffered network

    **example**::

        >>> primes = Repository.get_primes("raf")
        >>> primes_ = negate(primes)
        >>> primes["raf"][0] == primes_["raf"][1]
        True
    """

    if names is None:
        names = list(primes)

    primes_ = PyBoolNet.PrimeImplicants.copy(primes) if copy else primes

    for v in names:
        primes_[v][0], primes_[v][1] = primes_[v][1], primes_[v][0]

    return primes_


def invert(primes: dict, names: List[str] = None, copy: bool = True) -> dict:
    """
    Creates a Boolean network from `primes` by negating the update functions given in `names`.
    If `names` is `None` then all functions are negated.

    **arguments**:
        * *primes*: prime implicants
        * *names* (List[str]): either `"edge"` or `"node"`

    **returns**:
        * *new_primes* (dict): the primes of the buffered network

    **example**::

        >>> primes = Repository.get_primes("raf")
        >>> primes_ = negate(primes)
        >>> primes["raf"][0] == primes_["raf"][1]
        True
    """
    pass