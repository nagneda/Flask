from flask import Flask,request,redirect
import random

app=Flask(__name__)
nextid=4
topics = [ 
    {'id':1, 'title':'python','body':'python is...' },
    {'id':2, 'title':'c++','body':'c++ is...' },
    {'id':3, 'title':'java','body':'java is...' }
 ]

def template(contents,content,title):
    return f'''
    <!doctype html>
    <html>
    <head>
        <meta charset='utf-8'>
        <title>{title} </title>
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

# def gettitle(id):
#     for topic in topics:
#         if int(id)==topics['id']:
#             return topics['title']
def getcontents():
    string=''
    for topic in topics:    
        string+=f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return string

@app.route('/')
def index():
    return template(getcontents(),'<h2>welcome to my world</h2>','Flask')
    
    
@app.route('/create/', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        content='''
            <form action="/create/" method="POST">
                <p><input type = "text" name="title" placeholder="Enter the title..."></p>
                <p><textarea name="body" placeholder="Enter the sentence..."></textarea></p>
                <input type = "submit" value="submit">
            </form>
        '''
        return template(getcontents(),content,'Create page')
    elif request.method == 'POST':
        global nextid
        title=request.form['title']
        body=request.form['body']
        newtopic={'id':nextid,'title':title,'body':body}
        topics.append(newtopic)
        url = '/read/'+str(nextid)+'/'
        nextid+=1
        return redirect(url)#redirect 사용자의 웹브라우저에게 어디로 이동하라고 명령가능
    


    
@app.route('/read/<id>/')
def read(id):
    
    for topic in topics:
        if int(id)==topic['id']:#기본적으로 id값은 숫자긴 하지만 위의 route를 통해 문자열로 인식됐기 때문에 int로 변환하는 과정이 필요
            body=topic['body']
            title=topic['title']
            break
            
    return template(getcontents(), f'<h2>{title}</h2>{body}',title)
    
app.run(debug=True)



