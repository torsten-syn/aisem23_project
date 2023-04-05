import requests
import xmltodict, json

from project_web.chembl_search.data_schema import ChEMBLOutput

SERVER = "www.ebi.ac.uk"
ENDPOINT = "chembl/api/data/similarity"

def get_molecules(smiles, similarity=80, limit=100):
    query = f"https://{SERVER}/{ENDPOINT}/{smiles}/{similarity}?limit={limit}"
    response = requests.get(query)
    
    print("Request result:", response)
    
    if not response.ok:
        return []
    
    xml_data = response.text
    json_data = xmltodict.parse(xml_data)['response']['molecules']['molecule']
    
    if isinstance(json_data, dict):
        json_data = [json_data]
    
    output = []
    for data in json_data:
        try:
            output.append(ChEMBLOutput(**data).dict())
        except:
            pass
    return output
        