from _typeshed import Incomplete

from .isomorphvf2 import DiGraphMatcher, GraphMatcher

__all__ = ["TimeRespectingGraphMatcher", "TimeRespectingDiGraphMatcher"]

class TimeRespectingGraphMatcher(GraphMatcher):
    temporal_attribute_name: Incomplete
    delta: Incomplete

    def __init__(self, G1, G2, temporal_attribute_name, delta) -> None: ...
    def one_hop(self, Gx, Gx_node, neighbors): ...
    def two_hop(self, Gx, core_x, Gx_node, neighbors): ...
    def semantic_feasibility(self, G1_node, G2_node): ...

class TimeRespectingDiGraphMatcher(DiGraphMatcher):
    temporal_attribute_name: Incomplete
    delta: Incomplete

    def __init__(self, G1, G2, temporal_attribute_name, delta) -> None: ...
    def get_pred_dates(self, Gx, Gx_node, core_x, pred): ...
    def get_succ_dates(self, Gx, Gx_node, core_x, succ): ...
    def one_hop(self, Gx, Gx_node, core_x, pred, succ): ...
    def two_hop_pred(self, Gx, Gx_node, core_x, pred): ...
    def two_hop_succ(self, Gx, Gx_node, core_x, succ): ...
    def preds(self, Gx, core_x, v, Gx_node: Incomplete | None = None): ...
    def succs(self, Gx, core_x, v, Gx_node: Incomplete | None = None): ...
    def test_one(self, pred_dates, succ_dates): ...
    def test_two(self, pred_dates, succ_dates): ...
    def semantic_feasibility(self, G1_node, G2_node): ...
