from django.shortcuts import render, redirect
# from django.http import JsonResponse, HttpResponse
from .models import Author, Post #Test

# # Create your views here.

# home 화면을 구성하는 html생성, requests는 templates 까지 생략
def home(request):
    return render(request, 'home.html')


# urls.py의 path('authors', views.author_list),
def author_list(request):
    authors = Author.objects.all() # Author의 모든 데이터 추출
    return render(request, 'author/author_list.html', {'authors':authors})
# 'author/author_list.html'은 author 폴더 내부의 author_list.html이므로 그대로
# 동작 안하면 캐시 삭제


def author_detail(request,my_id):
    author = Author.objects.get(id=my_id) # Author의 모든 데이터 추출
    return render(request, 'author/author_detail.html', {'author':author})


def author_update(request,my_id):
    author = Author.objects.get(id=my_id) # Author의 모든 데이터 추출
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_pw']
        # 아래는 정석으로는 if문으로 작성
        author.name = my_name 
        author.email = my_email
        author.password = my_password
        author.save() 
        # save : 신규 객체 save 시 insert, 기존 객체 save 시 update
        return redirect('/') # localhost:8000/으로 가라(home으로)
    else:
        return render(request, 'author/author_update.html', {'author':author})
    # {'author':author} : 이미 조회한 데이터를 던져 줌


def author_new(request):
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_pw']
        # DB에 insert -> save 함수 사용
        # DB의 테이블과 sync가 맞는 Test 클래스에서 객체를 생성해 save
        a1 = Author() #객체 생성은 python_basic의 class_statements.py 참고
        a1.name = my_name #t1 객체에 my_name 세팅
        a1.email = my_email
        a1.password = my_password
        a1.save()
        return redirect('/') # localhost:8000/(home)으로 가라
    else:
        return render(request, 'author/author_new.html') 
    # author/author_new.html으로 return



# urls.py의 path('authors', views.author_list),
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts':posts})
# 'post/post_list.html'은 post 폴더 내부의 post/post_list.html이므로 그대로


def post_new(request):
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        # DB에 insert -> save 함수 사용
        # DB의 테이블과 sync가 맞는 Test 클래스에서 객체를 생성해 save
        p1 = Post() #객체 생성은 python_basic의 class_statements.py 참고
        p1.title = my_title #t1 객체에 my_name 세팅
        p1.contents = my_contents
        p1.save()
        return redirect('/') # localhost:8000/(home)으로 가라
    else:
        return render(request, 'post/post_new.html') 


def post_detail(request,my_id):
    post = Post.objects.get(id=my_id) # Post의 모든 데이터 추출
    return render(request, 'post/post_detail.html', {'post':post})


def post_update(request,my_id):
    post = Post.objects.get(id=my_id) # Author의 모든 데이터 추출
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        # 아래는 정석으로는 if문으로 작성
        post.title = my_title 
        post.contents = my_contents
        post.save() 
        # save : 신규 객체 save 시 insert, 기존 객체 save 시 update
        return redirect('/') # localhost:8000/으로 가라(home으로)
    else:
        return render(request, 'post/post_update.html', {'post':post})
    # {'post':post} : 이미 조회한 데이터를 던져 줌
