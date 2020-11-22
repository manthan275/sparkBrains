from datetime import datetime
def universal_data(request):
	context = {}
	now = datetime.now()
	context['year'] = datetime.strftime(now,"%Y")
	return context