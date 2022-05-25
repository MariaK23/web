# Декоратор - функция, которая декорирует другую функцию

# декоратор
def dec_builder(arg):
	def dec(f_arg):
		print(f"Arg d: {arg}")
		def wrapper(a):
			print(f"Arg w: {arg}")
			print("Before")
			f_arg(a)
			print("After")
		return wrapper
	return dec

# новый синтаксис
@dec_builder("Hi!")
# целевая (декорируемая) функция
def foo(arg):
	print("Hello", arg)


# старый синтаксис
# foo = dec(foo)

foo(100)