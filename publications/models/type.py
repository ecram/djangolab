__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.db import models
from publications.models.orderedmodel import OrderedModel

class Type(OrderedModel):
	class Meta:
		ordering = ('order',)
		app_label = 'publications'
		verbose_name_plural = '  Types'

	type = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	bibtex_types = models.CharField(max_length=256, default='article',
			verbose_name='BibTex types',
			help_text='Possible BibTex types, separated by comma.')
	hidden = models.BooleanField(default=False,
		help_text='Hide publications from main view.')

	def __unicode__(self):
		return self.type


	def __init__(self, *args, **kwargs):
		OrderedModel.__init__(self, *args, **kwargs)

		self.bibtex_types = self.bibtex_types.replace('@', '')
		self.bibtex_types = self.bibtex_types.replace(';', ',')
		self.bibtex_types = self.bibtex_types.replace('and', ',')
		self.bibtex_type_list = [s.strip().lower()
			for s in self.bibtex_types.split(',')]
		self.bibtex_types = ', '.join(self.bibtex_type_list)
		self.bibtex_type = self.bibtex_type_list[0]
