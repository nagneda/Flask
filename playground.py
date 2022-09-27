from flask import Flask

app=Flask(__name__)

nori=[
{'id':100,'title':'1번 놀이터'},
{'id':101,'title':'2번 놀이터'},
{'id':102,'title':'3번 놀이터'}
]

@app.route('/')
def homepage():
    return '''
    <h1>놀이터</h1>
    <ul>
        <li><a href = "/notice/">공지사항</a></li>
        <li><a href = "/warning/">주의사항</a></li>
    </ul>
    <h2>자유게시판</h2>
    <ul>
    <li><a href = "">1번 놀이터</a></li>
    <li><a href = "">2번 놀이터</a></li>
    <li><a href = "">3번 놀이터</a></li>
    </ul>
    <br>
    <a href= "" >놀이터 생성</a>
    '''
@app.route('/nori/<int:id>/')
def norifunc(id):
    for norinum in nori:
        if norinum['id']==id:
            title=norinum['title']
            break
        
    return f'''
    <h1>{title}</h1>
    '''




@app.route('/notice/')
def notice():
    return '''
    자유롭게 놀고싶은 분들을 위해 만들었습니다. 환영합니다.
    '''
@app.route('/warning/')
def warning():
    return '''
    본 사이트는 게시글의 열람 수정의 권한이 사용자 모두에게 허용돼있으므로 주의하시길 바랍니다.
    '''
app.run(debug=True)