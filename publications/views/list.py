__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from publications.models import List, Type, Publication, CustomLink, CustomFile

def list(request, list):
	list = List.objects.filter(list__iexact=list)

	if not list:
		raise Http404

	list = list[0]
	publications = list.publication_set.all()
	publications = publications.order_by('-year', '-month', '-id')

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

		return render_to_response('publications/list.html', {
				'list': list,
				'publications': publications
			}, context_instance=RequestContext(request))
