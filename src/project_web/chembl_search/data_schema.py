from pydantic import BaseModel
from typing import Optional, List, Dict


class ChEMBLMolProperties(BaseModel):
    alogp: float
    aromatic_rings: int
    cx_logd: str
    cx_logp: str
    cx_most_apka: str = None
    cx_most_bpka: str = None
    full_molformula: str
    full_mwt: float
    hba: int = None 
    hba_lipinski: int = None
    hbd: int = None
    hbd_lipinski: int = None
    heavy_atoms: str
    molecular_species: str
    mw_freebase: str
    mw_monoisotopic: str
    np_likeness_score: str
    num_lipinski_ro5_violations: str = None
    num_ro5_violations: int = None
    psa: float
    qed_weighted: str
    ro3_pass: str
    rtb: str
    

class ChEMBLMolStructures(BaseModel):
    standard_inchi: str
    canonical_smiles: str
    molfile: str
    standard_inchi_key: str
    
    
class ChEMBLMolHierarchy(BaseModel):
    molecule_chembl_id: str
    active_chembl_id: str
    parent_chembl_id: str
    
    
class ChEMBLOutput(BaseModel):
    chirality: str
    molecule_chembl_id: str
    molecule_type: str
    similarity: float
    structure_type: str
    
    molecule_properties: ChEMBLMolProperties
    molecule_structures: ChEMBLMolStructures
    
    atc_classifications: Optional[str] = None
    availability_type: Optional[str] = None
    biotherapeutic: Optional[str] = None
    black_box_warning:  Optional[str] = None
    chebi_par_id:  Optional[str] = None
    cross_references:  Optional[Dict] = None
    dosed_ingredient: Optional[str] = None
    first_approval: Optional[str] = None
    first_in_class:  Optional[str] = None
    helm_notation:  Optional[str] = None
    indication_class:  Optional[str] = None
    inorganic_flag:  Optional[str] = None
    max_phase:  Optional[str] = None
    natural_product:  Optional[str] = None
    oral:  Optional[str] = None
    parenteral:  Optional[str] = None
    polymer_flag:  Optional[str] = None
    pref_name:  Optional[str] = None
    prodrug:  Optional[str] = None
    therapeutic_flag: Optional[str] = None
    topical:  Optional[str] = None
    usan_stem:  Optional[str] = None
    usan_stem_definition:  Optional[str] = None
    usan_substem:  Optional[str] = None
    usan_year:  Optional[str] = None
    withdrawn_flag:  Optional[str] = None
    

class JSONResponse(BaseModel):
    json_data: List[ChEMBLOutput]
