from django.contrib import admin
from .models import *

# Register your models here.

class AwardAdmin(admin.ModelAdmin):
	list_display = ('id', 'award', 'date', 'description_award', 'web_award')
	list_filter = ['id']
	search_fields = ['award']
	
admin.site.register(Award, AwardAdmin)

class ConferenceAdmin(admin.ModelAdmin):
	list_display = ('id', 'acronym_conference', 'name_conference', 
		'place_conference', 'deadline_conference', 
		'discontinued_conference')
	list_filter = ['id']
	search_fields = ['acronym_conference']
	
admin.site.register(Conference, ConferenceAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'code_course', 'name_course', 
		'website_course', 'professor_course', 'course_document')
	list_filter = ['id']
	search_fields = ['name_course']

admin.site.register(Course, CourseAdmin)

class FormAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'date', 
		'document', 'hidden')
	list_filter = ['id']
	search_fields = ['name']

admin.site.register(Form, FormAdmin)

class InstituteAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'acronym', 'address', 'phone',
		'website', 'email')
	list_filter = ['id']
	search_fields = ['name']

admin.site.register(Institute, InstituteAdmin)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_meeting', 'date_meeting', 
		'description_meeting', 'site_meeting', 'past_event')
	list_filter = ['id']
	search_fields = ['name_meeting']
	
admin.site.register(Meeting, MeetingAdmin)

fields = ['image_tag']
readonly_fields = ['image_tag']

class PeopleAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'position', 'author_name','email', 
		'personal_web','phone')
	list_filter = ['id', 'name']
	search_fields = ['name']

admin.site.register(People, PeopleAdmin)

class PositionAdmin(admin.ModelAdmin):
	list_display = ('id','name_position', 'position_description', 
		'document')
	list_filter = ['id', 'name_position']
	search_fields = ['name_position']

admin.site.register(Position, PositionAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'acronym', 'name', 'chair', 'website', 
		'start', 'end')
	list_filter = ['id']
	search_fields = ['name']
	
admin.site.register(Project, ProjectAdmin)

class ReportAdmin(admin.ModelAdmin):
	list_display = ('id', 'year', 'hidden')
	list_filter = ['id']
	search_fields = ['year']
	
admin.site.register(Report, ReportAdmin)

class ResearchAreaAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'date','area_description', 
		'area_discontinued')
	list_filter = ['id']
	search_fields = ['name']

admin.site.register(ResearchArea, ResearchAreaAdmin)

class ResearchTopicsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'area', 'date', 'index_description', 
		'index_button', 'topic_discontinued')
	list_filter = ['id']
	search_fields = ['name']

admin.site.register(ResearchTopics, ResearchTopicsAdmin)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_services', 'research_topic', 
		'description_service', 'service_triptych', 'past_service')
	list_filter = ['id']
	search_fields = ['name']

admin.site.register(Service, ServiceAdmin)

'''
class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_comment', 'email_comment', 'ip_comment', 
		'country_name_comment', 'message_comment')
	list_filter = ['id']
	search_fields = ['email_comment']
	
admin.site.register(Comment, CommentAdmin)
'''
