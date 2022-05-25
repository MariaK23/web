import hashlib

def hash_generator(pwd, num_char):
	# кодирование в байт-строку
	byte_str = pwd.encode()

	# хеширование
	hash_str = hashlib.sha256(byte_str)

	# преобразование хеш-строки в обычную строку
	if num_char == "":
		hex_str = hash_str.hexdigest()
	else:
		hex_str = hash_str.hexdigest()[:int(num_char)]

	# возврат хеш-строки
	return hex_str