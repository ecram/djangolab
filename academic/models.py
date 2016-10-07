from django.db import models
from django.contrib.gis.geoip import GeoIP
from django.core.validators import MaxLengthValidator
from string import join
from django.core.mail import send_mail, BadHeaderError
import os
from PIL import Image as PImage
from django.conf import settings

# Codigo recaptcha-client-1.0.6
import base64
import cgi

try:
    from Crypto.Cipher import AES
except:
    raise Exception ("You need the pycrpyto library: http://cheeseshop.python.org/pypi/pycrypto/")

MAIL_HIDE_BASE="http://www.google.com/recaptcha/mailhide"

def asurl (email,
                 public_key,
                 private_key):
    """Wraps an email address with reCAPTCHA mailhide and
    returns the url. public_key is the public key from reCAPTCHA
    (in the base 64 encoded format). Private key is the AES key, and should
    be 32 hex chars."""
    
    cryptmail = _encrypt_string (email, base64.b16decode (private_key, casefold=True), '\0' * 16)
    base64crypt = base64.urlsafe_b64encode (cryptmail)

    return "%s/d?k=%s&c=%s" % (MAIL_HIDE_BASE, public_key, base64crypt)

def ashtml (email,
                  public_key,
                  private_key):
    """Wraps an email address with reCAPTCHA Mailhide and
    returns html that displays the email"""

    url = asurl (email, public_key, private_key)
    (userpart, domainpart) = _doterizeemail (email)
    return """<a href='%(url)s' onclick="window.open('%(url)s', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">%(user)s...@%(domain)s...</a>""" % {
        'user' : cgi.escape (userpart),
        'domain' : cgi.escape (domainpart),
        'url'  : cgi.escape (url),
        }

def _pad_string (str, block_size):
    numpad = block_size - (len (str) % block_size)
    return str + numpad * chr (numpad)

def _encrypt_string (str, aes_key, aes_iv):
    if len (aes_key) != 16:
        raise Exception ("expecting key of length 16")
    if len (aes_iv) != 16:
        raise Exception ("expecting iv of length 16")
    return AES.new (aes_key, AES.MODE_CBC, aes_iv).encrypt (_pad_string (str, 16))


def _doterizeemail (email):
    """replaces part of the username with dots"""
    try:
        [user, domain] = email.split ('@')
    except:
        # handle invalid emails... sorta
        user = email
        domain = ""

    if len(user) <= 4:
        user_prefix = user[:1]
    elif len(user) <= 6:
        user_prefix = user[:3]
    else:
        user_prefix = user[:4]

    if len(domain) <= 4:
        user_domain = domain[:]
    elif len(user) <= 6:
        user_domain = domain[:5]
    else:
        user_domain = domain[:5]

    return (user_prefix, user_domain)
"""    
    try:
        [user, domain] = email.split ('@')
    except:
        # handle invalid emails... sorta
        user = email
        domain = ""

    if len(user) <= 4:
        user_prefix = user[:1]
    elif len(user) <= 6:
        user_prefix = user[:3]
    else:
        user_prefix = user[:4]

    return (user_prefix, domain)
"""

#Fim do codigo recaptcha-client-1.0.6

class Comment(models.Model):
	name_comment = models.CharField(max_length=50)
	email_comment = models.EmailField()
	message_comment = models.TextField(validators=[MaxLengthValidator(500)])
	ip_comment = models.CharField(max_length=40, null=True, blank=True)
	country_name_comment = models.CharField(max_length=100, null=True, blank=True)
	country_code_comment = models.CharField(max_length=4, null=True, blank=True)
	def save(self, *args, **kwargs):
		g = GeoIP()
		if self.ip_comment:
			if not self.ip_comment == "127.0.0.1":
				self.country_name_comment = g.country(self.ip_comment)
				self.country_code_comment = g.country_code(self.ip_comment)
			else:
				self.country_name_comment = "Brazil-Lasca"
				self.country_code_comment = "BRL"
		else:
			self.country_name_comment = "None"
			self.country_code_comment = "--"
		super(Comment, self).save(*args, **kwargs)

