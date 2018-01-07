from django import forms
from chronos.models import Category, Task

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name:")

    class Meta:
        model = Category
        fields = ('name',)


class TaskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
                                     Category.objects.filter(user=user))
        
    name = forms.CharField(max_length=300, help_text="Enter a task:")

    

    class Meta:
        model = Task

        fields = ('name', 'category')