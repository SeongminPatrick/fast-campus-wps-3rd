# Making queries

```
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(blank=True)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    N_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
    
```

### Creating objects

```
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
```

### Saving changes to objects

Given a Blog instance b5 that has already been saved to the database, this example changes its name and updates its record in the database:

```
>>> b5.name = 'New name'
>>> b5.save()
```

### Saving ForeignKey and ManyToManyField fields

```
>>> from blog.models import Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()
```
---

### Retrieving specific objects with filters

`Entry.objects.filter(pub_date__year=2006)`
`__`은 pub_date 속성의 속성을 지칭한다
pub_date 의 year가 2006인 오프젝트를 찾는다

### Chaining filters

한번에  여러번 필터를 걸 수 있다.

```
>>> Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime(2005, 1, 30)
... )
```

`headline__startswith='what'`

> headline이 what으로 시작하는 쿼리는 받는다

`.exclude(pub_date__gte=datetime.date.today()`

> pub_date가 오늘 날짜보다 크거나 같으면 쿼리에서 제외한다.

`.filter(pub_date__gte=datetime(2005, 1, 30)`

> pub_date 값이 2005.1.30 보다 크거나 같은 경우 쿼리에 포함


### Limiting QuerySets

```
>>> Entry.objects.all()[:5]
>>> Entry.objects.all()[5:10]
>>> Entry.objects.order_by('headline')[0]
>>> Entry.objects.order_by('headline')[0:1].get()
```
---

### Field lookups

아래 결과는 동일하다 

```
>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)         # __exact is implied
```
* __iexact 는 대소문자 구분없이 일치 값을 가져온다

```
>>> Blog.objects.get(name__iexact="beatles blog")
```
* __contains 는 해당 단어를 포함하는 값을 필터한다.

* __icontains 는 대소문자 구분없이 해당 단어를 포함하는 값을 필터한다.

```
Entry.objects.get(headline__contains='Lennon')

```

`startswith, endswith`와 `istartswith and iendswith` 관계도 동일하다

### Lookups that span relationships

부모 클래스에서 자식 클래스의 속성을 가져올때

* **자식클래스명의lowercase\_\_자식속성명\_\_특성**

```
>>> Blog.objects.filter(entry__headline__contains='Lennon')
```


#### Spanning multi-valued relationships

**아래 두 개의 필터는 결과에 차이점이 있다.**

첫번째 쿼리는 앤트리중에 헤드라인에 lennon을 포함하고 pub_date가 2008년인 앤트리를 가진 블로그만 뽑아주지만

```
Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
```
아래 두 번째 쿼리는 Blog 클래스에서 headline에 lennon을 포함한 앤드티를 가진 블로그를 뽑아내고 그다음 다시 date__year가 2008이 있는 블로그를 가져온다.

```
Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```
두 가지는 미묘한 차이지만 쿼리 결과물이 다르므로 주의하자.

### Filters can reference fields on the model

Django provides F expressions

F 표현식을 사용하면 해당 클래스에서 원하는 속성을 변수로 가져와 필터 조건에 넣을 수 있다

아래는 n_comment 가 n_pingbacks 보다 값이 큰경우를 불러오고

```
>>> from django.db.models import F
>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
```

아래는 rating이 n_comments + n_pingbacks 보다 작은 경우를 불러온다.

```
>>> Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
```

### The pk lookup shortcut

아래는 다 같은 표현이다

```
>>> Blog.objects.get(id__exact=14) # Explicit form
>>> Blog.objects.get(id=14) # __exact is implied
>>> Blog.objects.get(pk=14) # pk implies id__exact
```

첫번째는 Get blogs entries with id 1, 4 and 7 

```
>>> Blog.objects.filter(pk__in=[1,4,7])
```
두 번째는 id가 14 보다 큰경우만 가져온다

```
>>> Blog.objects.filter(pk__gt=14)
```

### Caching and QuerySets

