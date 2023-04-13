from dash import html, dcc

from project_web.molecules_properties import (similarity, 
                                              molecule_weight, 
                                              aromatic_rings, 
                                              hba, 
                                              hbd,
                                              alogp,
                                              ro5,
                                              psa)



def similarity_component(raw_data):
    graph = ""
    data_stats = similarity.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = similarity.draw_component(data_stats["data"])
        
    return (html.Div([html.H5("Similarity"),
                      html.Div(graph)],
                     id="similarity-div",
                     className='six columns'),
            data_stats)
    
    
def alogp_component(raw_data):
    graph = ""
    data_stats =alogp.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = alogp.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("aLogP"),
                     html.Div(graph)],
                    id="alogp-div",
                    className='six columns'),
            data_stats)

    
def molecule_weight_component(raw_data):
    graph = ""
    data_stats = molecule_weight.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = molecule_weight.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("Molecule weight"),
                     html.Div(graph)],
                    id="mol-wt-div",
                    className='six columns'),
            data_stats)
    
    
def aromatic_rings_component(raw_data):
    graph = ""
    data_stats = aromatic_rings.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = aromatic_rings.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("Number of aromatic rings"),
                     html.Div(graph)],
                    id="ar_rings_div",
                    className='six columns'),
            data_stats)
    

def hba_component(raw_data):
    graph = ""
    data_stats = hba.get_data(raw_data)
    if not data_stats:
        return ("", {})       
    graph = hba.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("Number of H-bond acceptors"),
                     html.Div(graph)],
                    id="hba-div",
                    className='six columns'),
            data_stats)
    
    
def hbd_component(raw_data):
    graph = ""
    data_stats = hbd.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = hbd.draw_component(data_stats["data"])
        
    return (html.Div([html.H5("Number of H-bond donors"),
                     html.Div(graph)],
                    id="hbd-div",
                    className='six columns'),
            data_stats)
    
    
def ro5_component(raw_data):
    graph = ""
    data_stats = ro5.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = ro5.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("'Rule of five' violations"),
                     html.Div(graph)],
                    id="ro5-div",
                    className='six columns'),
            data_stats)
    
    
def psa_component(raw_data):
    graph = ""
    data_stats = psa.get_data(raw_data)
    if not data_stats:
        return ("", {})
    graph = psa.draw_component(data_stats["data"])
    
    return (html.Div([html.H5("Polar surface area"),
                     html.Div(graph)],
                    id="psa-div",
                    className='six columns'),
            data_stats)
    

def mol_props_component(data):
    components = [similarity_component(data),
                  alogp_component(data),
                  molecule_weight_component(data),
                  aromatic_rings_component(data),
                  hba_component(data),
                  hbd_component(data),
                  ro5_component(data),
                  psa_component(data)
                  ]
    
    table_data = []
    div_data = []
    div_output = []
    c = 0
    for c, (component_div, component_data) in enumerate(components):
        div_data.append(component_div)
        if component_data:
            table_data.append(dict(property_name=component_data["component"],
                                average=round(component_data["mean"], 3),
                                std=round(component_data["std"], 3),
                                maximum=round(component_data["max_value"], 3),
                                minimum=round(component_data["min_value"], 3),
                                ))
        if c % 2 != 0:
            div_output.append(html.Div(div_data,
                                       className="row"))
            div_data = []
        
    
    return div_output, table_data
      