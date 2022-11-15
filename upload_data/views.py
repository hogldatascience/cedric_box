from django.shortcuts import render
from . import upl_data

# Create your views here.

def home(request):

    return render(request, "upload_data.html")


def upload_data_ftn(request):

    up_data = request.POST['selected_file_html']

    msg = upl_data.update_db(up_data)

    return render(request, "upload_data.html", {'message': msg})
