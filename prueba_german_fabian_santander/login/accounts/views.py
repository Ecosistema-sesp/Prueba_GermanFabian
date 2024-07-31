from .imports.import_views import *

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.error(request, ('Usuario o contraseña incorrectos'))
    else:
        form = CustomAuthenticationForm()
    form.fields['username'].widget.attrs['value'] = ''
    form.fields['password'].widget.attrs['value'] = ''
    return render(request, 'account/login.html', {'form': form})

def home_view(request):
    db_status = check_database_connection()
    context = {
        'db_status': db_status
    }
    return render(request, 'home.html', context)

@never_cache
@login_required
def welcome_view(request):
    return render(request, 'account/welcome.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@never_cache
def logout_view(request):
    logout(request)
    return redirect('login')
