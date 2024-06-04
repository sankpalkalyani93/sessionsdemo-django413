from django.shortcuts import render, redirect 

# Create your views here.
def set_session(request):
    request.session['username'] = 'kalyani sankpal'
    return redirect('get_session')

def get_session(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'session.html', {'username': username})