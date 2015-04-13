try:
    # Python3; implicit relative imports aren't allowed, so 'gcm' refers to the
    # top-level package.
    from gcm.gcm import GCM
except ImportError:
    # Python2; 'gcm' refers to the sibling module.
    from gcm import GCM
