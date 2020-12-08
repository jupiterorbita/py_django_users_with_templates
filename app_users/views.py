from django.shortcuts import redirect, render
from .models import User

def index(request):
  print('\n----------- index ----------')
  context = {
    'all_users': User.objects.all()
  }
  return render(request, 'index.html', context)

def process_form(request):
  print('\n-------- process_form -------')
  if request.method == "POST":
    print(request.POST)
    post_fname = request.POST['first_name']
    post_lname = request.POST['last_name']
    post_email = request.POST['email']
    post_age = int(request.POST['age'])
    
    print(f'\n == POST data ==\n {post_fname}, {post_lname}, {post_email}, {post_age}')
    
    # add them to the db
    User.objects.create(first_name=post_fname, last_name=post_lname, email=post_email, age=post_age)
    
  return redirect('/')
