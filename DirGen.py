import os


def Test():
    main_dir = ["module_name"]
    common_dir = ["models", "views", "controllers", "static", "data", "demo", "security",
                  "report", "wizard", "test", "i18n", "doc"]

    for dir1 in main_dir:
    #    f = open('__init__.py', 'x')
    #    f = open('__manifest__.py', 'x')
   #     f.close()
#        f.close()
        for dir2 in common_dir:
            try:
                os.makedirs(os.path.join(dir1, dir2))
                os.path.join()
            except OSError:
                pass


Test()
