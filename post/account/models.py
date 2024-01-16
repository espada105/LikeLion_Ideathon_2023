from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # Create your models here.

# class UserManager(BaseUserManager):
#     #일반 user 생성
#     def create_user(self, username,nickname, password=None):
#         if not nickname:
#             raise ValueError('must have user nickname')
#         if not username:
#             raise ValueError('must have user username')
#         user = self.model(
#             nickname = nickname,
#             username = username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     #관리자 user 생성
#     def create_superuser(self, username, nickname, password=None):
#         user = self.create_user(
#             password = password,
#             nickname = nickname,
#             username = username
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)

#     USERNAME_FIELD = 'username' #username으로 로그인
#     REQUIRED_FIELDS = [] #필수로 받고 싶은 필드들 넣기

#     # User 모델의 필수 field
#     is_active = models.BooleanField(default=True)    
#     is_admin = models.BooleanField(default=False)

#     #헬퍼 클래스 
#     objects = UserManager()

#     def __str__(self):
#         return self.nickname
    

#--------------------------------------------나중에
# class CustomUser(AbstractUser):
#     nickname = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nickname


    


