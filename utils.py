import pandas as pd

def dump_nodes(net):
    nodes = [net.get_node(node) for node in net.get_nodes()]
    return pd.DataFrame(nodes)

def dump_edges(net):
    edges = net.get_edges()
    return pd.DataFrame(edges)

def show_full_labels(net):
    for node in net.get_nodes():
        node = net.get_node(node)
        try:
            node['label'] = node['title']
        except KeyError:
            pass # some nodes don't have a title, so we leave their label as is

def show_abbr_labels(net):
    for node in net.get_nodes():
        node = net.get_node(node) 
        node['label'] = node['id']