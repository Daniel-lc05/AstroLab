import numpy as np

def attach(child, parent, p_parent_child, R_parent_child=None):
    if R_parent_child is None:
        R_parent_child = np.eye(3)

    p_parent_child = np.asarray(p_parent_child, dtype=float)
    R_parent_child = np.asarray(R_parent_child, dtype=float)

    # Detach from previous parent
    if child.parent is not None and child in child.parent.children:
        child.parent.children.remove(child)

    # Set hierarchy
    child.parent = parent
    child.p_parent_child = p_parent_child
    child.R_parent_child = R_parent_child

    # Ensure parent has children list
    if not hasattr(parent, "children"):
        parent.children = []

    # Register child once
    if child not in parent.children:
        parent.children.append(child)

    # Optional: inherit stage from core parent
    if hasattr(parent, "core") and parent.core:
        if hasattr(parent, "stage"):
            child.stage = parent.stage