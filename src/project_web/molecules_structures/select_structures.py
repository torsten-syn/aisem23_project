def select_structures_by_properties(mol_data: list, 
                                    prop_ranges: dict) -> list:
    """Rewrite this function so it selects from the mol_data the molecules 
       with the properties (similarity, aLogP and PSA) laying within a range of values given by prop_ranges.
       Return list of corresponding molecule SMILES.

    Args:
        mol_data (list): list of molecules data given as dictionary. 
                         The schema of each molecule data is described in src/project_web/chembl_search/data_schema.py
        prop_ranges (dict): dictionary of properties and their ranges: {property: [min_value, max_value]}
                            available properties: similarity, alogp, psa

    Returns:
        list: list of canonical SMILES (str). 
              SMILES are stored in data.molecule_structures.canonical_smiles
    """

    return [d["molecule_structures"]["canonical_smiles"] for d in mol_data]
