import requests
import os

base_url = "https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/"
output_dir = "acl_anthology_xml"


files = [
    # ACL
    "2017.acl.xml", "2018.acl.xml", "2019.acl.xml", "2020.acl.xml", 
    "2021.acl.xml", "2022.acl.xml", "2023.acl.xml", "2024.acl.xml", "2025.acl.xml",
    # EMNLP
    "2017.emnlp.xml", "2018.emnlp.xml", "2019.emnlp.xml", "2020.emnlp.xml",
    "2021.emnlp.xml", "2022.emnlp.xml", "2023.emnlp.xml", "2024.emnlp.xml", "2025.emnlp.xml",
    # NAACL
    "2018.naacl.xml", "2019.naacl.xml", "2021.naacl.xml", 
    "2022.naacl.xml", "2024.naacl.xml", "2025.naacl.xml",
    # EACL
    "2017.eacl.xml", "2021.eacl.xml", "2023.eacl.xml", "2024.eacl.xml"
]


os.makedirs(output_dir, exist_ok=True)


for filename in files:
    url = base_url + filename
    output_path = os.path.join(output_dir, filename)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✓ Downloaded: {filename}")
    except Exception as e:
        print(f"✗ Error downloading {filename}: {e}")

print(f"\nAll files downloaded to: {output_dir}/")