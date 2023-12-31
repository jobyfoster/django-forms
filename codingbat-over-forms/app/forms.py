from django import forms


class FontTimesForm(forms.Form):
    phrase = forms.CharField()
    copies = forms.IntegerField(min_value=1)


class NoTeenSumForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class XYZThereForm(forms.Form):
    phrase = forms.CharField()


class CenteredAverageForm(forms.Form):
    num_one = forms.IntegerField()
    num_two = forms.IntegerField()
    num_three = forms.IntegerField()
    num_four = forms.IntegerField()
    num_five = forms.IntegerField()
    num_six = forms.IntegerField(required=False)
    num_seven = forms.IntegerField(required=False)
