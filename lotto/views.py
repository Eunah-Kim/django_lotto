from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from .forms import PostForm

# # Create your views here.

def index(request):
    lottos=GuessNumbers.objects.all()
    # sample_str = 'This is python variable'
    # return render(request, 'lotto/default.html', {'pass_str':sample_str})
    return render(request, 'lotto/default.html', {'lottos':lottos})
    # default.html 파일 만드는 위치 : site_1\lotto\templates\lotto\default.html

    # site_1\member\templates\index.html (127.0.0.1:8000/member/)
    # site_1\products\templates\index.html (127.0.0.1:8000/member/)
    # site_1\history\templates\index.html (127.0.0.1:8000/member/)
    # django가 모든 앱들의 templates를 합치더라도
    # 각각 다른 app들의 index.html 파일들이 혼동/충돌 되지 않고 정리될 수 있음


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    print("********")
    print(request.method)
    print("********")

    if request.method == "POST":
        # print(request.POST) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 잇음
        # print(request.method) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST) #filed form
        # 양삭에 사용자가 제출한 데이터를 넣음.
        if form.is_valid():
            lotto = form.save(commit = False) #DB 저장은 아래 generate 함수의 .save()로 처리
            # github에서의 commit에 해당!
            lotto.generate()
            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정
    else:
        form = PostForm() # empty forms
        return render(request, "lotto/form.html", {"form":form})


    form = PostForm() # 상단 forms .forms import PostForm 추가
    return render(request, "lotto/form.html", {"form":form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})
