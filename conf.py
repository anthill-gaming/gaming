import os
import importlib

_conf = None


def settings(name):
    os.environ["ANTHILL_SETTINGS_MODULE"] = "%s.settings" % name
    try:
        import anthill.framework
    except ImportError:
        raise ImportError(
            "Couldn't import anthill framework. Are you sure it's installed "
            "and available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?")
    else:
        global _conf
        if _conf is None:
            _conf = importlib.import_module('anthill.framework.conf')
        else:
            importlib.reload(_conf)
        return _conf.settings


ROOT_TEMPLATES_MODULE = 'anthill.platform.conf'
ADMIN_STATIC_PATH = settings('admin').STATIC_PATH
ADMIN_TEMPLATE_PATH = settings('admin').TEMPLATE_PATH
SERVICES_REGISTRY_FILE = settings('discovery').REGISTERED_SERVICES
