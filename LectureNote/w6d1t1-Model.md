### symmetrical=False

나 자신과의 ManyToMany 관계이다.
Person이 Relationship을 통해 **자기 자신**과의 관계를 가진다.
Person 인스턴스끼리의 관계를 표현할 수 있다.
이때는 `symmetricla=false` 옵션을 사용해야한다. 



```
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_name_to+')

RELATIONSHIP_FOLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)
# 한 클래스 안에서의 관계를 나타낼 수 있다.
class Relationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_person')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

```

### Models across files

자주하던거 다른 app의 model에서 함수 가져오기 많이 하던거
`from geography.models import ZipCode`

```
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,

    )
```    
    
### Meta Option


```
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
```
 
 
`ordering = ["horn_length"]` horn_length 기준으로 오름차순 한다
meta는 그 클래스의 기본값(설정)이다

### manager

objects를 커스터마이징 할 수 있다.

```
from django.db import models

class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.id, p.question, p.poll_date, COUNT(*)
                FROM polls_opinionpoll p, polls_response r
                WHERE p.id = r.poll_id
                GROUP BY p.id, p.question, p.poll_date
                ORDER BY p.poll_date DESC""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list

class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    poll_date = models.DateField()
    objects = PollManager()

class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    response = models.TextField()
```

With this example, you’d use `OpinionPoll.objects.with_counts()` to return that list of OpinionPoll objects with num_responses attributes.


### Overriding predefined model methods

블로그 클래스 커스터마이징
기본으로 제공되는 모델을 커스터마이징 할 수 있다.

```
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    # 세이브 커스터미이징
    def save(self, *args, **kwargs):
        # 세이브 하기전에 엑션하나 부여
        do_something()
        # Call the "real" save() method.
        super(Blog, self).save(*args, **kwargs) 
        do_something_else()
        # 세이브하고 엑션하나 부여
        
```

`super(Blog, self).save(*args, **kwargs)` 기존 세이브 모델을 가져옴 do_something 부분만 커스터마이징 한거임

### Model inheritance

```
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @property
    def pull_name(self):
        return '%s%s' % (self.last_name, self.first_name)


# Person 클래스를 상속받음
class Student(Person):
    year = models.CharField(max_length=20)    
```

Person을 상속받은 Student 클래스는 테이블에 year라는 컬럼만 갖는다
first_name 과 last_name 은 Person에 유지되고 저장되고 수정된다.


```
>>> s1 = Student.objects.create(first_name="병현", last_name="박", year="3")
```

### Abstract base classes

추상 클래스

```
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

이렇게 migrate 하면 student 테이블에 name, age, bome_group 속성이 생긴다.
추상클래스 CommonInfo 테이블은 생성되지 않는다.
>추상클래스가 사용되는 이유는
>자주 사용하는 속성들을 추상클래스에 넣고 여기저기서 상속받아 사용한다.
>추상클래스는 그 자신의 테이블은 필요없기 때문에 테이블을 생서하지 않는다

### Multi-table inheritance

```
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

자식은 자연스럽게 부모의 속성을 사용할 수 있다

```
>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")
```
부모는 자식의 속성을 사용하기위해 `p.restaurant` 처럼 별도 명령이 필요하다

1. 특정 인스턴스를 가져오고
2. 가져온 인스턴스에 클래스명의 lower_case 로 접근해서 추출한다.

```
>>> p = Place.objects.get(id=12)
>>> p.restaurant.serves_hot_dogs
```

>tip. shell에서 p1의 속성으 모두 확인하기

```
for i in dir(p1):
 print(i)
```

### Proxy model

프록시는 테이블은 만들지 않고 기존 다른 테이블의 오더링만 해서 (재가공해서) 추출만 해준다.

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True
        ordering=('-year')

    def do_something(self):
        # ...
        pass
```

### Multiple inheritance

```
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...

class BookReview(Book, Article):
    pass
    
```

하나의 클래스가 여러개의 상속을 받을 수 있다.