class Project(models.Model):
	acronym_project = models.CharField(max_length=20, null=True, blank=True)
	name_project = models.CharField(max_length=150)
	description_project = models.TextField(validators=[MaxLengthValidator(500)],
		help_text='Here the coordinator(s) can describe the sponsor and information about its project.')
	start_project = models.DateField(null=True, blank=True)
	end_project = models.DateField(null=True, blank=True)
	monitor_project = models.CharField('Coordinator(s)', max_length=100, null=True, blank=True,
		help_text='List the coordinators separated by commas or and.')
	link_project = models.CharField(max_length=300, null=True, blank=True)
	link_Webpage_monitor = models.CharField(max_length=300, null=True, blank=True)

class Course(models.Model):
	code_course = models.CharField(max_length=10)
	name_course = models.CharField(max_length=100)
	professor_course = models.CharField(max_length=100, null=True, blank=True)
	description_course = models.TextField(validators=[MaxLengthValidator(1000)], null=True, blank=True)
	prerequisites_course = models.TextField(validators=[MaxLengthValidator(500)], null=True, blank=True)
	website_course = models.CharField(max_length=300, null=True, blank=True)
	past_course = models.BooleanField(default=False)

class Meeting(models.Model):
	description_meeting = models.TextField(validators=[MaxLengthValidator(1000)])
	date_meeting = models.DateField()
	#spring_or_fall = models.CharField(max_length=6, null=True, blank=True)
	past_event = models.BooleanField(default=False)
	def save(self, *args, **kwargs):
		if (self.date_meeting.month == 1) or (self.date_meeting.month == 2) or (self.date_meeting.month == 3) or (self.date_meeting.month == 4) or (self.date_meeting.month == 5) or (self.date_meeting.month == 6):
			self.spring_or_fall = "fall"
		else:
			self.spring_or_fall = "spring"
		"""
		name = "Web Site Admin"
		subject = "New LASCA Event"
		message = self.description_meeting
		from_email = "noreply@lasca.ic.unicamp.br"
		to_email = "mpalma@lasca.ic.unicamp.br"
		if name and message and from_email:
			try:
				send_mail(subject, "********** New LASCA Event ********** \n\nNAME: "+name+"\n\n-----------------------------------\n\nMESSAGE: \n\n"+message, from_email, [to_email])
			except BadHeaderError:
				return HttpResponse('Invalid header found')
		"""
		super(Meeting, self).save(*args, **kwargs)

class Conference(models.Model):
	acronym_conference = models.CharField(max_length=50)
	name_conference = models.CharField(max_length=200)
	place_conference = models.CharField(max_length=100, null=True, blank=True)
	start_conference = models.DateField(null=True, blank=True)
	end_conference = models.DateField(null=True, blank=True)
	deadline_conference = models.DateField(null=True, blank=True)
	site_conference = models.CharField(max_length=200, null=True, blank=True)
	qualis_cc = models.CharField(max_length=2, null=True, blank=True)
	past_conference = models.BooleanField(default=False)

