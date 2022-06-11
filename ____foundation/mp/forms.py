from django import forms


from .models import Word, Verse

# forms below

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['name', 'description', 'detailed']


class VerseForm(forms.ModelForm):
    class Meta:
        model = Verse
        fields = ['title', 'verse']

        example_title = '1 Chronicles 16:11'
        example_verse = 'Seek the Lord and his strength, seek his face continually'

        widgets = {
                'title': forms.TextInput(attrs={'class': 'title_input', 'placeholder': example_title}),
                'verse': forms.TextInput(attrs={'class': 'verse_input', 'placeholder': example_verse}),
                }
