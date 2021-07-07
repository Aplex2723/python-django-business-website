from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ('updated'))

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ('updated'))
    list_display = ('title', 'author', 'published', 'post_categories') #Muestra en la lista los valores establecidos
    ordering = ('author', 'published') # Ordena la lista dependiendo los valores
    search_fields = ('title', 'author__username', 'categories__name') #El cmapo no puede quear como 'author' ya que es un modelo relacionado
    date_hierarchy = 'published' # Gerarquizar los filtros mediante las fechas
    list_filter = ('author__username', 'categories__name') # Creacion de filtros

    #Creando nuevos campos
    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by("name")) 
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)