# coding=utf-8
from dash import html, dcc

from project_web.components.core_layout import (smiles_input, 
                                                properties_stats, 
                                                table_results, 
                                                mol_structures)
"""
Defining the core view (layout) component for the entire app.
Please do not define any callback logic in this file.
"""


header_layout = [dcc.Location(id="url", refresh=False),
                 html.Div([html.Div(className="one-half column"),
                           html.Img(src="assets/logos/Logo_SCG.png",
                                    className="two columns",
                                    style={"width": 70,
                                           "vertical-align": "bottom"}
                                    ),
                           html.Div([html.H1("SCS Spring School on Digital Chemistry"),
                                     html.H2("Collaborative Project")],
                                    className="nine columns",
                                    style={"vertical-align": "top"}),
                           html.Div(className="one-half column")
                           ],
                          className="row"),
                 html.Div(className="row", style={"margin": "10px"}),
                 ]

content_layout = html.Div([smiles_input,
                           table_results,
                           properties_stats,
                           mol_structures
                           ],
                          className="row")


footer_layout = [html.Div(["Designed by ",
                           html.A("Olga Kononova", href="https://olgakononova.com/"), html.Br(),
                           "Syngenta Crop Protection AG, Stein CH © 2023, "],
                          className="nine columns",
                          style={"font-size": "12px"})]

def core_view_html():
    return html.Div([html.Div(header_layout,
                              id="page-header",
                              className="row header"
                              ),
                     html.Div(content_layout,
                              id="page-content",
                              className="container",
                              ),
                     html.Div(footer_layout,
                              className="row footer")])

