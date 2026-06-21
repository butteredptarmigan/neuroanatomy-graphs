import ipywidgets as widgets

def refresh_output_factory(net, out, out_file):
    def refresh_output():
        out.clear_output()
        with out:
            display(net.show(out_file))
            
    return refresh_output

def add_node_box(net, callback=None):
    node_name = widgets.Text(placeholder='nazwa')
    node_abbr = widgets.Text(placeholder='skrót')
    button = widgets.Button(description='Dodaj')

    def add_node(b):
        name = node_name.value
        abbr = node_abbr.value
        identifier = abbr if abbr else name
        
        net.add_node(identifier, label=identifier, title=name)
    
        node_name.value = ''
        node_abbr.value = ''

        if callback:
            callback()
    
    button.on_click(add_node)
    
    node_box = widgets.Box(children=[
        widgets.Label('Struktura'),
        node_name,
        node_abbr,
        button
    ])
    
    return node_box

def add_edge_box(net, callback=None):
    fro = widgets.Text(placeholder='A')
    to = widgets.Text(placeholder='B')
    doi = widgets.Text(placeholder='DOI')
    sentence = widgets.Text(placeholder='Zdanie źródłowe')
    
    button = widgets.Button(description='Połącz')
    
    def add_edge(b):
        net.add_edge(
            fro.value,
            to.value,
            title=(doi.value + '\n' + sentence.value))
        
        fro.value = ''
        to.value = ''
        sentence.value = ''

        if callback:
            callback()
    
    button.on_click(add_edge)
    
    nodes = [fro, widgets.Label(value=' → '), to]
    nodes_layout = widgets.Layout(display='flex',
                                flex_flow='row',
                                align_items='stretch')
    nodes_box = widgets.Box(children=nodes, layout=nodes_layout)
    
    items = [nodes_box, doi, sentence, button]
    box_layout = widgets.Layout(display='flex',
                        flex_flow='column', 
                        align_items='stretch',
                        width='600px',
                        overflow='hidden')
    
    edge_box = widgets.Box(children=items, layout=box_layout)

    return edge_box