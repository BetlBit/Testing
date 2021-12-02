# Не забыть pip install pytest
import pytest
from api import PetFriends
import os

pf = PetFriends()
valid_email = 'inthebetmen@mail.ru'
valid_password = 'A1S4D3A1S4D3#1'
not_valid_email = 'feffefez@mail.ru'
not_valid_password = '612'

def test_get(
	email = "inthebetmen@mail.ru", 
	password = "A1S4D3A1S4D3#1"):
	status, result = pf.get_api_key(email, password)
	assert status == 200
	assert 'key' in result

def test_get_all_pets(filter = ''):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.get_list_of_pets(auth_key, filter)
	assert status == 200
	assert len(result['pets']) > 0

def test_post_pet(
	name = 'CyberDoggy', 
	animal_type = 'CyberDog',
	age = '666', 
	pet_photo = 'images/dog.jpg'):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
	status, result = pf.post_add_pet(auth_key, name, animal_type, age, pet_photo)
	assert status == 200
	assert result['name'] == name

def test_delete_pet(pet_id=0):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
	sum_pets = len(my_pets['pets'])
	if sum_pets == 0:
		raise Exception("Ваш список питомцев пуст")
	elif pet_id > (sum_pets - 1):
		raise Exception("В Вашем списоке нет питомца с таким id")
	else:
		status, _ = pf.delete_pet(auth_key, pet_id)
		_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
	assert status == 200
	assert pet_id not in my_pets.values()

def test_put_pet(
	pet_id = 0, 
	name = 'CyberDoggy', 
	animal_type = 'CyberDog', 
	age = 666):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
	sum_pets = len(my_pets['pets'])
	if sum_pets == 0:
		raise Exception("Ваш список питомцев пуст")
	else:
		status, result = pf.put_pet(auth_key, my_pets['pets'][pet_id]['id'], name, animal_type, age)
		assert status == 200
		assert result['name'] == name

def test_post_pet(
	name = 'Koteik', 
	animal_type = 'Cat', 
	age = 5):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.post_creat_pet(auth_key, name, animal_type, age)
	assert status == 200
	assert result['name'] == name
	assert result['pet_photo'] == ""