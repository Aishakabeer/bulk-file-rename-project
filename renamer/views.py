import os
import re
from django.shortcuts import render
from .forms import RenameForm

def rename_files(request):
    result = []
    if request.method == 'POST':
        form = RenameForm(request.POST)
        files = request.FILES.getlist('folder')
        if form.is_valid() and files:
            regex = form.cleaned_data['regex']
            prefix = form.cleaned_data['prefix']
            count = 1
            for f in files:
                filename = f.name.split('/')[-1]
                if re.match(regex, filename):
                    ext = os.path.splitext(filename)[1]
                    new_name = f"{prefix}_{count:03d}{ext}"
                    save_dir = os.path.join('uploaded', 'renamed')
                    os.makedirs(save_dir, exist_ok=True)
                    with open(os.path.join(save_dir, new_name), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                    result.append(f"{filename} → {new_name}")
                    count += 1
    else:
        form = RenameForm()
    return render(request, 'renamer/rename.html', {'form': form, 'result': result})
