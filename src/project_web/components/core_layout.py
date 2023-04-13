from dash import html, dcc

#from project_web.callbacks.molecule_structures import selection_panel_component


smiles_input = html.Div([html.Div(html.H3("Input SMILES",
                                 className="row")),
                         html.Div([dcc.Input(id="smiles-input",
                                             value="COC(=O)c1ccc(CBr)cc1",
                                             placeholder="e.g. n1ccccc1",
                                             className="five columns"),
                                   html.Div([html.Label("Similarity %",
                                                        className="two columns",
                                                        ),
                                            dcc.Input(id="smiles-sim-input",
                                                      placeholder="50",
                                                      value=50,
                                                      type="number",
                                                      min=0.1,
                                                      max=100,
                                                      className="two columns",
                                                        )],
                                            className="five columns"
                                            ),
                                   html.Button("Search",
                                               id="smiles-search-btn",
                                               className="button-primary")],
                                   className="row"),
                         dcc.Loading(html.Div(dcc.Store(id="chembl-results")),
                                     color="#cd0039",
                                     type="dot")
                         ],
                        className="row")

properties_stats = html.Div([html.H3("Molecules Properties"),
                             html.Div([html.Div(className="one column"),
                                       html.Div(id="mol-props-div",
                                                className="ten columns"),
                                       html.Div(className="one column")],
                                      className='row'),
                             ],
                            className="row")

mol_structures = html.Div([html.H3("Examples of molecules"),
                           html.Div([],
                                    id="mol-input-div",
                                    className="row"),
                           html.Div([],
                                    id="mols-select-div",
                                    className="row")],
                           className="row")

  
table_results = html.Div([html.H3("Results Summary"),
                          html.Div(id="table-div",
                                   className="ten columns"),
                          html.Div(dcc.Store(id="results-table"))
                          ],
                          className="row")