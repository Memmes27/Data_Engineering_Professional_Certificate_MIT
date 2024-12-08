#from flask import Flask

#app = Flask(__name__)



#@app.route("/", methods=["GET"])
#def first_route():
#    return "My first GET request"
 

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=5000)

#2.Modify the app.py file so that it includes HTML code to display the line “My first GET request” in a browser window.
#Run and debug your code. Ensure that the line “My first GET request” is displayed correctly in HTML in the browser window.
#from flask import Flask

#app = Flask(__name__)

#@app.route("/", methods=["GET"])
#def first_route():
#    html_content = """
#    <!DOCTYPE html>
#    <html>
#    <h1>
#        My First GET Request
#    </h1>
#    </html>
#    """
#    return html_content

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=5000)

##3. Open the file index.html in the template folder and include the correct HTML code,
# so that your browser window displays the text “Hello, my name is <your_full_name>”.
from flask import Flask, render_template

app = Flask(__name__)

username= 'Mohammed Abdin'

@app.route("/", methods=["GET"])
def first_route():
    return render_template('index.html', username=username)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)