from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User=get_user_model()
# class User_creationForm(BaseUserCreationForm):
#     model = User
#     fields=['username','password1','password2']
#     widgets={
#             'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#             'password1':forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
#             'password2':forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
#         }
    
#     def save(self,commit):
#         if commit:
#             return super().save(commit=True)

class User_creationForm(UserCreationForm):
    username=forms.CharField(label='Имя пользователя',min_length=4,max_length=10,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))                 
    email=forms.EmailField(label='Электронная почта',widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    password1=forms.CharField(label='Пароль',min_length=8,max_length=15,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})) 
    password2=forms.CharField(label='Подтверждение пароля',min_length=8,max_length=15,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    
    field_order=['username','email','password1','password2']
        
    def clean_username(self):
        username = self.cleaned_data['username']
        check_name=User.objects.filter(username=username)
        if check_name.count():
            raise forms.ValidationError('Пользователь с таким именем существует')
        else:
            return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        check_name=User.objects.filter(email=email)
        if check_name.count():
            raise forms.ValidationError('Пользователь с такой электронной почтой существует')
        else:
            return email
        
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2
    
    def save(self, commit=True):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']                          
            )
        return user