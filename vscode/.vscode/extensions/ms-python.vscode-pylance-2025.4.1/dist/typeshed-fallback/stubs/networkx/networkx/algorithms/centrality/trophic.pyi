from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def trophic_levels(G: DiGraph[_Node], weight="weight"): ...
@_dispatchable
def trophic_differences(G: DiGraph[_Node], weight="weight"): ...
@_dispatchable
def trophic_incoherence_parameter(G: DiGraph[_Node], weight="weight", cannibalism: bool = False): ...
