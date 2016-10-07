# -*- coding: utf-8 -*-

__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from collections import defaultdict
from django.shortcuts import render_to_response
from django.template import RequestContext
from publications.models import Type, Publication, CustomLink, CustomFile
from string import capwords

def person(request, name):
	author = capwords(name.replace('+', ' '))
	author = author.replace(' Von ', ' von ').replace(' Van ', ' van ')
	author = author.replace(' Der ', ' der ')

	# take care of dashes
	off = author.find('-')
	while off > 0:
		off += 1
		if off <= len(author):
			author = author[:off] + author[off].upper() + author[off + 1:]
		off = author.find('-', off)

	# split into forename, middlenames and surname
	names = name.replace(' ', '+').split('+')

	# construct a liberal query
	surname = names[-1]
	surname = surname.replace(u'ä', u'%%')
	surname = surname.replace(u'ae', u'%%')
	surname = surname.replace(u'ö', u'%%')
	surname = surname.replace(u'oe', u'%%')
	surname = surname.replace(u'ü', u'%%')
	surname = surname.replace(u'ue', u'%%')
	surname = surname.replace(u'ß', u'%%')
	surname = surname.replace(u'ss', u'%%')

	query_str = u'SELECT * FROM {table} ' \
		'WHERE lower({table}.authors) LIKE lower(\'%%{surname}%%\') ' \
		'ORDER BY {table}.year DESC, {table}.month DESC, {table}.id DESC'
	query = Publication.objects.raw(
		query_str.format(table=Publication._meta.db_table, surname=surname))

	# find publications of this author
	publications = []
	publications_by_type = defaultdict(lambda: [])

	# further filter results
	if len(names) > 1:
		name_simple = Publication.simplify_name(names[0][0] + '. ' + names[-1])
		for publication in query:
			if name_simple in publication.authors_list_simple:
				publications.append(publication)
				publications_by_type[publication.type_id].append(publication)

	elif len(names) > 0:
		for publication in query:
			if Publication.simplify_name(names[-1].lower()) in publication.authors_list_simple:
				publications.append(publication)
				publications_by_type[publication.type_id].append(publication)

	# attach publications to types
	types = Type.objects.filter(id__in=publications_by_type.keys())
	for t in types:
		t.publications = publications_by_type[t.id]

	if 'ascii' in request.GET:
		return render_to_response('publications/publications.txt', {
				'publications': publications
			}, context_instance=RequestContext(request), content_type='text/plain; charset=UTF-8')

	elif 'bibtex' in request.GET:
		return render_to_response('publications/publications.bib', {
				'publications': publications
			}, context_instance=RequestContext(request), content_type='text/x-bibtex; charset=UTF-8')

	elif 'mods' in request.GET:
		return render_to_response('publications/publications.mods', {
				'publications': publications
			}, context_instance=RequestContext(request), content_type='application/xml; charset=UTF-8')

	elif 'rss' in request.GET:
		return render_to_response('publications/publications.rss', {
				'url': 'http://' + request.META['HTTP_HOST'] + request.path,
				'author': author,
				'publications': publications
			}, context_instance=RequestContext(request), content_type='application/rss+xml; charset=UTF-8')

	else:
		customlinks = CustomLink.objects.filter(publication__in=publications)
		customfiles = CustomFile.objects.filter(publication__in=publications)

		publications_ = {}
		for publication in publications:
			publication.links = []
			publication.files = []
			publications_[publication.id] = publication

		for link in customlinks:
			publications_[link.publication_id].links.append(link)
		for file in customfiles:
			publications_[file.publication_id].files.append(file)

		return render_to_response('publications/person.html', {
				'publications': publications,
				'types': types,
				'author': author
			}, context_instance=RequestContext(request))
