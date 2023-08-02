from django.forms import ModelForm, fields
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class":"task_entry","placeholder":"Enter task"})

