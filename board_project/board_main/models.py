from django.db import models

# Create your models here.
# models.py이 클래스와 db의 테이블과 sync를 맞춰 테이블(컬럼정보) 자동생성

# 클래스 이름 = 테이블 이름, 클래스 변수 = 컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)


'''author 실전 모델 생성 '''
class Author(models.Model): #Author을 모델로 사용하겠다
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    # db 설정에 default timestamp가 걸리는 것이 아닌, 장고가 현재 시간을 db에 입력
    created_at = models.DateTimeField(auto_now_add=True) # get current timestamp로 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간

'''post 실전 모델 생성 '''
class Post(models.Model): #Author을 모델로 사용하겠다
    title = models.CharField(max_length=100) #varchar(100)
    contents = models.TextField(max_length=50) # 메모리 save
    created_at = models.DateTimeField(auto_now_add=True) # get current timestamp로 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    
    # 여기부터 DB와 class의 차이
    # db에는 fk를 설정한 변수명에 _id가 붙게 된다
    # Post에서 author 객체 정보를 조회, 
    # on_delete = models.CASCADE
    # db에 author_id는 파이썬에서는 author 객체와 같은 것
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts_list') # 상단의 Author에 FK를 걸어준다


'''
from typing import Any
from django.db import models

# Create your models here.
# models.py의 클래스와 DB의 table과 sync를 맞춰 테이블(컬럼정보) 자동생성.

# 클래스명 = 테이블명, 변수=컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    # DB설정에 default timestamp가 걸리는 것이아닌, 장고가 현재시간을 db에 insert
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # DB에는 fk를 설정한 변수명에 _id 가 붙게 된다.
    # on_delete = models.CASCADE, 
    # db에 author_id는 파이썬에서는 author객체와 같은것.
    author = models.ForeignKey(Author, on_delete=models.SET_NULL ,null=True, related_name='posts')

'''