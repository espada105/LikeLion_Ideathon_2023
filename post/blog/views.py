from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostsForm
# Create your views here.
def upload(request):
    user = request.user
    return render(request, 'upload.html',{'user':user})

def insert1(request):
    if request.method =='POST':
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        image4 = request.FILES['image4']
        body = request.POST['body'] #post 객체의 title에 폼에 작성한 title을 저장
        author = request.user
        posts = Post(
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image4 = image4,
            body = body,
            author = author,
        )
        posts.save() #post를 저장(데이터베이스에 저장한다)
        return redirect('main') #저장을 하였으면 url name이 'home'인 곳으로 리다이렉트
    else:
        postform = PostsForm
        posts = Post.objects.all()
        context = {
            'postform': postform,
            'posts':posts
        }
        return render(request, 'writing22.html',context) #폼이 유효하지 않았다면 url name이 'write'인 곳으로 리다이렉트

def insert2(request):
    if request.method =='POST':
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        image4 = request.FILES['image4']
        body = request.POST['body'] #post 객체의 title에 폼에 작성한 title을 저장
        author = request.user
        posts = Post(
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image4 = image4,
            body = body,
            author = author,
        )
        posts.save() #post를 저장(데이터베이스에 저장한다)
        return redirect('main') #저장을 하였으면 url name이 'home'인 곳으로 리다이렉트
    else:
        postform = PostsForm
        posts = Post.objects.all()
        context = {
            'postform': postform,
            'posts':posts
        }
        return render(request, 'writing33.html',context) #폼이 유효하지 않았다면 url name이 'write'인 곳으로 리다이렉트


def comment(request):
    return render(request, 'commentpage.html')

def blog_detail(request, posts_id):
    posts = get_object_or_404(Post,pk=posts_id)
    return render(request,'blog_detail.html',{'posts':posts})


def edit(request, pk):
    posts = Post.objects.get(pk=pk)
    if request.method =='GET':
        form = PostsForm(instance=posts)
        return render(request, 'post_write.html', {'form':form})

def delete(request,pk):
    posts = Post.objects.get(pk=pk)
    posts.delete()
    return redirect('main')


# def detail(request,post_id):
#   post_detail = get_object_or_404(Post,pk=post_id)
#   comments = Comment.objects.filter(post = post_id)
#   if request.method == "POST":
#     comment = Comment()
#     comment.post = post_detail
#     comment.body = request.POST['']
#     comment.save()
#   return render(request,'detail.html',{'post':post_detail, 'comments':comments})