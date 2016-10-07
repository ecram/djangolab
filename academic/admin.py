from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_comment', 'email_comment', 'country_name_comment', 'message_comment')
	list_filter = ['id']
	search_fields = ['email_comment']
	
admin.site.register(Comment, CommentAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_project', 'start_project', 'end_project', 'monitor_project', 'link_project')
	list_filter = ['id']
	search_fields = ['name_project']
	
admin.site.register(Project, ProjectAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'code_course', 'name_course', 'professor_course', 'prerequisites_course', 'website_course')
	list_filter = ['id']
	search_fields = ['name_course']
	
admin.site.register(Course, CourseAdmin)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('id', 'date_meeting', 'description_meeting', 'past_event')
	list_filter = ['id']
	search_fields = ['description_meeting']
	
admin.site.register(Meeting, MeetingAdmin)

class ConferenceAdmin(admin.ModelAdmin):
	list_display = ('id', 'acronym_conference', 'name_conference', 'place_conference', 'deadline_conference', 'past_conference')
	list_filter = ['id']
	search_fields = ['acronym_conference']
	
admin.site.register(Conference, ConferenceAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('id','name_person','email_person','group_person','size','thumbnail','advisor','start_course','end_course')
	list_filter = ['id', 'group_person']
	search_fields = ['name_person']

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()
	
admin.site.register(Person, PersonAdmin)

class AboutAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'html_text')
	list_filter = ['id']
	search_fields = ['title']
	
admin.site.register(About, AboutAdmin)

class AwardAdmin(admin.ModelAdmin):
	list_display = ('id', 'award', 'prize', 'data', 'description_award')
	list_filter = ['id']
	search_fields = ['award']
	
admin.site.register(Award, AwardAdmin)

class ReportAdmin(admin.ModelAdmin):
	list_display = ('id', 'year', 'hidden')
	list_filter = ['id']
	search_fields = ['year']
	
admin.site.register(Report, ReportAdmin)
