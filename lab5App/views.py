from django.shortcuts import render ,redirect

# Create your views here.

people  = []

class People:
    def __init__(self, username , password):
        self.username = username
        self.password = password



def display(request):
    return render(request, 'display_people.html',{'people': people })


def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        personNew = People(username=username, password=password)
        people .append(personNew)
        return redirect(display)
    return render(request , 'add_person.html')