queryset을 두 번째 요청할때는 캐싱한 결과를 가져와 속도가 빠르다

```
>>> queryset = Entry.objects.all()
>>> print([p.headline for p in queryset]) # Evaluate the query set.
>>> print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
```

같은 결과를 가져올때도 캐싱이 되는 경우와 아닌 경우가 나뉜다. 쿼리의 전체 값을 호출한적이 있다면 그 값은 캐싱되어 재활용 되지만. 전체 결과를 읽은 적이 없다면 캐싱되지 않고 서버에서 계속 호출한다.

아래 결과는 서버에서 계속 값을 호출하고

```
>>> queryset = Entry.objects.all()
>>> print queryset[5] # Queries the database
>>> print queryset[5] # Queries the database again
```

아래는 전체 쿼리를 한번 호출한 적이 있기 때문에 다음번에는 캐싱에서 값을 가져온다.

```
>>> queryset = Entry.objects.all()
>>> [entry for entry in queryset] # Queries the database
>>> print queryset[5] # Uses cache
>>> print queryset[5] # Uses cache
```

### Complex lookups with Q objects

Q 표현식은 필터에 보다 상세한 옵션을 걸 수 있다. 아래를 해석해보면


1. pub_date는 2005,5,2 이거나 
2. 2005,5,6이 아닌 경우 중 
3. question이 Who로 시작하는 쿼리를 뽑아준다.

```
from django.db.models import Q

Poll.objects.filter(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | ~Q(pub_date=date(2005, 5, 6))
)
```

---

### Deleting objects

쿼리 결과를 삭제한다.

```
>>> e.delete()
(1, {'weblog.Entry': 1})
>>> Entry.objects.filter(pub_date__year=2005).delete()
(5, {'webapp.Entry': 5})
```

### Copying model instances

pk를 none으로 초기화하고 다시 저장하면 새로운 pk가 부여된 데이터를 생성한다. 즉 복사기능이다.

```
blog = Blog(name='My blog', tagline='Blogging is easy')
blog.save() # blog.pk == 1

blog.pk = None
blog.save() # blog.pk == 2
```

다대다 관계는 저장방법이 다소 다른데, entry와 author가 다대다 관계이고 0번 entry의 authors를 복사한다고 할때

1. 먼저 기존 엔트리의 작가를 모두 old_authors 변수에 할당하고
2. 엔트리 pk를 초기화한다음에
3. 엔트리를 저장하고 (복사본 생성 but 작가 데이터가 빠진상태이다)
4. 다시 생성된 엔트리에 old_authors를 할당시켜 저장한다.
 
> 왜냐? 다대다 관계는 제 3의 테이블에 관계가 저장되므로 단순하게 복사할 수 없다. 기존 엔트리에서 작가 쿼리를 불러와서 저장해두고 다시 넣어주는 방법으로 복사해야한다.

```
entry = Entry.objects.all()[0] # some previous entry
old_authors = entry.authors.all()
entry.pk = None
entry.save()
entry.authors = old_authors # saves new many2many relations
```
### Updating multiple objects at once

값을 일괄적으로 수정한다.
Update all the headlines with pub_date in 2007.

```
Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
```
Change every Entry so that it belongs to this Blog.

```
>>> b = Blog.objects.get(pk=1)
>>> Entry.objects.all().update(blog=b)
```
#### 역참조

일반적이 역참조 방법이고

```
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all() # Returns all Entry objects related to Blog.
```

related_name 속성을 주면 related_name으로 역참조할 수 있다.

```
blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')

>>> b = Blog.objects.get(id=1)
>>> b.entries.all() # Returns all Entry objects related to Blog.
```
#### remove, clear, delete 비교

요소 하나만 삭제할때 (관계만 끊어짐)
`entry.authors.remove(Author.objects.get(name='Joe'))`

요소 전부 삭제할때 (관계만 끊어짐)
`entry.authors.clear()`

관계도 날라가고 authors도 날라감
`entry.authors.all().delete()`
