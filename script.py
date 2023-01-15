from pymenu import auto_menu

if __name__ == '__main__':
    auto_menu.exclude_folders += ['assets']
    menu = auto_menu.create_menu_from_directory('scripts')
    menu.add_option('exit', lambda: exit(0))
    menu.show()
