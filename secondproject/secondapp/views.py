from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import Question
from secondapp.models import UserData,Result,AdminData
# Create your views here.

def index(request):
    return HttpResponse('welcome user')

def display(request):
    return render(request,'questionmanagement.html')

def AddQuetion(request):
    Question.objects.create(
        qno=request.GET['qno'],
        qtext=request.GET['qtext'],
        answer=request.GET['answer'],
        op1=request.GET['op1'],
        op2=request.GET['op2'],
        op3=request.GET['op3'],
        op4=request.GET['op4'],
        subject=request.GET['subject']
    )

    return render(request,'questionmanagement.html',{'message':"Question added Succesfully!"})


def ViewQuestion(request):

    question=Question.objects.get(qno=request.GET['qno'],subject=request.GET['subject'])

    return render(request,'questionmanagement.html',{'question':question})

def UpdateQuestion(request):
    question = Question.objects.filter(qno=request.GET['qno'], subject=request.GET['subject'])
    
    question.update(
        qtext=request.GET['qtext'],
        answer=request.GET['answer'],
        op1=request.GET['op1'],
        op2=request.GET['op2'],
        op3=request.GET['op3'],
        op4=request.GET['op4']
    )
    return render(request, 'questionmanagement.html', {'message': "Question Updated Successfully!"})

def DeleteQuestion(request):
    Question.objects.filter(qno=request.GET['qno'], subject=request.GET['subject'])


    Question.objects.filter(qno=request.GET['qno'], subject=request.GET['subject']).delete()
    return render(request, 'questionmanagement.html', {'message': "Question Deleted Successfully!"})

def giveERegister(request):
    return render(request, 'register.html')

def Register(request):
    usernamefrombrowser=request.GET.get("username")
    useremailfrombrowser=request.GET.get("email") 
    passfrombrowser=request.GET.get("password")

    UserData.objects.create(username=usernamefrombrowser,email=useremailfrombrowser,password=passfrombrowser)

    return render(request, 'login.html',{'message': 'registration successfull! Please Login'})

def Login(request):
    usernamefrombrowser=request.GET['username']
    passfrombrowser=request.GET['password']

    request.session['username']=usernamefrombrowser

    try:
        usernamefromdb=UserData.objects.get(username=usernamefrombrowser)
    except:
        return render(request, 'login.html',{'message': 'invalid username'})


    if usernamefromdb.password == passfrombrowser:
        
        request.session['answer']={}
        request.session['score']=0
        request.session['qno']=-1

        # queryset=Question.objects.filter(subject='math').values()
        # listofquestions=list(queryset)
        # request.session["listofquestions"]=listofquestions
    
        return render(request,"subjects.html", {"message":"welcome" + "\t" +  usernamefrombrowser})

    else:
        return render(request,"login.html",{"message":"Invalid Credential"})


def giveELogin(request):

    return render(request, 'login.html')


def StartTest(request):
    subjectname=request.GET['subject']
    request.session['subject']=subjectname

    queryset=Question.objects.filter(subject=subjectname).values()
    listofquestions=list(queryset)
    request.session['listofquestions']=listofquestions

    return render(request,'questionnavigation.html',{'question':listofquestions[0]})


def QuestionNavigation(request):
    return render(request,'questionnavigation.html')


def nextQuestion(request):
    if 'op' in request.GET:

        allanswers=request.session['answer']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        print(allanswers)

    allquestions=request.session['listofquestions']
    questionindex=request.session['qno']

    if questionindex<len(allquestions)-1:
        request.session['qno']=request.session['qno']+1

        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session['qno']]

    else:
        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})

def previousQuestion(request):
    allquestions=request.session['listofquestions']
    questionindex=request.session['qno']

    if questionindex<len(allquestions):
        request.session['qno']=request.session['qno']-1

        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session['qno']]

    else:
        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})


def endExam(request):
    if 'op' in request.GET:

        allanswers=request.session['answer']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        print(allanswers)

    responses=request.session['answer']
    allanswers2=responses.values()

    for ans in allanswers2:

        print(f'correct answer {ans[2]} and submitted answer is {ans[3]}')

        if ans[2]==ans[3]:
            request.session['score']=request.session['score']+1
        
    finalscore=request.session['score']
    print(f'Your score is {finalscore}')
    
    usernamefrombrowser = request.session.get('username') 
    subjectname = request.session.get('subject')   

    
    if usernamefrombrowser and subjectname:
        Result.objects.create(username=usernamefrombrowser, subject=subjectname, score=finalscore)
    else:
        print("Error: Username or subject is missing.")


    return render(request,'score.html',{'score':finalscore,'responses':allanswers2})

def AdminLogin(request):
    return render(request,'adminLogin.html')

def AdminToLogin(request):
    adminnamefrombrowser=request.GET['adminname']
    apassfrombrowser=request.GET['apassword']

    request.session['adminname']=adminnamefrombrowser

    try:
        adminnamefromdb=AdminData.objects.get(username=adminnamefrombrowser)
    except:
        return render(request, 'login.html',{'message': 'invalid username'})


    if adminnamefromdb.password == apassfrombrowser:

        return render(request,"adminDash.html", {"message":"welcome" + "\t" +  adminnamefrombrowser})

    else:
        return render(request,"adminlogin.html",{"message":"Invalid Credential"})



def AdminDash(request):
    return render(request,'adminDash.html')

def ExamScore(request):
    Results=Result.objects.all()
    return render(request,'examscore.html',{'Results':Results})