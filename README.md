# python-django 学习
### 1. django环境搭建

使用idea新建django项目
新建应用 
python manage.py startapp appname
在新建的应用下的 models 创建model
```python
class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (2, '通过'),
        (3, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="邮箱")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=123, verbose_name="电话")

    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"

```
如果需要后台则在admin.py 创建 admin类
```python
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    list_filter = ('sex', 'status', 'created_time')
    search_fields = ('name', 'profession')

    fieldsets = (
        (None, {
            'fields': (
            'name',
            ('sex', 'profession'),
            ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )


admin.site.register(Student, StudentAdmin)
```
在setting.py 中添加新建的应用
使用以下命令
```python
python manage.py makemigrations
python manage.py migrate
 
```
创建后台超级管理员账号
```python
python manage.py createsuperuser
```

