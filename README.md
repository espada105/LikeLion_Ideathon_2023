# 🌴 여름이었다 (It was Summer)

**멋쟁이사자처럼 2023 아이디어톤 프로젝트**

## 📚 프로젝트 소개

*여름이었다*는 여름 추억을 다이어리 형식으로 기록하고 공유할 수 있는 웹 서비스입니다. 사진과 글을 통해 소중한 여름 추억을 아름답게 담아내고, 친구들과 공유하며 소통할 수 있는 플랫폼을 제공합니다.

## 👥 팀원 소개

### 프론트엔드
- **홍성인** - HTML, CSS, JavaScript
- **고보성** - HTML, CSS, JavaScript

### 백엔드
- **전형준** - Python (Django)

## 🛠️ 기술 스택

### 프론트엔드
- HTML5
- CSS3
- JavaScript (ES6+)
- jQuery

### 백엔드
- Python 3.11
- Django Framework
- SQLite

## 📋 주요 기능

- **계정 관리**: 사용자 회원가입 및 로그인
- **일기 작성**: 텍스트 에디터를 통한 일기 작성
- **사진 업로드**: 네컷 프레임 형식의 사진 업로드 및 관리
- **소셜 기능**: 좋아요, 댓글 기능을 통한 소통
- **공유 기능**: SNS(Facebook, Instagram, KakaoTalk)를 통한 일기 공유

## 📱 주요 화면

### 메인 페이지
![메인 페이지](https://github.com/user-attachments/assets/d9c893ad-2f61-45d5-a1d0-c9358ad758d7)
*여름 분위기가 물씬 나는 메인 페이지*

### 로그인 화면
![로그인 화면](https://github.com/user-attachments/assets/63081d5f-e29a-482e-b432-f0796018fb23)
*간편한 로그인 인터페이스*

### 회원가입 화면
![회원가입 화면](https://github.com/user-attachments/assets/d5a361ac-24dd-41bf-b429-01f1283e9de9)
*새로운 사용자를 위한 회원가입 페이지*

### 댓글 페이지
![댓글 페이지](https://github.com/user-attachments/assets/3cf2d97e-e653-4b4e-b02d-e771948f3951)
*다른 사용자와 소통할 수 있는 댓글 기능*

### 프레임 선택
![프레임 선택](https://github.com/user-attachments/assets/7688900a-4e93-4610-8609-eba36297af69)
*다양한 프레임 중 원하는 스타일 선택 가능*

### 사진 업로드
![사진 업로드](https://github.com/user-attachments/assets/cc6cfa97-9263-43fb-9fd6-c253d434cd1f)
*추억이 담긴 사진을 쉽게 업로드*

### 일기 작성
![일기 작성](https://github.com/user-attachments/assets/67856bc5-9649-49d5-b563-c35630479a60)
*자유롭게 일기를 작성할 수 있는 인터페이스*

## 🚀 설치 및 실행 방법

### 요구 사항
- Python 3.11 이상
- pip (Python 패키지 관리자)
- Git

### 설치 과정

1. 저장소 클론하기
```bash
git clone https://github.com/username/LikeLion_Ideathon_2023.git
cd LikeLion_Ideathon_2023
```

2. 가상환경 생성 및 활성화
```bash
python -m venv myvenv
# Windows
myvenv\Scripts\activate
# macOS/Linux
source myvenv/bin/activate
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

5. 개발 서버 실행
```bash
python manage.py runserver
```


