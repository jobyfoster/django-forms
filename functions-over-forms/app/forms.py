from django import forms


class HeyYouForm(forms.Form):
    name = forms.CharField()


class HowOldForm(forms.Form):
    birth_year = forms.IntegerField()
    end = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["birth_year"] > cleaned_data["end"]:
            self.add_error("end", "The end year must be higher than your birthyear!")

        return cleaned_data


class OrderTotalForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
