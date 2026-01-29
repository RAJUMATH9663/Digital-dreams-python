from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course = request.POST.get('course')
        return render(request, 'result.html', {
            'name': name,
            'course': course
        })
    return render(request, 'home.html')