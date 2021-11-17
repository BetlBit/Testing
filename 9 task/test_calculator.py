from calculator import Calculator

cal = Calculator()

def test_multiply_positive():
	x = 3
	y = 3
	res = 9
	assert cal.multiply(x, y) == res, f"Проверка умножения не пройдена {x} * {y} не равно {res}"

def test_multiply_negative():
	cal = Calculator()
	assert cal.multiply(3, 3) != 8

def test_division_positive():
	x = 3
	y = 3
	res = 1
	assert cal.division(x, y) == res, f"Проверка деления не пройдена {x} / {y} не равно {res}"

def test_division_negative():
	cal = Calculator()
	assert cal.division(3, 3) != 0

def test_adding_positive():
	x = 3
	y = 3
	res = 6
	assert cal.adding(x, y) == res, f"Проверка сложения не пройдена {x} / {y} не равно {res}"

def test_adding_negative():
	cal = Calculator()
	assert cal.adding(3, 3) != 0

def test_subtraction_positive():
	x = 3
	y = 3
	res = 0
	assert cal.subtraction(x, y) == res, f"Проверка вычитания не пройдена {x} / {y} не равно {res}"

def test_subtraction_negative():
	cal = Calculator()
	assert cal.subtraction(3, 3) != 1