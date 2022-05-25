from flask import Flask, render_template, request
from pwdGenerator import hash_generator
import db_handler as db

DB_PATH = "data/logs.db"

app = Flask(__name__)

# print(__name__)

@app.route("/")
def hello():
	return render_template("home.html")

@app.route("/test")
def test():
	var_1 = request.args.get("p1")
	var_2 = request.args.get("p2")
	return f"""
	<div style='border: 2px solid green; text-align: center;'>
	<h3> Test </h3>
	<p> Parameter 1 = {var_1} </p>
	<p> Parameter 2 = {var_2} </p>
	</div>
	"""

@app.route("/product", methods=["GET", "POST"])
def product_page():
	msg = ""
	if request.method == "POST":
		pwd = request.form.get("password")
		salt = request.form.get("salt")
		num_char = request.form.get("num_char")

		if pwd:
			raw_pwd = pwd + salt
			msg = hash_generator(raw_pwd, num_char)
			db.write_db(DB_PATH, (raw_pwd + num_char, msg))

	return render_template("product.html", message=msg)

@app.route("/logs")
def logs_page():
	return render_template("logs.html", data=db.read_db(DB_PATH))

# # точка входа
# if __name__ == "__main__":
# 	db.create_db(DB_PATH)
# 	app.run(debug=True)

def create_app():
	db.create_db(DB_PATH)
	return app



