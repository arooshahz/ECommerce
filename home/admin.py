from django.contrib import admin
from .models import Category, Product, Feature

from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    group_fieldsets = True

    list_display = ("name",)

    class Media:
        js = (
            'https://code.jquery.com/jquery-1.12.4.min.js',

            'https://code.jquery.com/ui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Feature)
class FeatureAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("name",)

    class Media:
        js = (
            'https://code.jquery.com/jquery-1.12.4.min.js',

            'https://code.jquery.com/ui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    # group_fieldsets = True

    list_display = ("slug",)

    class Media:
        js = (
            'https://code.jquery.com/jquery-1.12.4.min.js',

            'https://code.jquery.com/ui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
