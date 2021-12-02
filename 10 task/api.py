# Здесь все методы описаны

import json
import requests
from requests_toolbelt import MultipartEncoder

class PetFriends:
		def __init__(self):
			self.base_url = "https://petfriends1.herokuapp.com/"

# Метод получения ключа GET
		def get_api(self,
			email: str,
			password: str) -> json:
				headers = {
					'email': email,
					'password': password
				}
				res = requests.get(self.base_url+'api/key', headers=headers)
				status = res.status_code
				result = ""
				try:
						result = res.json()
				except json.decoder.JSONDecodeError:
						result = res.text
				return status, result

# Метод отправки данных POST
		def post_pet(self, 
			auth_key: json,
			name: str,
			animal_type: str,
			age: str,
			# Скрыл фото питомца, потому что не знаю, как его добавить в карточку питомца (делай через https://petfriends1.herokuapp.com/apidocs/#/)
			# Там костыль есть, когда можешь вручную вписывать данные в поле ввода и затем все данные отправятся в карточку питомца на https://petfriends1.herokuapp.com/all_pets
			# pet_photo: str
			) -> json:
			data = MultipartEncoder(
				fields={'name': name,
				'animal_type': animal_type,
				'age': age,
				# 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
				})
			headers = {
				'auth_key': auth_key['key'], 
				'Content-Type': data.content_type
				}
			res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
			status = res.status_code
			result = ""
			try:
					result = res.json()
			except json.decoder.JSONDecodeError:
					result = res.text
			return status, result

# Удалить карточку питомца
		def delete_pet(self, 
			auth_key: json, 
			pet_id: int) -> json:
				headers = {
						'auth_key': auth_key['key']
					}
				res = requests.delete(self.base_url + 'api/pets/' + str(pet_id), headers=headers)
				status = res.status_code
				try:
					result = res.json()
				except json.decoder.JSONDecodeError:
					result = res.text
				return status, result

# Обновление информации в карточке питомца
		def put_pet(self,
			auth_key: json,
			pet_id: str,
			name: str,
			animal_type: str,
			age: str) -> json:
			data = MultipartEncoder(
				fields={'pet_id': pet_id,
				'name': name,
				'animal_type': animal_type,
				'age': age
				})
			headers = {
				'auth_key': auth_key['key']
			}
			res = requests.put(self.base_url + 'api/pets', headers=headers, data=data)
			status = res.status_code
			result = ""
			try:
					result = res.json()
			except json.decoder.JSONDecodeError:
					result = res.text
			return status, result