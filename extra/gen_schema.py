import os
os.environ['BUMPS_USE_PYDANTIC'] = "True"

from pydantic.schema import get_model
from bumps.parameter import UnaryOperator, Operator
from refl1d.names import *
from refl1d.model import Repeat, Stack

base_model = get_model(MultiFitProblem)

# resolve circular dependencies and self-references
# TODO: this will be unnecessary in python 3.7+ with
#     'from __future__ import annotations'
# and in python 4.0+ presumably that can be removed as well.
to_resolve = [
    UnaryOperator, Operator,
    Repeat, Stack
]
for module in to_resolve:
    get_model(module).update_forward_refs()

schema = base_model.schema()
