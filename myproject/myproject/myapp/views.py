# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from text_exact import text_extract
import tempfile
import os
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = request.FILES['docfile']
            tup = tempfile.mkstemp("t.png")  # make a tmp file
            f = os.fdopen(tup[0], 'w')  # open the tmp file for writing
            f.write(newdoc.read())  # write the tmp file
            f.close()
            filepath = tup[1]
            t= text_extract(filepath)
            return render(
                request,
                'text.html',
                {'documents':t,'form': form}
            )
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'index.html',
        {'form': form}
    )
