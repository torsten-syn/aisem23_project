import sys
import dash
from dash.dependencies import Input, Output, State
import flask

#from flask_caching import Cache

from project_web.core_layout import core_view_html
from project_web.chembl_search.search_molecules import get_molecules
from project_web.components.results_table_layout import draw_table
from project_web.components.molecule_properties_layout import mol_props_component
from project_web.components.molecule_structures_layout import input_mol_structure, draw_selection_panel, select_mol_structures
from project_web.utils import get_property_ranges

################################################################################
# Dash app core instance
################################################################################
# Any external js scripts you need to define.
# external_scripts = [
#     #"https://www.googletagmanager.com/gtag/js?id=UA-149443072-1"
#     "https://fonts.googleapis.com/css2"
# ]

# cli = sys.modules['flask.cli']
# run_message = "To see the results go to your browser, type localhost:8053 in the address line and run a search for SMILES.\
#                If everything runs correct, you will see the histogram appearing in the results."
# cli.show_server_banner = lambda *x: cli.echo(run_message)

server = flask.Flask(__name__)
app = dash.Dash(__name__, assets_folder="assets/", server=server)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "Spring School 2023"

app.layout = core_view_html()

@app.callback(Output("chembl-results", "data"),
              Input("smiles-search-btn", "n_clicks"),
              State("smiles-input", "value"),
              State("smiles-sim-input", "value"))
def search_molecules(n_clicks, smiles, similarity):
    """Fires when SEARCH button is clicked
       Updates the Store component containing raw data from ChEMBL
    """
    if n_clicks is None:
        return {}
    
    mols_data = get_molecules(smiles, similarity)
    return {"input_smiles": smiles,
            "input_similarity": similarity,
            "mols_data": mols_data}

@app.callback([Output("mol-props-div", "children"),
               Output("results-table", "data"),
               Output("mol-input-div", "children")],
              Input("chembl-results", "data"))
def update_molecules_properties(data):
    """Fires when ChEMBL data change in Store
       Updates molecule properties section
    """
    if data:
        if not data["mols_data"]:
            return {}, {"table": [], "total": 0}, []
        input_smiles = data["input_smiles"]
        mols_data = data["mols_data"]
        graph_data, table_data = mol_props_component(mols_data)
        input_mol = input_mol_structure(input_smiles)
        value_ranges = {}
        value_ranges["similarity"] = get_property_ranges(mols_data, "similarity")
        value_ranges["alogp"] = get_property_ranges(mols_data, "alogp")
        value_ranges["psa"] = get_property_ranges(mols_data, "psa")
        selection_panel = draw_selection_panel(value_ranges)
        return graph_data, {"table": table_data, "total": len(mols_data)}, input_mol+selection_panel
    return [], {}, []


@app.callback(Output("table-div", "children"),
              Input("results-table", "data"))
def update_table(data):
    """Fires when table data get updated
       Re-draws table
    """
    if data:
        return draw_table(data)
    return ""

@app.callback(Output("mols-select-div", "children"),
              [Input("similarity-rc", "value"),
               Input("alogp-rc", "value"),
               Input("psa-rc", "value")],
              State("chembl-results", "data"))
def update_mol_structures(sim_range, alogp_range, psa_range, data):
    """Fires when table data get updated
       Re-draws table
    """
    if sim_range and alogp_range and psa_range:
        value_ranges = {}
        value_ranges["similarity"] = sim_range
        value_ranges["alogp"] = alogp_range
        value_ranges["psa"] = psa_range
        return select_mol_structures(data["mols_data"], value_ranges)
    return ""
