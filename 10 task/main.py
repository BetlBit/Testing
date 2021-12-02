from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

status, result = pf.get_api(valid_email, valid_password)
print(status, result)

print(status, result = pf.post_pet(pf.get_api(valid_email, valid_password), "CyberKitty", "CyberCat", 612))
