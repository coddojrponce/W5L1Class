from flask import Flask,render_template,request,redirect,session
from users import User

app = Flask(__name__)
app.secret_key="supersecretpizza"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    # print(request.form['action'])
    if request.form['action'] == 'register':

        data={
            'first_name': request.form['f_name'],
            'last_name':request.form['l_name'],
            'email':request.form['email'],
            'password':request.form['password'],
        }

        id = User.save(data)
        print(f"THIS IS THE ID: {id}")
        
        session['user_id'] = id

        return redirect("/dash")
   
    return redirect("/")


@app.route("/dash")
def dash():
    users = User.get_all()
    return render_template("dash.html",users=users)

@app.route("/users/<int:id>/edit")
def edit_view(id):
    return render_template("update.html",user=User.get_one(id))

@app.route("/users/<int:id>/update",methods=["POST"])
def update_user(id):
    data={
        'first_name':request.form['f_name'],
        'last_name':request.form['l_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'id':id
    }
    User.update(data)
    return redirect("/dash")

@app.route("/users/<int:id>/destroy")
def delete(id):
    User.delete(id)
    return redirect("/dash")

if __name__ == "__main__":
    app.run(debug=True)

