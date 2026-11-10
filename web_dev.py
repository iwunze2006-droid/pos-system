from flask import Flask, url_for, render_template

web = Flask(__name__) 
users = [
    {"name":"emmanuel",
     "email": "emma@gmail.com",
     "phone number":"0902233983"
     },

   {"name":"john",
     "email": "john@gmail.com",
     "phone number":"0902233983"
     },

     {"name":"aisha",
      "email": "aisha@gmail.com",
      "phone number":"0902233983"
     },
]

@web.route("/")
def home():
    return render_template("index.html")

@web.route("/about")
def about():
    home_url = url_for("profile", username='John')  
    return render_template("about.html", home=home_url)

@web.route("/contact_us")
def contact_us():
    return render_template("contact.html")

@web.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username)


@web.route("/users")
def user_list():
    return render_template("user.html", users=users)

if __name__ == "__main__":
    web.run(debug=True)
