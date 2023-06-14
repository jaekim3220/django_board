from django.urls import path
from . import views_test

urlpatterns = [
    path('', views_test.test_html_multi_data),
    path('test_json', views_test.test_json_data),
    path('parameter_data', views_test.test_html_parameter_data),
    path('parameter_data2/<int:my_id>', views_test.test_html_parameter_data2),
    # path('test_post', views_test.test_post_form),
    path('test_post_handle', views_test.test_post_handle),
    path('test_select_one/<int:my_id>', views_test.test_select_one), 
    # test_select_one은 데이터 하나만 조회하므로 key 값을 설정(사용자가 원하는 데이터 조회)
    # id를 넣어서 조회
    path('test_select_all', views_test.test_select_all),

]