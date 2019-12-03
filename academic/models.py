from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator

# Variables
Instituto_de_Investigacion = 'Insituto de Investigación '
Sigla = 'II'
Facultad = 'Facultad de Ciencias Puras y Naturales'
Carrera = 'Carrera de '

# Crea tus modelos aqui

class Conference(models.Model):
	id = models.AutoField(primary_key = True)
	acronym_conference = models.CharField('Sigla de la Conferencia', max_length=50)
	name_conference = models.CharField('Nombre', max_length=200)
	place_conference = models.CharField('Lugar', max_length=100, null=True, blank=True)
	start_conference = models.DateField('Inicia', null=True, blank=True)
	end_conference = models.DateField('Termina', null=True, blank=True)
	deadline_conference = models.DateField('Deadline', null=True, blank=True)
	site_conference = models.URLField('Web Site', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	qualis_cc = models.CharField('Calificación', max_length=2, null=True, blank=True)
	discontinued_conference = models.BooleanField('Conferencia descontinuada', default=False)
	class Meta:
		verbose_name_plural = 'K. Eventos Relacionadas al Instituto'
		ordering = ['id']
	def __str__(self):
		return self.name_conference

class Meeting(models.Model):
	id = models.AutoField(primary_key = True)
	name_meeting = models.CharField('Nombre del evento', max_length=150)
	description_meeting = models.TextField('Descripción', validators=[MaxLengthValidator(1000)])
	date_meeting = models.DateField('Fecha')
	site_meeting = models.URLField('Web Site', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	document_meeting = models.FileField(upload_to='eventos/', 
		null=True, blank=True, help_text='Documento del evento.')
	image_meeting = models.ImageField(upload_to = 'eventos/', default='images/logo.png',
		null=True, blank=True, 
		help_text='Publicidad del evento (jpg, gif, png).')
	past_event = models.BooleanField('Excluir noticia', default=False)
	class Meta:
		verbose_name_plural = 'J. Noticias del Instituto'
		ordering = ['id']
	def __str__(self):
		return self.name_meeting

class Report(models.Model):
	id = models.AutoField(primary_key = True)
	year = models.PositiveIntegerField('Año', validators=[MaxValueValidator(9999)],
		help_text='Escribe el año del reporte.')
	hidden = models.BooleanField(default=False,
		help_text='Ocultar informe año de vista principal.')
	class Meta:
		verbose_name_plural = 'L. Reportes por año'
		ordering = ['id']
	def __str__(self):
		return str(self.year)

# Nuevos Modelos

class Form(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField('Nombre del formulario o documento', max_length=150)
	date = models.DateField('Fecha de subida', blank=True, null=True)
	document = models.FileField(upload_to='documentos/', 
		help_text='Este campo acepta diversos formatos (doc, docx, pdf, xls, ppt, pptx, etc.)')
	hidden = models.BooleanField(default=False,
		help_text='Ocultar formulario o documento.')
	class Meta:
		verbose_name_plural = 'M. Formularios y Documentos'
		ordering = ['id']
	def __str__(self):
		return str(self.name)

class ResearchArea(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField('Área de investigación', max_length=150)
	date = models.DateField('Fecha de creación', blank=True, null=True)
	area_description = models.TextField('Descripción del área', 
		validators=[MaxLengthValidator(1000)], blank=True, null=True)
	area_document = models.FileField('Documento descripción del área', 
		upload_to='areas_investigacion/', blank=True, null=True,
		help_text='Documento describiendo la investigación informativa del Área.')
	area_discontinued = models.BooleanField('Descontinuada', default=False)
	class Meta:
		verbose_name_plural = 'B. Areas de Investigación'
		ordering = ['id']
	def __str__(self):
		return self.name

class ResearchTopics(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField('Línea de investigación', max_length=150)
	area = models.ForeignKey(ResearchArea, on_delete=models.PROTECT, 
		help_text='Seleccione o adicione el Área de Investigación de la Línea de Investigación.')
	date = models.DateField('Fecha de creación', blank=True, null=True)
	topic_description = models.TextField('Descripción de la linea de investigación', 
		validators=[MaxLengthValidator(1000)], blank=True, null=True)
	topic_document = models.FileField('Descripción de la línea', upload_to='lineas_investigacion/',
		blank=True, null=True, 
		help_text='Documento definiendo la línea de investigación.')
	topic_discontinued = models.BooleanField('Descontinuada', default=False)
	index_description = models.TextField('Descripción del index', 
		validators=[MaxLengthValidator(140)], blank=True, null=True)
	index_image = models.ImageField(upload_to = 'lineas_investigacion/', 
		default='images/logo.png',
		help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.')
	index_button = models.CharField('Nombre del botón del index', max_length=30, 
		default='Investigación')
	class Meta:
		verbose_name_plural = 'C. Lineas de Investigación'
		ordering = ['id']
	def __str__(self):
		return self.name

class Position(models.Model):
	id = models.AutoField(primary_key = True)
	name_position = models.CharField('Nombre del Cargo', max_length=150)
	position_description = models.TextField('Descripción del cargo', 
		validators=[MaxLengthValidator(1000)], blank=True, null=True)
	document = models.FileField('Documento del Cargo', upload_to='cargos/', 
		null=True, blank=True, 
		help_text='Descripción del cargo.')
	class Meta:
		verbose_name_plural = 'D. Cargos/Puestos del Instituto'
		ordering = ['id']
	def __str__(self):
		return self.name_position

class People(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField('Nombre',max_length=150,
		help_text='Usa tu nombre completo e.g. Juan José Perez.')
	join_date = models.DateField('Fecha de ingreso al instituto', blank=True, null=True)
	author_name = models.CharField('Nombre de Autor', max_length=50, 
		help_text='Use su nombre de autor como en publicaciones e.g. JJ Perez')
	position = models.ForeignKey(Position, on_delete=models.PROTECT, 
		related_name='position', blank=True, null=True)
	technical_committee = models.BooleanField('Comité/Consejo Técnico', default=False, 
		help_text='Pertenece al Consejo/Comité Técnico')
	executive_committee = models.BooleanField('Comité/Consejo Ejecutivo', default=False, 
		help_text='Pertenece al Consejo/Comité Ejecutivo')
	editor_committee = models.BooleanField('Consejo/Comité Editor', default=False, 
		help_text='Pertenece al Consejo/Comité Editorial')
	scholarship_committee = models.BooleanField('Consejo/Comité de Becas', default=False, 
		help_text='Pertenece al Consejo/Comité de Becas')
	research_topic = models.ForeignKey(ResearchTopics, on_delete=models.PROTECT, 
		related_name='rt_people', blank=True, null=True)
	email = models.EmailField('Email', max_length=100,
		help_text='De preferencia un email institucional.')
	phone = models.CharField('Telefono(s)', max_length=100, null=True, blank=True)
	personal_web = models.URLField('Web personal', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	cv_web = models.URLField('Web de su CV', max_length=250, null=True, blank=True, 
		help_text='Linkdin o otro sitio web donde actualiza constantemente su CV, dirección completa https://')
	curriculo_vitae = models.FileField(upload_to='curriculos_vitae/', 
		null=True, blank=True, 
		help_text='Curriculo vitae del miembro del instituto de investigación.')
	image = models.ImageField(upload_to = 'images/', default='images/logo.png',
		help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.')
	past_member = models.BooleanField('Ex miembro del instituto', default=False)
	hidden_member = models.BooleanField('Ocultar al miembro de reportes y la página Personal', default=False)
	class Meta:
		verbose_name_plural = 'E. Personal del Instituto de Investigación'
		ordering = ['id']
	def __str__(self):
		return self.name

class Service(models.Model):
	id = models.AutoField(primary_key = True)
	name_services = models.CharField('Nombre del servicio', max_length=150)
	research_topic = models.ForeignKey(ResearchTopics, on_delete=models.PROTECT, 
		related_name='rt_service', blank=True, null=True)
	description_service = models.TextField('Descripción del servicio', 
		validators=[MaxLengthValidator(1000)])
	web_service = models.URLField('Sitio web del servicio', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	service_triptych = models.FileField('Tríptico del Servicio', upload_to='services/',
		blank=True, null=True, 
		help_text='Documento definiendo la línea de investigación.')
	image_service = models.ImageField(upload_to = 'services/', default='images/logo.png',
		help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.')
	past_service = models.BooleanField('Descontinuado', default=False)
	class Meta:
		verbose_name_plural = 'G. Servicios Ofrecidos'
		ordering = ['id']
	def __str__(self):
		return self.name_services

class Institute(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField('Nombre del instituto', max_length=150, 
		default=Instituto_de_Investigacion)
	acronym = models.CharField('Sigla del instituto', default=Sigla, max_length=10)
	inauguration = models.DateField('Fecha de inauguración', null=True, blank=True)
	resolution = models.CharField('Resolución', max_length=20, null=True, blank=True)
	faculty = models.CharField('Facultad', default=Facultad, max_length=100, 
		null=True, blank=True)
	career = models.CharField('Carrera', default=Carrera, max_length=100, 
		null=True, blank=True)
	address = models.TextField('Dirección', validators=[MaxLengthValidator(500)],
		help_text='Describa de forma exacta la dirección del Instituto de Investigación.')
	phone = models.CharField('Teléfono(s)', max_length=100, null=True, blank=True)
	fax = models.CharField('Fax', max_length=100, null=True, blank=True)
	pob = models.CharField('Casilla Postal', max_length=100, null=True, blank=True)
	website = models.URLField('Sitio Web del Instituto', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	email = models.EmailField('Email del Instituto', max_length=100,
		help_text='De preferencia email institucional @fcpn.edu.bo.')
	research_area = models.ManyToManyField(ResearchArea, 
		help_text='Seleccione las áreas de investigación del Instituto.')
	class Meta:
		verbose_name_plural = 'A. Instituto de Investigación'
		ordering = ['id']
	def __str__(self):
		return self.name

class Course(models.Model):
	id = models.AutoField(primary_key = True)
	code_course = models.CharField('Código', max_length=10)
	name_course = models.CharField('Curso', max_length=100)
	website_course = models.URLField('Web Site', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	professor_course = models.ForeignKey(People, on_delete=models.PROTECT, blank=True, null=True,
		related_name='professor_course', help_text='Docente del Curso')
	description_course = models.TextField('Descripción', validators=[MaxLengthValidator(1000)], 
		null=True, blank=True)
	prerequisites_course = models.TextField('Pre-requisitos', validators=[MaxLengthValidator(500)], 
		null=True, blank=True)
	course_document = models.FileField('Documento del curso', upload_to='cursos/',
		blank=True, null=True, 
		help_text='Documento describiendo el contenido del curso/publicidad.')
	past_course = models.BooleanField('Descontinuado', default=False)
	class Meta:
		verbose_name_plural = 'I. Cursos del Instituto'
		ordering = ['id']
	def __str__(self):
		return self.name_course

class Project(models.Model):
	id = models.AutoField(primary_key = True)
	acronym = models.CharField('Sigla del Proyecto', max_length=20)
	name = models.CharField('Nombre del Proyecto', max_length=150)
	topic = models.ForeignKey(ResearchTopics, on_delete=models.PROTECT, 
		help_text='Seleccione la Línea de Investigación al cual pertenece.')
	website = models.URLField('Web Site del Proyecto', max_length=250, null=True, blank=True,
		help_text="Escriba la dirección completa incluido http:// o https://")
	project_document = models.FileField('Documento del proyecto', upload_to='proyectos/',
		blank=True, null=True, 
		help_text='Documento del proyecto.')
	description = models.TextField('Descripción', validators=[MaxLengthValidator(1000)],
		null=True, blank=True, 
		help_text='Describir información acerca del proyecto y sus patrocinadores.')
	impact = models.TextField('Impacto', validators=[MaxLengthValidator(1000)],
		null=True, blank=True, 
		help_text='Describir los resultados esperados del proyecto')
	objective = models.TextField('Objetivo(s)', validators=[MaxLengthValidator(1000)],
		null=True, blank=True, 
		help_text='Describir los objetivos del proyecto')
	start = models.DateField('Inicio del Proyecto', null=True, blank=True)
	end = models.DateField('Fin del Proyecto', null=True, blank=True)
	chair = models.ForeignKey(People, on_delete=models.PROTECT, 
		help_text='Seleccione al coordinador del Proyecto.')
	co_chair = models.ManyToManyField(People, related_name='co_chair_project', 
		blank=True, help_text='Lista de co-coordinadores del proyecto.')
	member = models.ManyToManyField(People, related_name='member_project', 
		blank=True, help_text='Lista de miembros del proyecto.')
	collaborator = models.ManyToManyField(People, related_name='collaborator_project', 
		blank=True, help_text='Lista de colaboradores del proyecto.')
	proponent = models.CharField('Unidad Proponente', max_length=100, null=True, blank=True)
	counterpart_unit = models.CharField('Unidad Contraparte', max_length=100, null=True, blank=True)
	co_executing_unit = models.CharField('Unidad(es) Co-Ejecutoras', max_length=100, null=True, blank=True)
	responsible_unit = models.CharField('Unidad Responsable', max_length=100, null=True, blank=True)
	monitor_project = models.CharField('Monitor(es)', max_length=100, null=True, blank=True,
		help_text='Lista de monitores separados por coma.')
	class Meta:
		verbose_name_plural = 'F. Proyectos de Investigación'
		ordering = ['id']
	def __str__(self):
		return self.name

class Award(models.Model):
	id = models.AutoField(primary_key = True)
	award = models.CharField('Premio', max_length=200,
		help_text='Nombre completo del premio o reconocimiento.')
	awarded = models.ManyToManyField(People, related_name='awarded_award', 
		blank=True, help_text='Seleccione a los miembros premiados del Instituto.')
	web_award = models.URLField('Sitio web del premio', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	date = models.DateField('Fecha de la ceremonia de la premiación', 
		null=True, blank=True)
	description_award= models.TextField('Descripción', validators=[MaxLengthValidator(1000)])
	class Meta:
		verbose_name_plural = 'H. Premios del Instituto'
		ordering = ['id']
	def __str__(self):
		return self.award

'''Table Project:
chair = models.ManyToManyField(People, related_name='chair_project', 
	blank=True, help_text='Lista de coordinadores del proyecto.')'''

'''Table Award:
prize = models.ForeignKey(People, on_delete=models.PROTECT, 
	help_text='Seleccione al miembro premiado del Instituto.')'''

class Comment(models.Model):
	id = models.AutoField(primary_key = True)
	name_comment = models.CharField('Nombre', max_length=50)
	email_comment = models.EmailField('E-Mail')
	message_comment = models.TextField('Mensaje', validators=[MaxLengthValidator(500)])
	ip_comment = models.CharField('IP', max_length=40, null=True, blank=True)
	country_name_comment = models.CharField('Pais', max_length=100, null=True, blank=True)
	country_code_comment = models.CharField('Código de Pais', max_length=4, null=True, blank=True)
	class Meta:
		verbose_name_plural = 'M. Comentarios Enviados al Site'
		ordering = ['id']
	def __str__(self):
		return self.name_comment
