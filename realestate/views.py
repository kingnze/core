from django.shortcuts import get_object_or_404, render,redirect
from .models import Properties,Top_properties,Blog,Contact,Whoweare,Allinone,whyus,About,Start
from realestate.choices import price_choices, state_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from realtors.models import Realtor
from django.contrib import messages

def index(request):
    myproperties = Properties.objects.order_by('-date').filter(published=True)[:6]
    top_properties = Top_properties.objects.order_by('-date').filter(published=True)[:6]
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:3]
    whoweare = Whoweare.objects.order_by('-date').filter(published=True)[:3]
    allinone = Allinone.objects.order_by('-date').filter(published=True)[:1]
    start = Start.objects.all()
    context= {
        'myproperties': myproperties,
        'top_properties': top_properties,
        'blog': blog,
        'allinone': allinone,
        'whoweare': whoweare,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'start': start


    }
    return render(request,'realestate/index.html',context)  

def myproperties(request):
    myproperties = Properties.objects.order_by('-date').filter(published=True)
    realtors = Realtor.objects.order_by('-hire_date')[:1]

    paginator = Paginator(myproperties, 15)
    page = request.GET.get('page')
    paged_myproperties = paginator.get_page(page)
    
    context = {
        'myproperties': paged_myproperties,
        'realtors': realtors
    }
    return render(request,'realestate/myproperties.html',context)  

def myproperty(request, myproperty_id):
    myproperty = get_object_or_404(Properties, pk=myproperty_id)
    realtors = Realtor.objects.order_by('-hire_date')[:4]
    top_properties = Top_properties.objects.order_by('-date').filter(published=True)[:6]
    
    context = {
        'myproperty': myproperty,
        'realtors': realtors,
        'top_properties': top_properties,
    }
    return render(request,'realestate/myproperty.html',context)  
 
def blog(request):
    blog = Blog.objects.order_by('-date_posted').filter(published=True)
    realtors = Realtor.objects.order_by('-hire_date')[:1]

    paginator = Paginator(blog, 15)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog,
        'realtors': realtors
    }
    return render(request,'realestate/blog.html',context)  

def blogdetail(request, slug_id):
    blogdetail = Blog.objects.filter(slug=slug_id).first()
    top_properties = Top_properties.objects.order_by('-date').filter(published=True)[:9]
    
    context = {
        'post': blogdetail,
        'top_properties': top_properties,
    }
    return render(request,'realestate/blogdetail.html',context)  

def realtors(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)  
    paginator = Paginator(realtors, 12)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)  
    context = {
        'realtors': paged_realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request,'realestate/realtors.html',context)  

def about(request):
    Whyus = whyus.objects.all()
    about = About.objects.all()
    start = Start.objects.all()
    realtors = Realtor.objects.order_by('-hire_date')
    allinone = Allinone.objects.order_by('-date').filter(published=True)[:1]
    context= {
        'realtors': realtors,
        'whyus': Whyus,
        'about' : about,
        'allinone': allinone,
        'start': start
    }
    return render(request,'realestate/about.html',context)   

def search(request):
    queryset_list = Top_properties.objects.order_by('-date')
    realtors = Realtor.objects.order_by('-hire_date')

    if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                queryset_list = queryset_list.filter(description__icontains=keyword)

    context = {
        'myproperties': queryset_list,
        'realtors': realtors,
        'values': request.GET
    }

    return render(request,'realestate/search.html',context) 

def contact(request):   
    if request.method == 'POST':
    
      try:
          connect = Contact(fname=request.POST['fname'],lname=request.POST['lname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

    return render(request,'realestate/contact.html')     

def whoweare(request):
    whoweare = Whoweare.objects.order_by('-date').filter(published=True)

    paginator = Paginator(whoweare, 12)
    page = request.GET.get('page')
    paged_whoweare = paginator.get_page(page)
    
    context = {
        'whoweare': paged_whoweare,
    }

    return render(request,'realestate/whoweare.html',context)

def whowearedetail(request, slug_id):
    whowearedetail = Whoweare.objects.filter(slug=slug_id).first()
    top_properties = Top_properties.objects.order_by('-date').filter(published=True)[:9]
    
    context = {
        'post': whowearedetail,
        'top_properties': top_properties,
    }

    return render(request,'realestate/whowearedetail.html',context)  

def allinone(request):
    allinone = Allinone.objects.order_by('-date').filter(published=True)

    paginator = Paginator(allinone, 12)
    page = request.GET.get('page')
    paged_allinone = paginator.get_page(page)
    
    context = {
        'allinone': paged_allinone,
    }

    return render(request,'realestate/allinone.html',context)  

# def search(request):
#     keyword = request.GET['keyword']
#     result = Properties.objects.filter(description__icontains = keyword)
    
#     context = {
#         'results':result,
#     }
#     return render(request,'realestate/search.html',context)