class Person(models.Model):
	Faculty = 'fac'
	Post_Doc = 'pos'
	PhD_Student = 'phd'
	MsC_Student = 'msc'
	Junior_Research = 'sis'
	Research_Assistant = 'ras'
	Alumni = "alu"
	Scientific_Categories = (
			(Faculty, 'Faculty'),
			(Post_Doc, 'Post Doc'),
			(PhD_Student, 'PhD Student'),
			(MsC_Student, 'MsC Student'),
			(Junior_Research, 'Junior Research'),
			(Research_Assistant, 'Research Assistant'),
			(Alumni, 'Alumni'),
		)
	No_Professor = 'nop'
	Professor_Colaborador = 'pco'
	Professor_Doutor_I  = 'pd1'
	Professor_Doutor_II  = 'pd2'
	Professor_Doutor_III = 'pd3'
	Professor_Assistente = 'pa0'
	Professor_Associado_I = 'pa1'
	Professor_Associado_II = 'pa2'
	Professor_Associado_III = 'pa3'
	Professor_Titular = 'pti'
	Professor_Categories = (
			(No_Professor, 'No Professor'),
			(Professor_Colaborador, 'Professor Colaborador'),
			(Professor_Doutor_I, 'Professor Doutor I'),
			(Professor_Doutor_II, 'Professor Doutor II'),
			(Professor_Doutor_III, 'Professor Doutor III'),
			(Professor_Associado_I, 'Professor Associado I'),
			(Professor_Associado_II, 'Professor Associado II'),
			(Professor_Associado_III, 'Professor Associado III'),
			(Professor_Titular, 'Professor Titular'),
		)
	group_person = models.CharField(max_length=3, choices=Scientific_Categories, 
		default=MsC_Student,
		help_text='Category of the academic persone.')
	# Title
	name_person = models.CharField('Name', max_length=100,
		help_text='Use the full name.')
	email_person = models.CharField('Work email', max_length=100,
		help_text='Preferably the LASCA email.')
	email_link = models.CharField('reCAPTCHA email', max_length=700, null=True, blank=True,
		help_text='Do not use this space.')
	personal_web = models.CharField('Personal Web', max_length=100, null=True, blank=True)
	lattes_link = models.CharField('Lattes', max_length=50, null=True, blank=True)
	telephone = models.CharField(max_length=50, null=True, blank=True)
	past_visitor = models.BooleanField('Past Visitor', default=False)
	advisor = models.CharField('Advisor', max_length=100, null=True, blank=True,
		help_text='Use the same name register in People.')
	co_advisor = models.CharField('Co-Advisor', max_length=100, null=True, blank=True,
		help_text='List the co-advidors separated by commas or and.')
	professor_categories = models.CharField(max_length=3, null=True, blank=True, 
		choices=Professor_Categories, 
		default=No_Professor,
		help_text='Category ONLY FOR Professors.')
	start_course = models.DateField('Start course or career', null=True, blank=True)
	end_course = models.DateField('End course or career', null=True, blank=True)
	# image
	image = models.FileField(upload_to = 'images/', default='images/no-img.png')
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	def save(self, *args, **kwargs):
		super(Person, self).save(*args, **kwargs)
		im = PImage.open(os.path.join(settings.MEDIA_ROOT, self.image.name))
		self.width, self.height = im.size
		public_key = '01RfnRrcXL-DTTEMvMq5ItsQ=='
		private_key = '2c5cd00024cbfe592481106592116bc7'
		self.email_link = ashtml(self.email_person, public_key, private_key)
		super(Person, self).save(*args, **kwargs)
	def size(self):
		return "%s x %s" % (self.width, self.height)
	def __unicode__(self):
		return self.image.name
	def thumbnail(self):
		return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % ( (self.image.name, self.image.name))
		#return '<img src="/media/%s" width="100" height="100" />' % (self.image.name)
	thumbnail.allow_tags = True
	thumbnail.short_description = 'Thumb'
	class Meta:
		verbose_name_plural = 'People'

class About(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	html_text = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'About'

class Award(models.Model):
	award = models.CharField(max_length=200,
		help_text='Full name of the award or acknowledgment.')
	prize = models.CharField(max_length=100, help_text='Use the full name.')
	data = models.DateField('Day of the awards ceremony', null=True, blank=True)
	description_award= models.TextField(validators=[MaxLengthValidator(1000)])
	class Meta:
		verbose_name_plural = 'Awards'

class Report(models.Model):
	year = models.IntegerField(help_text='Write the report year from main view.')
	hidden = models.BooleanField(default=False,
		help_text='Hide report year from main view.')
	class Meta:
		verbose_name_plural = '  Reports'
