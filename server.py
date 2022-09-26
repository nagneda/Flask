from flask import Flask
import random

app=Flask(__name__)

topics = [ 
    {'id':1, 'title':'python','body':'python is...' },
    {'id':2, 'title':'c++','body':'c++ is...' },
    {'id':3, 'title':'java','body':'java is...' }
 ]

def template(contents,content):
    return f'''
    <!doctype html>
    <html>
    <head>
        <meta charset='utf-8'>
        <title>  </title>
    </head>
    <body>
        <h1><a href ="/">FLASK</a></h1>
        <ol>
            {contents}     
        </ol>
        
        {content}
        <ul>

            <li><h2><a href="/create/">create</a></h2></li>
        </ul>
    </body>
    </html>
    '''
def getcontents():
    string=''
    for topic in topics:    
        string+=f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return string

@app.route('/')
def index():
    return template(getcontents(),'<h2>welcome to my world</h2>')
    
    
@app.route('/create/')
def create():
    content='''
    <p><input type = "text" name="title" placeholder="Enter the title..."></p>
    <p><textarea name="body" placeholder="Enter the sentence..."></textarea></p>
    <input type = "submit" value="submit">
    '''
    return template(getcontents(),content)


    
@app.route('/read/<id>/')
def read(id):
    
    for topic in topics:
        if int(id)==topic['id']:
            body=topic['body']
            title=topic['title']
            break
            
    return template(getcontents(), f'<h2>{title}</h2>{body}')
    
app.run(debug=True)



