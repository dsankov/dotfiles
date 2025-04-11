from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def reciprocity(G: Graph[_Node], nodes: Iterable[_Node] | None = None): ...
@_dispatchable
def overall_reciprocity(G: Graph[_Node]): ...
