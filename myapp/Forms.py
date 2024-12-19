from django import forms
class Studentform(forms.Form):
	name=forms.CharField()
	usn=forms.CharField()
	mob=forms.IntegerField()
	branch=forms.CharField()
	email=forms.CharField()