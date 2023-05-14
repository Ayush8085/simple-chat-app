from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import SignupForm, MessageForm

# Create your views here.

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is invalid!!')
    
    context = {}
    return render(request, 'login.html', context)

def registerUser(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'New User Created')
                return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')

@login_required
def home(request):
    user = request.user

    allMessages = user.messages.all()
    unseenMessages = allMessages.filter(seen=False).count()

    sentMessages = user.sent_messages.all()

    context = {'allMessages': allMessages, 'unseenMessages': unseenMessages, 'sentMessages': sentMessages}
    return render(request, 'home.html', context)

@login_required
def viewMessage(request, pk):
    user = request.user

    message = user.messages.get(id=pk)

    if message.seen == False:
        message.seen = True
        message.save()

    context = {'message': message}
    return render(request, 'message.html', context)

@login_required
def createMessage(request):
    form = MessageForm()

    if request.method == 'POST':
        sender = request.user
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender

            message.save()
            messages.success(request, 'Message sent successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'create-message.html', context)