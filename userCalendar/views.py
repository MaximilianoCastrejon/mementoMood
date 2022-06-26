from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
# Create your views here.

APP_LANGUAGES = ['es', 'fr', 'de', 'en']

def home_calendar(request):
	trans = translate(language='fr')
	context = {
		'LANGUAGE_OPTIONS': APP_LANGUAGES,
		'translated': trans,
	}

	return render(request, "base.html", context)

def translate(language):
	cur_lannguage = get_language()
	try:
		activate(language)
		text = _('Hello')
	finally:
		activate(cur_lannguage)
	return(text)