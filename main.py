

from flask import Flask
from flask import request
import os 
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="workshop",
  password="workshop",
  database="workshop"
)


@app.route('/')
def main():
    data = """
    <h3>XSS</h3>
    <form action="/xss", method="post", id = "xss", name="xss" >
          <label for="fname">Choice:</label>
          <br>
          <input type="text" id="name" name="name" value="" autofocus>
          <br><br>
          <input type="submit" value="Submit">
        </form> 
        <h3>SQL</h3>
      <form action="/sql", method="post", id = "submit", name="submit" >
          <label for="fname">Choice:</label>
          <br>
          <input type="text" id="name" name="name" value="" autofocus>
          <br><br>
          <input type="submit" value="Submit">
        </form> 
    """
    return data

@app.route('/sql', methods = ["POST"])
def sql():
    data = request.form.to_dict(flat=False)
    results = mycursor.execute('SELECT * FROM Users WHERE FirstName = "' + str(data['name'][0]) + '" limit 1', multi=True)
    return str(results)

@app.route('/xss', methods = ["POST"])
def xss():
    data = request.form.to_dict(flat=False)
    return str(data['name'][0])

@app.route('/creds', methods = ["POST"])
def creds():
    username = "JASON"
    password = "Password1@"
    return str(username + " : " + password)

import xml.etree.cElementTree as etree
tree = etree.Element("root")

@app.route('/xml', methods = ["POST"])
def xml():
    data = request.form.to_dict(flat=False)
    tree.set("hello", str(data['name'][0]))
    return str(tree.get("hello"))

@app.route('/os', methods = ["POST"])
def os():
    data = request.form.to_dict(flat=False)
    os.system(str(data['name'][0]))
    return str("Done")


if __name__ == '__main__':
    app.run()