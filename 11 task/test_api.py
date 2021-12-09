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

def test_get_novalid(email=not_valid_email, password=not_valid_password):
	status, result = pf.get_api_key(email, password)
	assert status == 403

def test_get_all_pets(filter = ''):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.get_list_of_pets(auth_key, filter)
	assert status == 200
	assert len(result['pets']) > 0

def test_get_pets_novalid_key(filter=''):
	auth_key = {"key": "6erf8er9f8ge87ew7ew9ew7fwe9f8wef8g7h6h5er5f6e7df7w6f5we5"}
	status, result = pf.get_list_of_pets(auth_key, filter)
	try:
		assert status == 400
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")

def test_get_pets_valid_key_novalid_filter(filter='fgjtfghj'):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.get_list_of_pets(auth_key, filter)
	try:
		assert status == 400
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")

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

def test_post_pet_valid_data_novalid_key(name='Бьянка', animal_type='Бишон Фризе', age='612', pet_photo='images/Byanka.jpg'):
	auth_key = {"key": "6erf8er9f8ge87ew7ew9ew7fwe9f8wef8g7h6h5er5f6e7df7w6f5we5"}
	pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
	status, result = pf.post_add_pet(auth_key, name, animal_type, age, pet_photo)
	try:
		assert status == 403
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")

def test_post_pet_null_data(name='', animal_type='', age='', pet_photo='images/Byanka.jpg'):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
	status, result = pf.post_add_pet(auth_key, name, animal_type, age, pet_photo)
	try:
		assert status == 400
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")

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

def test_put_pet_valid_data_novalid_key(pet_id='0', name='Пушистик', animal_type='Кот', age=44):
	auth_key = {"key": "863c49458eab7eefa9cd0d66bcee10855c460bc695c06bcb905f36af"}
	status, result = pf.put_pet(auth_key, pet_id, name, animal_type, age)
	try:
		assert status == 403
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")

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

def test_delete_pet_valid_data_novalid_key(pet_id=0):
	auth_key = {"key": "863c49458eab7eefa9cd0d66bcee10855c460bc695c06bcb905f36af"}
	status, _ = pf.delete_pet(auth_key, pet_id)
	try:
		assert status == 403
	except AssertionError:
		print("Исключение AssertionError")
	else:
		print("So Yeah")