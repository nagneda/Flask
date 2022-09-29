from flask import Flask, request, redirect
import time

app=Flask(__name__)

nori=[
{'id':100,'title':'1번놀이터'},
{'id':200,'title':'2번놀이터'},
{'id':300,'title':'3번놀이터'}
]

nori100=[]
nori200=[]
nori300=[]

newid_100=0

newid=400
updateid=0

@app.route('/' , methods=['GET','POST'])
def start():
    
    
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
    <a href= "/update/" >놀이터명 수정</a><br>
    
    </ul>
    ''' 
#변수를 그때그떄 만들어주는것..앞전 실습에서는 이미 생성돼있는 리스트에 딕셔너리로서 create된 페이지만 추가하는 형식이었고 내가 하고싶은 것은
#새로운 놀이터가 생성될지 안될지도 모르는 상태에서 리스트를 미리 만들수도 없을뿐더러 비효율적임. 그리고 나는 놀이터안에 또 게시글을 생성할것이기
#때문에 놀이터별로 다른 저장공간(딕셔너리를 저장할 리스트)이 필요하고 놀이터별로 id값을 저장할 놀이터별 id 변수도 필요함.
#즉 놀이터를 생성할때마다 리스트 변수가 생성됐으면 좋겠는것. 그 이후는 creat과 동일하게 딕셔너리추가만 하면 됨. 이러한 변수를 동적변수라고 표현
#>> globals() locals()사용시 가능. 사용자로부터 어떠한 문자열을 입력받고 globals()는 딕셔너리의 형태로 값을 받아들이며 문자열을 변수로 선언하며(key) 그 문자열의
#값을 이용해 다시 key에 해당하는 value(문자열이든 숫자든 변수에 들어갈 수 있는 모든 것)를 대입해주면 된다.
#놀이터 생성시 놀이터에 해당하는 리스트 변수를 생성, 놀이터별 id값 변수는 딱히 따로 두지않고 한놈으로 써도 될 것 같긴 하다.

#놀이터 내부 게시판 READ=====================================================
@app.route('/nori/<int:id>/', methods=['GET','POST'])
def norifunc(id):
    variable2='nori'+str(id)
    global updateid
    if request.method=='POST':
        title=request.form['title']
        body=request.form['body']
        global newid_100
        newid_100+=1
        var=globals()[variable2]
        var.append({'id':newid_100,'title':title,'body':body})
   
        return redirect(f'/nori/{updateid}/')

    elif request.method=='GET':
        for norinum in nori:
            if norinum['id']==id:
                title=norinum['title']
                
                updateid=id
                break
        string=''
        for newids in globals()[variable2]:
            string+=f'<li><a href="/nori/{id}/{newids["id"]}/">{newids["title"]}</a></li>'
        
        return f'''
        <h1>{title}</h1>
        {string}
        <a href="/nori/create/">게시글 작성하기</a><br>
        <form action="/delete/{id}/" method="POST">
         <input type="submit" value="놀이터 삭제하기"><br>
        <a href="/">처음으로</a>
        '''

#CREATE=============================================================================   
@app.route('/nori/create/')
def noricreate():
    global updateid
    
    return f'''
    
    <h1>게시글 작성하기</h1>
    <form action = "/nori/{updateid}/" method = "POST">
    <p><input type="text" name="title" placeholder="게시판 이름"></p>
    <p><textarea name="body" placeholder="내용"></textarea><br></p>
    <input type="submit" value="생성하기">
    </form>
    '''

@app.route('/create/' ,methods=['GET','POST'])
def create():
    if request.method=='POST':
        global newid
        title=request.form['title']
        nori.append({'id':newid,'title':title})
        global variable
        variable='nori'+str(newid)
        globals()[variable]=[]
        newid+=100
        return redirect('/')

    elif request.method=='GET':
        return '''
    <h1>놀이터 생성하기</h1>
    <form action = "/create/" method = "POST">
    <input type="text" name="title" placeholder="게시판 이름">
    <input type="submit" value="생성하기">
    </form>
    
    '''
#UPDATE====================================================
@app.route('/update/', methods=['POST','GET'])
def update():
   
                
    string='<h2>수정할 게시판을 선택해주세요.</h2>'
    for norinum in nori:
        string+=f'<li><a href ="/updatesite/{norinum["id"]}/">{norinum["title"]}</a></li>'
    return string+'<a href="/">처음으로</a>'
    
@app.route('/updatesite/<int:id>/', methods=['POST','GET'])
def updatesite(id):
    global updateid
    if request.method=='POST':
        for norinum in nori:
            if norinum['id']==updateid:
                norinum['title']=request.form['title']
                break
        return redirect('/update/')

    elif request.method=='GET':      
        for norinum in nori:
            if norinum['id']==id:
                
                updateid=id
                updatebox=f'''
                <form action = "/updatesite/{updateid}/" method="POST">
                <input type="text" name="title" value={norinum['title']}>
                <input type="submit" value="수정하기">
                '''
                
                break
        return updatebox
#DELETE====================================================================
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    
    for norinum in nori:
        if norinum['id']==id:
            nori.remove(norinum)
    return redirect('/')
    


#update별로 id값을 안주고 updatesite라는 통합 site를 따로 만들어 수정해보려고 했으나 결국에는 nori/id/ 부터 id값을 들고 있어야 update가 가능
#물론 title로 딕셔너리를 매칭시킬 수도 있지만 중복되는 제목일경우 당연히 문제 생기기 때문에 하면 안되고..    
#생활코딩에서도 그래서 read할때 id값 들고 있고 read하는 페이지에서 update create delete가 모두 표시되게 했다. 그래야 현재 read페이지에 있는 
#id값을 이용해서 creat update delete를 하러갈 수 있기 때문. 단순히 삭제할 목차만 id를 통해 뽑아놓는다면 선택했을때 내가 뭘 선택했는지는(무슨id) 
# 알 수가 없다.
#id를 update 라우트 응답함수의 파라미터로 주지 않고 updatesite에서 global변수로 잠깐 저장 시킨 후 update로 action 갔을때 global변수 사용으로 해결.
#id값을 각각 따로 가지고 있는 server.py의 read, update사이트에서는 id값을 read든 update에서든 갖고 있기 때문에 괜찮으나 내가 여기서 원하던 것은 각 페이지의
#수정, 추가할때 게시판마다 url이 따로 있는 것이 아닌 공통적인 한 페이지에서 이뤄지게 하고 싶었고 그러기 위해서는 위 방법처럼 변수하나에 id값을 저장하고
#있어야했다.


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

#redirect를 사용해야 페이지 새로고침시 중복실행이 되지 않음.