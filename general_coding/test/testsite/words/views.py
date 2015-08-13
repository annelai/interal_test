from django.shortcuts import render
from words.models import Word


# Create your views here.
def show_word(request):
	words = Word.objects.all().order_by('?')[0]
	return render(request, 'hello.html', {"words": words, })