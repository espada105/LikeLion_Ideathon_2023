from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from blog.models import Post
# from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mypage')
        else:
            return render(request, 'login.html',{'error':'아이디나 비밀번호 잘못 입력!'})
    else:
        return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('main')

def mypage(request):
    posts = Post.objects.filter(author=request.user).order_by('pk')
    return render(request, 'mypage1.html',{'posts':posts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 게시글 목록 페이지
            return redirect('mypage')
        return redirect('signup')
    else:
        form = UserCreationForm()
    
    return render(request, 'join.html',  {'form': form})

def blog_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'blog_detail.html',{'posts':posts})

#이건 나중에 설명할게
# def signup(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # 로그인
#             messages.success(request, '회원가입이 완료되었습니다.')
#             return redirect('main')
#         else:
#             messages.error(request, '입력한 정보에 오류가 있습니다. 다시 시도해주세요.')  # 오류 메시지 추가

#     else:
#         form = UserForm()
#     return render(request, 'join.html', {'form': form})
