import base64
import io

from rdkit.Chem import Draw, MolFromSmiles

def draw_molecule_from_smiles(smiles):
    rdk_mol = MolFromSmiles(smiles)
    pil_img = Draw.MolToImage(rdk_mol)
    
    buff = io.BytesIO()
    pil_img.save(buff, format="png")
    return base64.b64encode(buff.getvalue()).decode("utf-8")


def draw_molecules_grid_from_smiles(smiles_list):
    rdk_mols = [MolFromSmiles(s) for s in smiles_list]
    pil_img = Draw.MolsToGridImage(rdk_mols, molsPerRow=5, subImgSize=(300,300))
    
    buff = io.BytesIO()
    pil_img.save(buff, format="png")
    return base64.b64encode(buff.getvalue()).decode("utf-8")


def get_property_ranges(mols_data, data_prop):
    data = []
    if data_prop == "similarity":
        data = [d["similarity"] for d in mols_data]
    else:
        data = [d["molecule_properties"][data_prop] for d in mols_data]
        
    if data:
        return [min(data), max(data)]
    return [-1, -1]
    
    
    