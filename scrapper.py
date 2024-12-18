import requests
import json
import hashlib
import pandas as pd
import datetime

data_json_url = "https://bluebook.unmeetings.org/data.json"
response = requests.get(data_json_url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch the data.json file. Status code: {response.status_code}")

json_data = response.json()

pls_general_info = json_data.get("plsGeneralInfo", [])
lkp_address = pls_general_info[0].get("LKP_Address", "") if pls_general_info else ""  # Default to an empty string if no address is found
records = []
pls_staff = json_data.get("plsStaff", [])
for staff in pls_staff:
    entity_name = f"{staff.get('LKP_Title', '')} {staff.get('LKP_FirstName', '')} {staff.get('LKP_LastName', '')}".strip()
    designation = staff.get("LKP_Function", "")
    unique_key = hashlib.md5((entity_name + designation + lkp_address).encode()).hexdigest()
    records.append({
        "Entity_Name": entity_name,
        "Designation": designation,
        "Address": lkp_address,
        "Unique_Key": unique_key
    })

countries_map = {
    item.get("MC_Entity", ""): item.get("MC_Address", "") for item in json_data.get("countries", [])
}
bluebooks = json_data.get("bluebooks", [])
for book in bluebooks:
    bb_mission = book.get("BB_Mission", "")
    mc_address = countries_map.get(bb_mission, "")
    entity_name = f"{book.get('BB_Title', '')} {book.get('BB_FirstName', '')} {book.get('BB_LastName', '')}".strip()
    designation = f"{book.get('BB_Dipl_Rank_Display', '')}, {book.get('BB_Function', '')}".strip(", ")
    unique_key = hashlib.md5((entity_name + designation + mc_address).encode()).hexdigest()
    records.append({
        "Entity_Name": entity_name,
        "Designation": designation,
        "Address": mc_address,
        "Unique_Key": unique_key
    })

df = pd.DataFrame(records)
output_file = f"output_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Data successfully saved to {output_file}")
