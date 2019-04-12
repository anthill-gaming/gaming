#!/usr/bin/env python3
from anthill.framework.core.exceptions import ImproperlyConfigured
from anthill.framework.core.management import Manager
import importlib
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault("ANTHILL_SETTINGS_MODULE", "settings")

    try:
        app_name = sys.argv[2] if sys.argv[1] == 'app' else ''
        app_mod = importlib.import_module(app_name)
    except (IndexError, ImportError, ValueError):
        pass
    else:
        sys.path.insert(0, app_mod.__path__[0])
        os.chdir(app_mod.__path__[0])

    try:
        import anthill.framework
        anthill.framework.setup()
    except (ImportError, ImproperlyConfigured):
        app = None
    else:
        from anthill.framework.apps import app
        del sys.argv[1:3]

    kwargs = dict(app=app)

    if app is None:
        from anthill.platform.management.commands import StartApplication
        try:
            conf = importlib.import_module('conf')
            kwargs.update(root_templates_mod=conf.ROOT_TEMPLATES_MODULE)
            kwargs.update(extra_commands={
                'startapp': StartApplication(
                    root_templates_mod=conf.ROOT_TEMPLATES_MODULE,
                    ui_static_path=conf.ADMIN_STATIC_PATH,
                    ui_template_path=conf.ADMIN_TEMPLATE_PATH,
                    services_registry_file=conf.SERVICES_REGISTRY_FILE
                )
            })
        except (ImportError, AttributeError):
            pass

    manager = Manager(**kwargs)
    manager.run()
