from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Ad, Profile, Location, Review, Contact


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text='First Name' , widget=forms.TextInput(attrs={'placeholder':'User Name'}))
    first_name = forms.CharField(max_length=20, help_text='First Name' , widget=forms.TextInput(attrs={'placeholder':'First Name*'}))
    last_name = forms.CharField(max_length=20 , help_text='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=30 , help_text= 'Email' , widget=forms.TextInput(attrs={'placeholder':'Email*'}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Password*'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name',
                 'password1', 'password2')

class EditProfile(UserChangeForm):

    class Meta:
        model = User
        fields = ('username' , 'email' , 'first_name' , 'last_name' )


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('Old Password' , 'New Password' , 'Confirm Password')

class UserPicture(forms.ModelForm):
    # user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Your User Name"}))
    ad_profile_pic = forms.ImageField(help_text='max. 3 megabytes',widget= forms.FileInput(attrs={'accept':"image/*"}) , required=False)
    Phone = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"987*******"}))
    class Meta:
        model= Profile
        fields = ('ad_profile_pic','Phone')

class LocationForm(forms.ModelForm):
    location = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Address"}))
    city = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"City"}))
    state = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"State"}))
    pin_code = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Pin Code"}))
    class Meta:
        model = Location
        fields =('location' , 'city' , 'state' , 'pin_code')

STATUS= [
    ('True', 'Active'),
    ('False', 'Inactive')
    ]
STATES =[
    ('MP','MADHYA PRADESH'),
    ('UP','UTTAR PRADESH')
]

class AdForm(forms.ModelForm):

    ad_title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Title of your Ad"}))
    ad_brand = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Brand"}))
    ad_model = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Model"}))
    condition = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Condition"}))
    ad_price = forms.CharField(widget= forms.TextInput(attrs={'placeholder':"Price"}))
    ad_description = forms.CharField(widget= forms.Textarea(attrs={'placeholder':"Description"}))
    ad_image1 = forms.ImageField(help_text='max. 3 megabytes', widget=forms.FileInput(attrs={'accept': "image/*"}),required=True)
    ad_image2 = forms.ImageField(help_text='max. 3 megabytes', widget=forms.FileInput(attrs={'accept': "image/*"}), required=False)
    ad_image3 = forms.ImageField(help_text='max. 3 megabytes', widget=forms.FileInput(attrs={'accept': "image/*"}),required=False)
    ad_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Address"}))
    ad_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "City"}))
    ad_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "State"}))
    # state = forms.CharField(label='State', widget=forms.Select(attrs={'class' : 'py-2'} , choices=STATES))
    ad_pin_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Pin Code"}))
    ad_status = forms.CharField(label='Ad Status', widget=forms.RadioSelect(attrs={'class': 'py-2'}, choices=STATUS))

    class Meta:
        model = Ad
        fields ={'ad_title','ad_brand','ad_model','condition','ad_price',
                 'ad_description','ad_cat' , 'ad_subcat' , 'ad_image1','ad_image2',
                 'ad_image3', 'ad_status' ,'ad_location','ad_city','ad_state','ad_pin_code'}

class AdUpdate(forms.ModelForm):
    class Meta:
        model = Ad
        fields ={'ad_title','ad_brand','ad_model','condition','ad_price',
                 'ad_description','ad_cat' , 'ad_subcat' , 'ad_image1','ad_image2',
                 'ad_image3', 'ad_status'}

class ReviewForm(forms.ModelForm):
    subject = forms.CharField(widget= forms.TextInput(attrs={'placeholder' :"Subject"}))
    message = forms.CharField(widget= forms.Textarea(attrs={'placeholder' :"Message"}))

    class Meta:
        model = Review
        fields = {'subject','message',}

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Name"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Type Your Message"}))

    class Meta:
        model = Contact
        fields = {'name','subject', 'message' }
