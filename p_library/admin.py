from django.contrib import admin
from p_library.models import Redaction, Book, Author

# 
from p_library.models import Friend, Rent, UserProfile
# 


@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redaction', 'book_img')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass    
 

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    
    @staticmethod
    def friend_name(obj):
        return obj.friend.name

    @staticmethod
    def book_title(obj):
        return obj.book.title

    list_display = ('friend_name', 'book_title', 'num',)