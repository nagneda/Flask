from flask import Flask, request
import time

app=Flask(__name__)

nori=[
{'id':100,'title':'1번놀이터'},
{'id':200,'title':'2번놀이터'},
{'id':300,'title':'3번놀이터'}
]
newid=400

@app.route('/' , methods=['GET','POST'])
def start():
    
    if request.method=='POST':
        global newid
        title=request.form['title']
        nori.append({'id':newid,'title':title})
        newid+=100
    
    return homepage(getstring())

def getstring():
    string=''

    for norinum in nori:
        string+=f'<li><a href ="/nori/{norinum["id"]}/">{norinum["title"]}</a></li>'
    return string



def homepage(norilist):
    
    return f'''
    <h1>놀이터</h1>
    <ul>
        <li><a href = "/notice/">공지사항</a></li>
        <li><a href = "/warning/">주의사항</a></li>
    </ul>
    <h2>자유게시판</h2>
    <ul>
    {norilist}
    <br>
    <br>
    <br>
    <a href= "/create/" >놀이터 생성</a><br>
    <a href= "/update/" >놀이터명 수정</a>
    </ul>
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


@app.route('/create/' ,methods=['GET','POST'])
def create():

    return '''
    <h1>놀이터 생성하기</h1>
    <form action = "/" method = "POST">
    <input type="text" name="title" placeholder="게시판 이름">
    <input type="submit" value="생성하기">
    </form>
    
    '''

@app.route('/update/', methods=['POST','GET'])
def update(id=0):
    if request.method=='POST':
        for norinum in nori:
            if norinum['id']==id:
                norinum['title']=request.form['value']
        


    
    string='<h2>수정할 게시판을 선택해주세요.</h2>'
    for norinum in nori:
        string+=f'<li><a href ="/updatesite/{norinum["id"]}/">{norinum["title"]}</a></li>'
    return string+'<a href="/">처음으로</a>'
    
@app.route('/updatesite/<int:id>/')
def updatesite(id):
    for norinum in nori:
        if norinum['id']==id:
            
            updatebox=f'''
            <form action = "/update/" method="POST">
            <input type="text" name="title" value={id}>
            <input type="submit" value="수정하기">
            '''
            
            break
    return updatebox

#update별로 id값을 안주고 updatesite라는 통합 site를 따로 만들어 수정해보려고 했으나 결국에는 nori/id/ 부터 id값을 들고 있어야 update가 가능
#물론 title로 딕셔너리를 매칭시킬 수도 있지만 중복되는 제목일경우 당연히 문제 생기기 때문에 하면 안되고..    
#생활코딩에서도 그래서 read할때 id값 들고 있고 read하는 페이지에서 update create delete가 모두 표시되게 했다. 그래야 현재 read페이지에 있는 
#id값을 이용해서 creat update delete를 하러갈 수 있기 때문. 단순히 삭제할 목차만 id를 통해 뽑아놓는다면 선택했을때 내가 뭘 선택했는지는(무슨id) 
# 알 수가 없다.



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