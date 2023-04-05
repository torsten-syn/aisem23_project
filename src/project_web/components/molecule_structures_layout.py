from dash import html, dcc

from project_web.utils import draw_molecule_from_smiles, draw_molecules_grid_from_smiles
from project_web.molecules_structures.select_structures import select_structures_by_properties

def draw_selection_panel(values_ranges):
    sim_min, sim_max = values_ranges["similarity"]
    alogp_min, alogp_max = values_ranges["alogp"]
    psa_min, psa_max = values_ranges["psa"]
    return [html.Div([html.Div(className="one column"),
                      html.H6("Similarity",
                              className="two columns"),
                      html.Div(dcc.RangeSlider(id="similarity-rc",
                                               min=0,
                                               max=100,
                                               value=[sim_min, sim_max],
                                               allowCross=False,
                                               tooltip={"placement": "bottom", "always_visible": True}),
                               className="eight columns",
                               style={"margin-top": "20px"}),
                      html.Div(className="one column")],
                     className="row"),
            html.Div([html.Div(className="one column"),
                      html.H6("aLogP",
                              className="two columns"),
                      html.Div(dcc.RangeSlider(id="alogp-rc",
                                               min=max(0, alogp_min-1),
                                               max=alogp_max+1,
                                               value=[alogp_min, alogp_max],
                                               allowCross=False,
                                               tooltip={"placement": "bottom", "always_visible": True}),
                               className="eight columns",
                               style={"margin-top": "20px"}),
                      html.Div(className="one column")],
                     className="row"),
            html.Div([html.Div(className="one column"),
                      html.H6("Polar surface area",
                              className="two columns"),
                      html.Div(dcc.RangeSlider(id="psa-rc",
                                               min=max(0, int(psa_min)-1),
                                               max=int(psa_max)+1,
                                               value=[psa_min, psa_max],
                                               allowCross=False,
                                               tooltip={"placement": "bottom", "always_visible": True}),
                               className="eight columns",
                               style={"margin-top": "20px"}),
                      html.Div(className="one column")],
                     className="row")
            ]

def input_mol_structure(input_smiles):
    encoded_input_img = draw_molecule_from_smiles(input_smiles)
    
    return [html.H5("Input molecule"),
            html.Img(src="data:image/png;base64, " + encoded_input_img,
                     id="input-mol-img", 
                     className="image")]
    
    
def select_mol_structures(raw_data, prop_ranges, num_mols=30):
    smiles_list = select_structures_by_properties(raw_data, prop_ranges)
    
    if not smiles_list:
        return [html.Label("No matches")]
    
    encoded_sample_img = draw_molecules_grid_from_smiles(smiles_list[:num_mols])
    return [html.Label(f"Found {len(smiles_list)} molecules"),
            html.Img(src="data:image/png;base64, " + encoded_sample_img,
                     id="sim-mols-img", 
                     className="image")]  
