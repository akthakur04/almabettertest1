from django import forms
class studmarks(forms.Form):
    roll_no = forms.IntegerField(required=True, widget=forms.TextInput())
    name =forms.CharField(required=True,widget=forms.TextInput())
    Math_marks =forms.IntegerField(required=True,widget=forms.TextInput())
    Physics_marks =forms.IntegerField(required=True,widget=forms.TextInput())
    Chem_marks =forms.IntegerField(required=True,widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(studmarks, self).__init__(*args, **kwargs)
        self.fields['roll_no'].label = "Roll No.:"
        self.fields['name'].label = "Name:"
        self.fields['Math_marks'].label = "marks in maths"
        self.fields['Physics_marks'].label = "marks in physics:"
        self.fields['Chem_marks'].label = "marks in chemistry:"