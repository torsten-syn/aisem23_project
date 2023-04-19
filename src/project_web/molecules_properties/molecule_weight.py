import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts molecule weight per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Molecule weight is located in attribute `full_mwt` of `molecule_properties`
       - Make sure to exclude None values
       - When input is empty, the method should return an empty dictionary

    Args:
        raw_data (list): ChEMBL output: see callbacks/data_schema.py for description
                        
    Returns:
        dict: the following attributes have to be included in the output
                - component (str): name of the component
                - data (list): array of integers, actual values
                - mean (float): average value
                - std (float): standard deviation
                - min_value (float): minimum value
                - max_value (float): maximum value
    """
    heavy_atoms_values = [int(d["molecule_properties"]["heavy_atoms"]) for d in raw_data if d["molecule_properties"]["heavy_atoms"]]
    return dict(component="Number of heavy atoms",
                data=heavy_atoms_values,
                mean=np.mean(heavy_atoms_values),
                std=np.std(heavy_atoms_values),
                max_value=np.max(heavy_atoms_values),
                min_value=np.min(heavy_atoms_values)
                )     
    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram of molecule weights.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. BoxPlot
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of floats

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#FFC000",
                                 "line": {"width": 3,
                                          "color": "#D39F02"}}
                         ),
            ]
    layout = go.Layout(xaxis={"title": "Molecule weight"},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    