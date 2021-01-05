from django.shortcuts import render

# Create your views here.
import subprocess
from cowsayapp.models import Cowsay
from .forms import CowsayAddForm

def Home_view(request):
    html = "index.html"
    form = CowsayAddForm()
    # print(cowsay.stdout.decode("utf-8"))

    if request.method == 'POST':
        form = CowsayAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cowsay.objects.create(input_text=data['input_text'])
            cowsay = subprocess.run(['cowsay', f'{data["input_text"]}'], capture_output=True)
            clear_form = CowsayAddForm()
            return render(request, html, {'cowsay': cowsay, 'form': clear_form})

    return render(request, html, {'form': form})        


def Most_recent(request):
    html = "recent.html"
    cowsays = Cowsay.objects.all()
    cowsayids = sorted([word.id for word in cowsays], reverse=True)
    return render(request, html, {'cowsays': cowsays, 'cowsayids': cowsayids[:10]})
