from flask import Flask, request, render_template

app = Flask(__name__)



#@app.route("/", methods=["GET"])
#def first_route():
#    return ''' <HTML>
#    <h1> You issued a GET request</h1>
#<HTML> '''

@app.route("/", methods=["GET"])
def first_route():
    return render_template("index.html", message = "Hello Earthline")
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
