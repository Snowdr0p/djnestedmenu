from django import template
from django.urls import resolve
from ..models import MenuItemContainer
from .utils import find_in_tree, make_tree_menu

register = template.Library()


@register.inclusion_tag('nested_menu/menu.html', takes_context=True)
def draw_menu(context: template.RequestContext, menu_name: str) -> dict:
    """Draws a menu"""
    # fetch all menu layers from db
    menu_items = MenuItemContainer.objects.filter(menu__name=menu_name)

    if not menu_items:
        raise ValueError(f"No such menu with name '{menu_name}'")

    # generate tree menu
    tree_menu = make_tree_menu(menu_items)
    # find names of items that are on the way to target item
    url_name = resolve(context.request.path).url_name
    names_list = find_in_tree(tree_menu, context.request.path[1:], url_name)
    
    return {
        "tree_menu": tree_menu,
        "names_list": names_list,
    }


@register.inclusion_tag('nested_menu/tree.html')
def create_tree_menu(tree_menu: list[MenuItemContainer], names_list: list) -> dict:
    """creates a tree menu"""
    return {
        'tree_menu': tree_menu,
        'names_list': names_list,
    }
