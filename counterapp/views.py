from django.shortcuts import render, HttpResponse, redirect 
def index(request):
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
    
    
        'num_visits': num_visits,
    }
         
    return render(request,'index.html',context)

def destroy_session(request):
    del request.session['num_visits']
    return redirect("/")