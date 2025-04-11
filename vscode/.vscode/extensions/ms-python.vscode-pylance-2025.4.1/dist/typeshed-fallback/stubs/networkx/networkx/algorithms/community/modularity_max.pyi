from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def greedy_modularity_communities(
    G: Graph[_Node], weight: str | None = None, resolution: float | None = 1, cutoff: int | None = 1, best_n: int | None = None
): ...
@_dispatchable
def naive_greedy_modularity_communities(G: Graph[_Node], resolution: float = 1, weight: str | None = None): ...
