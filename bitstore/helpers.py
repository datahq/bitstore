import logging


def generate_s3_path(inpath, rel_path, filedata, owner=None, name=None):
    if ('{owner}' in inpath and not owner):
        logging.error('Following format variable is not available: owner')
        raise KeyError
    if ('{name}' in inpath and not name):
        logging.error('Following format variable is not available: name')
        raise KeyError

    # For easier formatting (as filedata has "name" key as well)
    inpath = inpath.replace('{name}', '{dataset_name}')
    format_params = {
        'path': rel_path,
        'dataset_name': name,
        'owner': owner
    }
    format_params.update(filedata)
    try:
        upload_url = inpath.format(**format_params)
    except KeyError as e:
        logging.error('Following format variable is not available: %s' % e)
        raise

    return upload_url
