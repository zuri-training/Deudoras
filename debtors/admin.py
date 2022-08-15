from django.contrib import admin
from debtors.models import Account,School,Debt,DebtorComments,Debtors,Article,ArticleComments,Dispute,User

# Register your models here.
admin.site.register(Account)
admin.site.register(School)
admin.site.register(Debtors)
admin.site.register(Debt)
admin.site.register(User)
admin.site.register(Dispute)
admin.site.register(Article)
admin.site.register(ArticleComments)
admin.site.register(DebtorComments)