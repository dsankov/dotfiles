from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def eccentricity(G: Graph[_Node], v: _Node | None = None, sp=None, weight: str | None = None): ...
@_dispatchable
def diameter(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None): ...
@_dispatchable
def periphery(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None): ...
@_dispatchable
def radius(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None): ...
@_dispatchable
def center(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None): ...
@_dispatchable
def barycenter(G, weight: str | None = None, attr=None, sp=None): ...
@_dispatchable
def resistance_distance(G: Graph[_Node], nodeA=None, nodeB=None, weight: str | None = None, invert_weight: bool = True): ...
