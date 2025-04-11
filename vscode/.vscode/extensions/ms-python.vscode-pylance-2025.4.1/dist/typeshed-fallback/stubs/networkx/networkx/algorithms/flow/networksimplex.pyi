from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

class _DataEssentialsAndFunctions:
    node_list: Incomplete
    node_indices: Incomplete
    node_demands: Incomplete
    edge_sources: Incomplete
    edge_targets: Incomplete
    edge_keys: Incomplete
    edge_indices: Incomplete
    edge_capacities: Incomplete
    edge_weights: Incomplete
    edge_count: Incomplete
    edge_flow: Incomplete
    node_potentials: Incomplete
    parent: Incomplete
    parent_edge: Incomplete
    subtree_size: Incomplete
    next_node_dft: Incomplete
    prev_node_dft: Incomplete
    last_descendent_dft: Incomplete

    def __init__(self, G, multigraph, demand: str = "demand", capacity: str = "capacity", weight: str = "weight") -> None: ...
    def initialize_spanning_tree(self, n, faux_inf) -> None: ...
    def find_apex(self, p, q): ...
    def trace_path(self, p, w): ...
    def find_cycle(self, i, p, q): ...
    def augment_flow(self, Wn, We, f) -> None: ...
    def trace_subtree(self, p) -> Generator[Incomplete, None, None]: ...
    def remove_edge(self, s, t) -> None: ...
    def make_root(self, q) -> None: ...
    def add_edge(self, i, p, q) -> None: ...
    def update_potentials(self, i, p, q) -> None: ...
    def reduced_cost(self, i): ...
    def find_entering_edges(self) -> Generator[Incomplete, None, None]: ...
    def residual_capacity(self, i, p): ...
    def find_leaving_edge(self, Wn, We): ...

@_dispatchable
def network_simplex(G: Graph[_Node], demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
