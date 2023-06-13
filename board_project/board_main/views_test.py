from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# Create your views here.


'''get 요청 시 html 단일 데이터 return
'''
# def test_html(request):
#     return render(request, 'test/test.html') 
# #templates 폴더 내부의 test파일을 templates 폴더의 est폴더에 삽입했기 때문


'''get 요청 시 html + 데이터 return
board_main의 urls.py에서 mapping 되도록 설정
'''
# def test_html_data(request): # 레거시한 방법
#     my_name = 'hongildong'
#     return render(request, 'test/test.html', {'name' : my_name})


'''get 요청 시 html + multi 데이터 return
'''
def test_html_multi_data(request): # 레거시한 방법
    data = {'name' : 'hongildong', 
            'age' : 20}
    return render(request, 'test/test.html', {'data' : data})


'''get 요청 시 jason data return
board_main의 urls.py에서 mapping 되도록 설정
'''
def test_json_data(request): # 데이터 할당 시 주로 json이 표준
    data = {'my_name' : 'hongildong', 
            'age' : 20} 
#     '''render는 웹 개발에서 일반적으로 화면을 return 해줄 때 사용하는 용어
#     파이썬의 dict와 유사한 json 형태로 변환해서 return
#     from django.http import JsonResponse를 사용해 형태 변환'''
    return JsonResponse(data)


'''사용자가 get 요청으로 데이터 넣어오는 방식 2가지
1. 쿼리파라미터 방식 : localhost:8000/author?id=10 
localhost:8000/parameter_data?id=1&name=hongildong를 url에 입력, 콘솔에서 정보 확인
2. pathvariable 방식(더 현대적 : rest api 방식에 근접) : localhost:8000/author/10
'''
'''사용자가 get 요청으로 쿼리파라미터 방식 데이터를 넣어올 때 post 요청
board_main의 urls.py에서 mapping 되도록 설정
'''
# localhost:8000/parameter_data?id=1&name=hongildong&password=1234
def test_html_parameter_data(request):
    # 아래에 받아올 데이터를 설정
    id = request.GET.get('id') # request의 GET 데이터 내에서 'id' 정보를 추출
    name = request.GET.get('name') # request의 GET 데이터 내에서 'name' 정보를 추출
    password = request.GET.get('password') # request의 GET 데이터 내에서 'password' 정보를 추출
    # print(id) # 화면으로 넘기기 전 확인
    # print(name) # 콘솔에 찍힘
    data = {'id' : id, 'name': name, 'password' : password}
    return render(request, 'test/test.html', {"data":data})


'''name, email, password 받아서 화면에 dict 형태로 던져주고, 
화면에는 이름을 xxx 이메일은 xxx password는 xxx url은 솔댈 필요 없음
위에도 test_html_parameter_data를 사용하므로 중복 발생 할 수 있으니 하나는 지우고
'''
# localhost:8000/parameter_data?name=hong&email=hong@naver.com&password=1234

def test_html_parameter_data(request):
    # 아래에 받아올 데이터를 설정
    name = request.GET.get('name') # request의 GET 데이터 내에서 'name' 정보를 추출
    email = request.GET.get('email') # request의 GET 데이터 내에서 'email' 정보를 추출
    password = request.GET.get('password')
    mydata = {'name' : name, 'email' : email, 'password' : password} 
    return render(request, 'test/test.html', {"my_data":mydata})


'''urls.py test_html_parameter_data2 확인
http://localhost:8000/parameter_data2/숫자 로 확인
'''
def test_html_parameter_data2(request, my_id):
    print(my_id)
    return render(request, 'test/test.html', {})


# 여기부터 test/test_post_form.html 학인
'''
form 태그를 활용한 post 방식
화면을 rendering 해주는 method 필요
test/test_post_form.html 생성 후 form 태그로 name, email, password 생성
def test_post_form(): 에서 return test/test_post_form.html
http://localhost:8000/test_post url로 매핑
'''
# def test_post_form(request):
#     return render(request, 'test/test_post_form.html')

def test_post_handle(request):
    if request.method == 'POST':
        name = request.POST['my_name']
        email = request.POST['my_email']
        password = request.POST['my_pw']
        print(name)
        print(email)
        print(password)
        return redirect('/') # localhost:8000/으로 가라(home으로)
    else:
        return render(request, 'test/test_post_form.html')
#/test_post_handle로 url 지정