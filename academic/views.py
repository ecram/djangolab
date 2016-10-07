from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, render_to_response, RequestContext
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from datetime import datetime
from datetime import date

from .forms import *
from .models import *
from publications.models import *
from django.db.models import Q

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
	newdoc = Meeting.objects.all().order_by('-date_meeting')[:3]
	professor = Person.objects.exclude(professor_categories="nop").order_by("name_person")
	course = Course.objects.all().order_by("code_course")
	return render_to_response("index.html", dict(newdoc=newdoc, professor=professor, course=course))
	

def contact(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			newdoc = Comment(name_comment = request.POST['name_comment'], email_comment = request.POST['email_comment'], message_comment = request.POST['message_comment'], ip_comment = get_client_ip(request))
			newdoc.save()
			name = request.POST.get('name_comment', '')
			subject = "New LASCA Message"
			message = request.POST.get('message_comment', '')
			from_email = request.POST.get('email_comment', '')
			to_email = "mpalma@lasca.ic.unicamp.br"
			if name and message and from_email:
				try:
					send_mail(subject, "********** Message sent from the Collector System - BAMTA Malware ********** \n\nNAME: "+name+"\n\n-----------------------------------\n\nMESSAGE: \n\n"+message, from_email, [to_email])
				except BadHeaderError:
					return HttpResponse('Invalid header found')
				return render(request, 'successful_message.html', {'newdoc': newdoc})
			else:
				return HttpResponse('Invalid header found')
	else:
		form = CommentForm()
	return render_to_response("index.html",
								locals(),
								context_instance=RequestContext(request))

def about(request):
	if About.objects.all().count() >= 1:
		newdoc = About.objects.all()
		return render(request, 'about.html', {'newdoc': newdoc})
	return render_to_response("abouts.html", 
                                locals(),
                                context_instance=RequestContext(request))

def projects(request):
	if Project.objects.all().count() >= 1:
		newdoc = Project.objects.all()
		return render(request, 'projects.html', {'newdoc': newdoc})
	return render_to_response("noprojects.html", 
                                locals(),
                                context_instance=RequestContext(request))

def courses(request):
	if Course.objects.all().count() >= 1:
		newdoc = Course.objects.all()
		return render(request, 'courses.html', {'newdoc': newdoc})
	return render_to_response("nocourses.html", 
                                locals(),
                                context_instance=RequestContext(request))

def meetings(request):
	if Meeting.objects.all().count() >= 1:
		today = date.today()
		newdoc = Meeting.objects.all()
		for item in newdoc:
			if (today.year > item.date_meeting.year) or (today.month > item.date_meeting.month) or (today.day > item.date_meeting.day):
				item.past_event = True
			else:
				item.past_event = False
			item.save()
		newdoc = Meeting.objects.all().order_by('-date_meeting')
		return render(request, "meetings.html", {'newdoc': newdoc})
	return render_to_response("nomeetings.html", 
                                locals(),
                                context_instance=RequestContext(request))

def conferences(request):
	if Conference.objects.all().count() >= 1:
		today = date.today()
		newdoc = Conference.objects.all()
		for item in newdoc:
			if item.start_conference:
				if (today.year < item.start_conference.year) or (today.month < item.start_conference.month) or (today.day < item.start_conference.day):
					item.past_conference = False
				else:
					item.past_conference = True
			else:
				item.past_conference = True
			item.save()
		newdoc = Conference.objects.all().order_by('acronym_conference')
		return render(request, "conferences.html", {'newdoc': newdoc})
	return render_to_response("noconferences.html", 
                                locals(),
                                context_instance=RequestContext(request))

def people(request):
	if Person.objects.all().count() >= 1:
		newdoc = Person.objects.all().order_by('name_person')
		return render(request, "people.html", {'newdoc': newdoc})
	return render_to_response("nopeople.html", 
                                locals(),
                                context_instance=RequestContext(request))


def error404(request):
    return render_to_response("error404.html", 
                                locals(),
                                context_instance=RequestContext(request))

def error500(request):
    return render_to_response("error500.html", 
                                locals(),
                                context_instance=RequestContext(request))

def awards(request):
	if Award.objects.all().count() >= 1:
		newdoc = Award.objects.all().order_by('-data')
		return render(request, "awards.html", {'newdoc': newdoc})
	return render_to_response("noawards.html", 
                                locals(),
                                context_instance=RequestContext(request))

def reports(request, year=None):
	# Select data
	publications = Publication.objects.select_related()
	awards = Award.objects.exclude(data__isnull=True)
	people = Person.objects.exclude(start_course__isnull=True)
	projects = Project.objects.exclude(start_project__isnull=True)
	allyears = Report.objects.filter(hidden=False)
	if year:
		dyear = datetime.strptime('Jan 1 '+str(year), '%b %d %Y')
		fyear = datetime.strptime('Dec 31 '+str(year), '%b %d %Y')
		awards = awards.filter(data__year=year).order_by('data')
		publications = publications.filter(year=year, external=False)
		# For people
		people = people.filter(Q(end_course__gte=dyear) | Q(end_course__isnull=True))
		people = people.filter(start_course__lte=fyear).order_by('name_person').distinct('name_person')
		# For projects
		projects = projects.filter(Q(end_project__gte=dyear) | Q(end_project__isnull=True))
		projects = projects.filter(start_project__lte=fyear).order_by('name_project')
		flag = 1
		# Calculate the rest of data for report
		pro_count = people.count() - people.filter(professor_categories="nop").count() - people.filter(professor_categories="pco").count()
		msc_count = people.filter(group_person="msc").count()
		phd_count = people.filter(group_person="phd").count()
		pos_count = people.filter(group_person="pos").count()
		ras_count = people.filter(group_person="ras").count()
		pas_count = people.filter(past_visitor=True).count()
		msc_defended = people.filter(group_person="msc", end_course__lte=fyear).count()
		phd_defended = people.filter(group_person="phd", end_course__lte=fyear).count()
	else:
		flag = 0

	if flag == 1:
		return render_to_response("reports.html", dict(awards=awards, publications=publications, people=people, 
			projects=projects, allyears=allyears, year=year, pro_count=pro_count, msc_count=msc_count, phd_count=phd_count,
			pos_count=pos_count, msc_defended=msc_defended, phd_defended=phd_defended, ras_count=ras_count, pas_count=pas_count))
	else:
		return render(request, 'noreports.html', {'allyears': allyears})
