from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .forms import CreatePollForm 
from .models import Poll
from django.core.paginator import Paginator

def home(request):
    polls = Poll.objects.all()
    paginator = Paginator(polls, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'polls': polls,'page_obj':page_obj}
    return render(request,'poll/home.html',context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request,'poll/create.html',context)
    

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST['poll']
        
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()
        
        return redirect('results', poll.id)
        
    context = {'poll': poll}
    return render(request,'poll/vote.html',context)    

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll':poll}
    return render(request,'poll/results.html',context)

def delete_con(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == "POST":
            poll.delete()
            return redirect('home')
    else:  
        context = {'poll':poll}
    
    return render(request,'poll/confirm_delete.html',context)
    
    
    
