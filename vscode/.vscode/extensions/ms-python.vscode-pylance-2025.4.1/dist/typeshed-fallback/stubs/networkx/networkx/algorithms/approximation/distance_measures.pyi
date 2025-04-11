from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def diameter(G: Graph[_Node], seed: int | RandomState | None = None): ...
