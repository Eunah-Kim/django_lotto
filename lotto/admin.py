from django.contrib import admin
from .models import GuessNumbers
# from lotto.models import GuessNumbers
# admin.py가 lotto에 속해있음. 속해있는 폴더의 경우 .models로 쓸 수 있음 (밝혀서 써도 무방)

# Register your models here.
admin.site.register(GuessNumbers)
