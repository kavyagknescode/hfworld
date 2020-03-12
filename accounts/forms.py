from registration.forms import RegistrationForm

class MyRegForm(RegistrationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'

        for fieldname in ['username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = False
