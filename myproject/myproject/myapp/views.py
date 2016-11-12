# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.shortcuts import render_to_response

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            # Redirect to the document list after POST
            return render_to_response("'resource/get_back.html'")
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render(
        request,
        'resource/upload_home.html',
        {'form': form}
    )

