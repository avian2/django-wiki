from django import forms as forms

from models import Page

class PageForm(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        import re
        from templatetags.wiki import WIKI_WORD

        name = self.cleaned_data['name']
        match = re.match(WIKI_WORD, name)
        if not (match and match.group() == name):
            raise forms.ValidationError('Must be a WikiWord.')

        return name
