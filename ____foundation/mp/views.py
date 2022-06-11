from django.shortcuts import render, redirect

from .models import Word, Verse
from .forms import WordForm, VerseForm
import re

# Create your views here.


def home(request):
    verses = Verse.objects.all()
    form_v = VerseForm()
    words = Word.objects.all()
    form_w = WordForm()

    all_words = []
    for i in words:
        all_words.append(i.name)  # is this needed? what about list(words.value())

    all_verses = []
    for x in verses:
        all_verses.append(x.title)

    if request.method == "POST":
        if 'verse_add' in request.POST:
            form1 = VerseForm(request.POST)
            if form1.is_valid():
                form2 = form1.save(commit=False)
                form2.title = re.sub("\s+", "", form2.title)
                form2.title = form2.title.lower()

                if form2.title in all_verses:
                    # Will have a message saying already added
                    pass
                elif form2.title not in all_verses:
                    form2.shown_title = form2.title
                    add_space1 = re.search('^[0-9]', form2.shown_title)
                    add_space2 = re.search('[a-zA-Z][0-9]', form2.shown_title)
                    add_space1 = add_space1.group()
                    add_space2 = add_space2.group()
                    form2.shown_title = re.sub('^[0-9]', f"{add_space1} ", form2.shown_title)
                    form2.shown_title = re.sub('[a-zA-Z][0-9]', f"{add_space2[0]} {add_space2[1]}", form2.shown_title)
                    form2.shown_title = form2.shown_title.title()


                    form2.mp_verse = form2.verse
                    form2.mp_verse = re.sub('[,!;.?“”:\"]', '', form2.mp_verse)
                    form2.mp_verse = form2.mp_verse.lower()
                    form2.save()

                    word_list = form2.mp_verse.split(" ")
                    for i in word_list:
                        if i not in all_words:
                            form_w = WordForm({'name': i.lower()})
                            all_words.append(i)  # add it to all words
                            if form_w.is_valid():
                                form_w.save()

                    return redirect('mp_home')

    context = {'verses': verses, 'form': form_v}
    response = render(request, 'mp/mp_home.html', context)
    return response


def detail(request, pk):
    verse = Verse.objects.get(id=pk)
    words = Word.objects.all()

    verse_words = verse.mp_verse.split(" ")
    word_details = []
    for i in words:
        word_details.append(i)

    choosen_words = []
    for i in verse_words:
        for x in word_details:
            if str(i) == str(x.name):
                choosen_words.append(x)

    context = {'words': words, 'verse': verse, 'choosen_words': choosen_words,}
    response = render(request, 'mp/mp_detail.html', context)
    return response

def word(request):
    words = Word.objects.all()
    form = WordForm()

    context = {'words': words, 'form': form,}
    response = render(request, 'mp/mp_word.html', context)
    return response



