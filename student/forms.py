from  django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        # 如果model 已经定义过了,可以直接在原来的model上面修改行
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )

