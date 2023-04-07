from .models import Opportunity,Position
from django import forms
from django.contrib import messages


class OpportunityForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())
    class Meta:
        model = Opportunity
        fields = '__all__'
        exclude=["user","is_applicant","published","job_type","salary","location",]

        def clean(self):
            clean_data= super.clean()
            if not request.user:
                raise ValidationError(
                    format_html("<p style='background-color:pink; color:white'>You must be a registered and signedin user to submit this form</p>")
                )
            return  clean_data   
                
                # raise forms.ValidationError("Title already exists, choose a unique title.")
     