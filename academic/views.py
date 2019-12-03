from django.shortcuts import render, render_to_response
from datetime import datetime, date
from django.db.models import Q, Count

from publications.models import *
from academic.models import *


def index(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	forms = Form.objects.all().order_by("-date").exclude(hidden=True)[:5]
	courses = Course.objects.all().order_by("name_course")
	events = Meeting.objects.exclude(past_event = 'True')
	events = events.all().order_by('-date_meeting')[:4]
	eve_count = events.count()
	conferences = Conference.objects.exclude(discontinued_conference='True')
	conferences = conferences.all().order_by('-deadline_conference')[:4]
	conf_count = conferences.count()
	topics = ResearchTopics.objects.exclude(topic_discontinued = True)
	topics = topics.all()
	tps_count = ResearchTopics.objects.all().count()
	return render_to_response("academic/index.html", dict(events=events, 
		eve_count=eve_count, services=services, topics=topics, 
		tps_count=tps_count, forms=forms, conferences=conferences, 
		conf_count=conf_count))

def areas(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	areas = ResearchArea.objects.exclude(area_discontinued = True)
	if areas.all().count() >= 1:
		areas = areas.all().order_by('name')
		return render_to_response("academic/areas.html", 
			dict(areas=areas, services=services))
	return render_to_response("academic/noareas.html",
		dict(services=services))

def about(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	if Institute.objects.all().count() >= 1:
		institutos = Institute.objects.all()
		topics = ResearchTopics.objects.exclude(topic_discontinued = True)
		return render_to_response("academic/about.html", 
			dict(institutos=institutos, services=services, topics=topics))
	return render_to_response('academic/noabout.html',
		dict(services=services))

def awards(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	if Award.objects.all().count() >= 1:
		awards = Award.objects.all().order_by('-date')
		return render_to_response("academic/awards.html", 
			dict(awards=awards, services=services))
	return render_to_response("academic/noawards.html")

def conferences(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	conferences = Conference.objects.exclude(discontinued_conference='True')
	if conferences.all().count() >= 1:
		return render_to_response("academic/conferences.html", 
			dict(conferences=conferences, services=services))
	return render_to_response("academic/noconferences.html",
		dict(services=services))

def courses(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	courses = Course.objects.exclude(past_course='True')
	if courses.all().count() >= 1:
		return render_to_response("academic/courses.html", 
			dict(courses=courses, services=services))
	return render_to_response("academic/nocourses.html",
		dict(services=services))

def forms(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	forms = Form.objects.all().order_by("-date").exclude(hidden=True)
	if forms.all().count() >= 1:
		return render_to_response("academic/forms.html", 
			dict(forms=forms, services=services))
	return render_to_response("academic/noforms.html",
		dict(services=services))

def meetings(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	meetings = Meeting.objects.exclude(past_event = 'True')
	if meetings.all().count() >= 1:
		meetings = meetings.all().order_by('-date_meeting')
		return render_to_response("academic/meetings.html", 
			dict(meetings=meetings, services=services))
	return render_to_response("academic/nomeetings.html",
		dict(services=services))

def people(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	positions = Position.objects.all()
	research_topics = ResearchTopics.objects.all().order_by("name")
	active_members = People.objects.exclude(hidden_member = True)
	current_members = active_members.exclude(past_member = True)
	pm_count = active_members.filter(past_member = True).count()
	dir_count = current_members.filter(position__name_position__contains='Director(a)').count()
	cte_count = current_members.filter(technical_committee = True).count()
	exe_count = current_members.filter(executive_committee = True).count()
	ced_count = current_members.filter(editor_committee = True).count()
	scp_count = current_members.filter(scholarship_committee = True).count()
	res_member = current_members.exclude(research_topic__name__isnull=True)
	res_member = res_member.exclude(position__name_position__contains='Director(a)')
	res_member = res_member.exclude(technical_committee=True).exclude( 
		executive_committee=True).exclude(scholarship_committee=True)
	res_members = res_member.exclude(editor_committee=True).order_by('position__name_position')
	res_count = res_members.count()
	adm_count = current_members.filter( position__name_position__contains='Personal Administrativo' ).count()
	if active_members.all().count() >= 1:
		members = active_members.all().order_by('name')
		return render_to_response("academic/people.html", 
			dict(members=members, services=services, 
				research_topics=research_topics, dir_count=dir_count, positions=positions,
				cte_count=cte_count, ced_count=ced_count, adm_count=adm_count, 
				res_count=res_count, res_members=res_members, pm_count=pm_count, 
				exe_count=exe_count, scp_count=scp_count))
	return render_to_response("academic/nopeople.html",
		dict(services=services))

def projects(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	projects = Project.objects.all()
	topics = ResearchTopics.objects.exclude(topic_discontinued = True)
	tp = Project.objects.order_by('topic__id').distinct('topic__id')
	if projects.all().count() >= 1:
		return render_to_response("academic/projects.html", 
			dict(projects=projects, services=services, topics=topics, 
				tp=tp))
	return render_to_response("academic/noprojects.html",
		dict(services=services))

def projects_details(request):
	services = Service.objects.all().exclude(past_service=True)[:8]
	projects = Project.objects.all()
	topics = ResearchTopics.objects.exclude(topic_discontinued = True)
	tp = Project.objects.order_by('topic__id').distinct('topic__id')
	if projects.all().count() >= 1:
		return render_to_response("academic/projects_details.html", 
			dict(projects=projects, services=services, topics=topics, 
				tp=tp))
	return render_to_response("academic/noprojects.html",
		dict(services=services))

def services(request):
	services = Service.objects.all().exclude(past_service=True).order_by('name_services')
	if services.all().count() >= 1:
		return render_to_response("academic/services.html", 
			dict(services=services))
	return render_to_response("academic/noservices.html",
		dict(services=services))

def topics(request):
	services = Service.objects.all().exclude(past_service=True).order_by('name_services')
	topics = ResearchTopics.objects.exclude(topic_discontinued = True)
	if topics.all().count() >= 1:
		topics = topics.all().order_by('name')
		return render_to_response("academic/topics.html", 
			dict(topics=topics, services=services))
	return render_to_response("academic/notopics.html",
		dict(topics=topics, services=services))

def reports(request, year=None):
	positions = Position.objects.all()
	people = People.objects.filter(past_member=False).filter( hidden_member=False
		).order_by('name').distinct('name')
	areas = ResearchArea.objects.exclude(area_discontinued=True)
	topics = ResearchTopics.objects.exclude(topic_discontinued=True)
	projects = Project.objects.exclude(start__isnull=True)
	publications = Publication.objects.select_related()
	awards = Award.objects.exclude(date__isnull=True)
	services = Service.objects.exclude(past_service=True)
	courses = Course.objects.exclude(past_course=True)
	allyears = Report.objects.filter(hidden=False)
	if year:
		flag = 1
		dyear = datetime.strptime('Jan 1 '+str(year), '%b %d %Y')
		fyear = datetime.strptime('Dec 31 '+str(year), '%b %d %Y')
		# For areas and topics research
		are_count = areas.count()
		top_count = topics.count()
		# For people
		peo_count = people.count()
		active_members = People.objects.exclude(hidden_member = True)
		pm_count = active_members.filter(past_member = True).count()
		dir_count = people.filter(position__name_position__contains='Director(a)').count()
		cte_count = people.filter(technical_committee = True).count()
		cej_count = people.filter(executive_committee = True).count()
		ced_count = people.filter(editor_committee = True).count()
		cbe_count = people.filter(scholarship_committee = True).count()
		adm_count = people.filter( position__name_position__contains='Personal Administrativo' ).count()
		res_members = people.exclude(research_topic__name__isnull=True)
		res_members = res_members.exclude(position__name_position__contains='Director(a)')
		res_members = res_members.exclude(technical_committee=True).exclude( 
			executive_committee=True).exclude(scholarship_committee=True).exclude(
			editor_committee=True)
		res_count = res_members.count()
		# For projects
		projects = projects.filter(Q(end__gte=dyear) | Q(end__isnull=True))
		projects = projects.filter(start__lte=fyear).order_by('name')
		pro_count = projects.count()
		# For Publications
		publications = publications.filter(year=year, external=False)
		pub_count = publications.count()
		# For Awards
		awards = awards.filter(date__year=year).order_by('date')
		awa_count = awards.count()
		# For Services and Courses
		ser_count = services.count()
		cou_count = courses.count()
		# For Topics Researchs
		#result = res_members.values('research_topic').order_by('research_topic').annotate(count=Count('research_topic'))
	else:
		flag = 0

	if flag == 1:
		return render_to_response("academic/reports.html", 
			dict(people=people, peo_count=peo_count,
				positions=positions, allyears=allyears, 
				year=year, areas=areas, are_count=are_count, 
				topics=topics, top_count=top_count, 
				projects=projects, pro_count=pro_count, 
				publications=publications, pub_count=pub_count, 
				awards=awards, awa_count=awa_count, 
				services=services, ser_count=ser_count, 
				courses=courses, cou_count=cou_count, 
				dir_count=dir_count, cte_count=cte_count, 
				cej_count=cej_count, ced_count=ced_count, 
				cbe_count=cbe_count, res_members=res_members, 
				res_count=res_count, adm_count=adm_count))
	else:
		return render(request, 'academic/noreports.html', {'allyears': allyears, 
			'services': services})

def error404(request, exception):
    return render(request,'academic/error404.html', status=404) 

def error500(request):
    return render(request,'academic/error500.html', status=500)

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
				return render(request, 'academic/successful_message.html', {'newdoc': newdoc})
			else:
				return HttpResponse('Invalid header found')
	else:
		form = CommentForm()
	return render_to_response("academic/index.html")
