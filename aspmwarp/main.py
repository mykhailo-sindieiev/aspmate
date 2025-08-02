from defectdojo.defectdojo import DefectDojo
import os

dd_url = os.getenv("DEFECTDOJO_URL")
dd_key = os.getenv("DEFECTDOJO_API_KEY")

dd_client = DefectDojo(url=dd_url, key=dd_key)

prod_id = dd_client.create_product(name="test", description="test", prod_type=1, additional_fields={"tags": ['test'],})

code = dd_client.delete_product(product_id=prod_id)
print(prod_id)
