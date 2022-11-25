from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()


class StudentLoginForm(forms.Form):
    username=forms.CharField();
    password=forms.CharField(widget=forms.PasswordInput)


from django.core import validators
class FeedBackForm(forms.Form):
    '''def starts_with_b(val):
        if val[0]!='b':
            raise forms.ValidationError('Name should start with b only...')'''
    '''
    name = forms.CharField(validators=[validators.RegexValidator('[A-Z][a-z]*')])
    rollno = forms.IntegerField(validators=[validators.RegexValidator('[5]\d{2}')])
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    '''

    '''
    def clean_name(self):
        print("validating name...")
        inp_name=self.cleaned_data['name']
        if len(inp_name)<4 or len(inp_name)>10:
            raise forms.ValidationError("Name should be Min 4 and Max 10 characters...")

    def clean_email(self):
        inputemail = self.cleaned_data['email'];
        print("Validating email-field...");
        if len(inputemail) < 8:
            raise forms.ValidationError('Email-field cannot be EMPTY or less than 3-chars...');
        return inputemail;

    def clean_feedback(self):
        inputfeedback = self.cleaned_data['feedback']
        print("Validating feedback-field...");
        if len(inputfeedback) < 3:
            raise forms.ValidationError('Feedback-field cannot be less than 3-chars...');
        return inputfeedback'''

    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea);

    def clean(self):
        print('Total Form validation... is getting done!!!')
        total_cleaned_data = super().clean();  # gets complete form submitted data
        inputname = total_cleaned_data['name'];
        if inputname[0].lower() != 's':
            raise forms.ValidationError('Name parameter should start with S or s only...');
        inputrollno = total_cleaned_data['rollno'];
        if inputrollno <= 0:
            raise forms.ValidationError('Rollno should be > 0...')
        inputfeedback = total_cleaned_data['feedback'];
        if len(inputfeedback) < 10 or len(inputfeedback) > 50:
            raise forms.ValidationError('Feedback should be min 10-chars & max 50-chars...')

class SignupForm(forms.Form):
    name=forms.CharField(label='Enter your name :')
    #password=forms.CharField(widget=forms.PasswordInput,validators=[validators.RegexValidator('[A-Z]*[a-z]*[0-9]*[@#&$]')])
    password=forms.CharField(widget=forms.PasswordInput,validators=[validators.RegexValidator('^.*(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$&=!%^])')])
    repassword=forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    email=forms.EmailField()
    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['repassword']
        if pwd!=rpwd:
            raise forms.ValidationError('Both Passwords must be same...!!!')
        if len(pwd) < 8 or len(pwd) > 15:
            raise forms.ValidationError('Password should be min=8 & max=15 chars...')
        if len(rpwd) < 8 or len(rpwd) > 15:
            raise forms.ValidationError('Re-Password should be min=8 & max=15 chars...')



