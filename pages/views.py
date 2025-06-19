from django.shortcuts import render, redirect


def set_role(request, role):
    if role in ['Viewer', 'Creator']:
        request.session['role'] = role
    return redirect('homepage')


def homepage(request):
    role = request.session.get('role', 'Viewer')
    return render(request, 'pages/homepage.html', {'role': role})


def about(request):
    role = request.session.get('role', 'Viewer')
    return render(request, 'pages/about.html', {'role': role})