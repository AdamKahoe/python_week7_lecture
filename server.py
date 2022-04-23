from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "S3cr3t"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def form_info():
    print (request.form['artist_name'])
    # form_data = {
    #     "artist_name": request.form["artist_name"],
    #     "genre": request.form["genre"],
    #     "album": request.form["album"],
    #     "quantity": request.form["quantity"]
    # }

    session["artist_name"] = request.form["artist_name"]
    session["genre"] = request.form["genre"]
    session["album"] = request.form["album"]
    session["quantity"] = request.form["quantity"]
    # data = {
    #     "first_name": "Mike",
    #     "email": = "m@.com"
    # }
    # print(data['first_name'])
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)