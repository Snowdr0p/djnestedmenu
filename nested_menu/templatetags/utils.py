"""utils for menu extras"""
from ..models import MenuItemContainer


def make_tree_menu(menu_items: list[MenuItemContainer]) -> dict:
    """Makes a tree menu as a dict"""
    # create dict with menu items dependencies
    items_with_keys = {}
    for menu_item in menu_items:
        if menu_item.parent_item_id in items_with_keys.keys():
            items_with_keys[menu_item.parent_item_id].append(menu_item)
        else:
            items_with_keys[menu_item.parent_item_id] = [menu_item]
    
    # check if there are layer with items without parent items
    if None not in items_with_keys.keys():
        raise ValueError("No root menu items (all menu items have parents.")
    
    def create_recursive_tree(key):
        """creates dict with menu"""
        # get current_layer
        layer = items_with_keys.get(key, None)

        if layer is None:
            return None
        
        # create tree
        tree_layer = {}
        for menu_item in layer:
            tree_layer[menu_item] = create_recursive_tree(menu_item.pk)

        return tree_layer
    
    return create_recursive_tree(None)


def find_in_tree(menu_tree: dict, url: str|None=None, url_name: str|None=None, names_list: list=[]) -> list:
    """returns a list of names of menu items that are on the way to item with url"""
    # search for the menu item with specified url
    if menu_tree is None:
        return []

    new_names = names_list.copy()
    for menu_item in menu_tree.keys():
        if menu_item.url == url or (menu_item.url_name is not None and menu_item.url_name == url_name):
            new_names.append(menu_item.name)
            return new_names
        names_in_item = find_in_tree(menu_tree[menu_item], url, url_name, new_names + [menu_item.name])
        if names_in_item:
            return names_in_item
    
    return []
