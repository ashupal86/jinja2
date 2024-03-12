from flask import Flask, render_template

app = Flask(__name__)

head=["Name","Age"]
data1=[
    ("ashu",180),
    ("ASHU",190),
    ("Pradeep",109),
    ("Abhay",109)
]

@app.route('/')
def index():
    return render_template('index.html',heading=head,data=data1)

    