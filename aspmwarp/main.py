from defectdojo.defectdojo import DefectDojo
import os

dd_url = os.getenv("DEFECTDOJO_URL")
dd_key = os.getenv("DEFECTDOJO_API_KEY")

dd_client = DefectDojo(url=dd_url, key=dd_key)

code = dd_client.create_product(name="test", description="test", prod_type=1, additional_fields={'data': 123})

print(code)
