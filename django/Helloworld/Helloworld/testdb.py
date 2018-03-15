# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

#數據庫操作 添加數據
#def testdb(request):
    #test1 = Test(name='runoob')
    #test1.save()
    #return HttpResponse("<p>數據庫添加成功</p>")

#數據庫操作 獲取數據
def testdb(request):
    #初始化
    response = ""
    response1 = ""

    #通過objects這個管理器的all()獲得所有數據行，相當於SQL中的SELECT * FROM
    list = Test.objects.all()

    #filter相當於SQL中的WHERE,可設置條件過濾結果
    response2 = Test.objects.filter(id=1)

    #獲取單個對象
    response3 = Test.objects.get(id=1)

    #限制返回的數據，相當於SQL中的OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    #數據排序
    Test.objects.order_by("id")

    #上面的方法可以連鎖使用
    Test.objects.filter(name="runoob").order_by("id")

    #輸出所有數據
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

#數據庫操作 更新數據
#def testdb(request):
    #修改其中一個id=1的name字段，再save，相當於SQL中的UPDATE
    #test1 = Test.objects.get(id=1)
    #test1.name = 'Google'
    #test1.save()

    #另外一種方式
    #Test.objects.filter(id=1),update(name='Google')

    #修改所有的列
    #Test.objects.all(),update(name='Google')

    #return HttpResponse("<p>修改成功</p>")

#數據庫操作 刪除數據
#def testdb(request):
    # 刪除id=1的數據
    #test1 = Test.objects.get(id=1)
    #test1.delete()

    #另外一種方式
    #Test.objects.filter(id=1).delete()

    #刪除所有數據
    #Test.objects.all().delete()

    #return HttpResponse("<p>刪除成功</p>")
