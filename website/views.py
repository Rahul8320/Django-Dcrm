from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# home page.
def home(request):
	# check to see if user is logged in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been Logged In!")
			return redirect('home')
		else:
			messages.error(request, "Error in Logged In. Please check once again.")
			return redirect('home')
	else:
		return render(request, 'home.html', {})

# # login user
# def login_user(request):
# 	pass

# logout user
def logout_user(request):
	pass