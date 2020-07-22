from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})
  
def postnew(request):
    return render(request, 'postnew.html')

def postcreate(request):
    print(request.method)
    if(request.method == 'POST'):
      #<form action="{% url 'postcreate' %}" method="post">
      #hello/templates/postnew.html 파일 메서드 확인
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')


def postedit(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'postedit.html',{'onepost':onepost})

def postupdate(request,post_id):
    editpost=get_object_or_404(Blog,pk=post_id)
    editpost.title=request.POST['title']
    editpost.body=request.POST['body']
    editpost.save()
    return redirect('/detail/'+str(post_id))

def postdelete(request,post_id):
    deletepost=get_object_or_404(Blog,pk=post_id)
    deletepost.delete()
    return redirect('home')


def detail(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id) 
    comments = onepost.blogcomment_set.all()
    return render(request, 'detail.html', {'onepost': onepost, 'comments': comments})

# views.py에 blogcommentcreate 함수 추가

def commentcreate(req, post_id):
    if (req.method == 'POST'):
        post = get_object_or_404(Blog, id=post_id)
        post.blogcomment_set.create(title=req.POST['comment_content'])
    return redirect('/blog/detail/'+str(post_id))