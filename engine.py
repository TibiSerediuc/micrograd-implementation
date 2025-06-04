import math
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Digraph

def trace(root):
    # constructs a set of all nodes and edges in the graph
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add(child, v)
                build(child)

    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir' : 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))

        dot.node(name=uid, label = "{data $.4f }" % (n.data, ), shape='record')
        if n._op:
            dor.node(name=uid + n._op, label=n._op)
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot



class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data = {self.data})"

    def __add__(self, other):
        return Value(self.data + other.data)

    def __mul__(self, other):
        return Value(self.data * other.data)

    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        out = Value(t, (self,), 'tanh')
        
a = Value(2.0)
b = Value(3.0)
c = a + b
draw_dot(c)
