# Week5 주말과제

1. pyenv전체삭제
2. pyenv재설치
3. pyenv에 파이썬 3.4.3설치
4. 가상환경생성
5. pip로 장고설치
6. 장고프로젝트생성
7. 파이참으로 프로젝트폴더 열기
8. 해당 프로젝트에 가상환경 인터프리터 세팅

<br>
## 1. pyenv 전체삭제

```
$ rm -rf pyenv
$ rm -rf .pyenv
$ pyenv versions

```

pyenv versions 해봐도 버전이 남아있다?
Finder에서 cmd + shift + G 로 urs/local/var 경로 검색해서 접근하고 pyenv 를 삭제하자

```
pyenv versions  (깨끗하다)

brew remove pyenv

```
<br>
## 2. pyenv 재설치

pyenv 설치하고 zshrc 열기

``` 
$ brew install pyenv
vi zshrc
```

하기 내용 삽입

```
export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

```
<br>
## 3. pyenv에 파이썬 3.4.3설치

가능 리스트 확인

``` 
$ pyenv install --list 

```
설치시작 !!

```
$ pyenv install 3.4.3
.
.
zipimport.ZipImportError: can't decompress data; zlib not available
=> 오류난다

$ xcode-select --install
$ brew install homebrew/dupes/zlib
$ pyenv install 3.4.3
=> 성공
$ pyenv versions
=> 확인
$ python -V
Python 2.7.11
=> 원래 버전
$ pyenv shell 3.5.0
=> 변경
$ python -V
Python 3.5.0

```

<br>
## 4. 가상환경생성

이번엔 python 프로젝트마다 각각의 가상환경을 만들어 줄 수 있는 virtualenv를 설치

```
$ brew install pyenv-virtualenv

```
가상환경 생성

```
$ pyenv virtualenv 3.4.3 prac-firstenv
```
원하는 폴더에 이동해서 가상환경을 설치

```
$ pyenv local prac-firstenv

```
터미널을 껏다가 키면 이제 폴더에 접근하면 자동으로 가상환경이 변경된다.

<br>
## 5. pip로 장고설치

```
$ pip install django
```
<br>
## 6. 장고프로젝트생성
```
$ django-admin startproject mysite

```
project 폴더명 변경해도됨
mysite => mysite-project

```
% mv mysite mysite-project
```

원하는 app 추가

```
% python manage.py startapp polls

```
mysite > settings.py 에서
INSTALLED_APPS 리스트에 polls 추가

<br>
## 7. 파이참으로 프로젝트폴더 열기

pycharm open 에서 생성한 프로젝트 가져오고, mysite-project 파일을 우클릭해서 mark dir as 를 클릭하고, source root 를 클릭한다.
> source root를 설정하면
> BASE_DIR로 지정되어 url참조시 기준이 된다.

<br>
## 8. 해당 프로젝트에 가상환경 인터프리터 세팅

1. pycharm의 preference > project:mysite-project > project interpreter 이동
2. project interpreter 에서 show all 클릭
3. + 클릭 해서 add local 클릭
4. /usr/local/var/pyenv/versions/prac-firstenv/bin/python 경로 선택
