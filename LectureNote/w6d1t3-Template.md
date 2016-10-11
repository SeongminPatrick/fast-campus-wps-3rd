#Template


### 전체적 그림

```
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}

```

### 변수

{{ variable }}



### for 문

```
{% for k, v in defaultdict.iteritems %}
    Do something with k and v here...
{% endfor %}
```

### Filters

* 소문자로 {{ name|lower }}
* {{ text|escape|linebreaks }}
* {{ list|join:", " }}.
* 글자수 제한 `{{ bio|truncatewords:30 }}`
* 길이 `{{ value|length }}`
* 파일사이즈 `{{ value|filesizeformat }}`


### Template inheritance


block요소로 템플릿을 블럭요소로 관리한다
base.html은 주로 네비게이션 푸터등 자주 쓰이는 부분을 담당
나머지는 내용 content가 작성된다. 즉, base.html은 여러 템플릿에서 호출하여 사용 가능

base.html을 가져다 사용하는 템플릿은 `{% extends 'base.html' %}` 을 상단에 선언해야한다.

타이틀에도 블럭요소를 쓸 수 있는데 타이틀 텍스트를 블럭으로 감싸고 상속받는 list.html 타이틀에도 블럭요소로 감싸면 된다. base.html에 작성된 타이틀은 디폴트 값이고 list.html에 작성된 타이틀은 list페이지 접근시 디폴트 타이틀을 대신한다.

base.html

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="ko">
<body>
  <div class="page-header">
    <h1>
    		<a href="{% url 'blog:post_list' %}">{% block title %} Django Blog {% endblock %}</a>
   	</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        {% block content %}
        {% endblock %}
      </div>
    </div>
  </div>
</body>
</html>
```

list.html

```
{% extends 'base.html' %}

{% block title %} Post-List {% endblock %}

{% block content %}
{% for post in posts %}
  <div class="post">
    <p>published: {{ post.published_date }}</p>
    <h1><a href="{% url 'blog:post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    <p>{{ post.text|linebreaksbr|truncatewords:50 }}</p>
  </div>
{% endfor %}

{% endblock %}
```

### autoescape

The 'escape' filter escapes a string's HTML. Specifically, it makes these replacements:

1. < is converted to &lt;
2. > is converted to &gt;
3. ' (single quote) is converted to &#39;
4. " (double quote) is converted to &quot;
5. & is converted to &amp;

보안을 위해 입력된 str의 일부분을 특수 문자로 변환한다. 안전한 데이터는 꺼도됨


```
{% autoescape on %}
    {{ body }}
{% endautoescape %}
```
