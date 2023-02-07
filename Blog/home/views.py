from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth import logout

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)

def add_blog(request):
    context = {'form' : BlogForm}

    try:
        if request.method == 'POST':
            form  = BlogForm(request.POST)
            title = request.POST.get('title')
            image = request.FILES.get('image', ' ')
            user = request.user
        
        if form.is_valid() : 
            content = form.cleaned_data['content']
        
        blog_obj = BlogModel.objects.create(
            user = user, title = title,
            content = content, image= image
        )
        print(blog_obj)
        return redirect('/addblog/')

    except Exception as e:
        print(e)


    return render(request, 'add_blog.html', context)

def delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/seeblog/')

def update(request, slug):
    context = {}

    try:
        blog_obj = BlogModel.objects.get(slug = slug)
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content' : blog_obj.content}
        form = BlogForm(instance=blog_obj)
        if request.method == 'POST':
            form  = BlogForm(request.POST)
            title = request.POST.get('title')
            image = request.FILES.get('image', ' ')
            user = request.user
        
            if form.is_valid() : 
                content = form.cleaned_data['content']
        
            blog_obj = BlogModel.objects.create(
            user = user, title = title,
            content = content, image= image
        )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'update.html', context)
        
def logout_view(request):
    logout(request)
    return redirect('/')






# Create your views here.
