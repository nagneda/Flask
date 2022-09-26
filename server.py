from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'MY NAME IS YC WHAT THE FUCK!!'

app.run(debug=True)