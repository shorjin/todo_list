from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'todo_text'}))

