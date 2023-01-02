from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version='0.3.5'
setup(
    name = 'jupyter-edigraf-proxy',
    version = version,
    packages = find_packages(),

    url = 'https://github.com/sebastiendfortier/jupyter-edigraf-proxy',
    download_url = 'https://github.com/sebastiendfortier/jupyter-edigraf-proxy/archive/v{0}.tar.gz'.format(version),

    author = 'Sebastien Fortier',
    author_email = 'sebastiendfortier@gmail.com',

    description = 'Edigraf for JupyterLab',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    keywords = ['jupyter', 'xpra', 'jupyterhub', 'jupyter-server-proxy'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
    ],

    entry_points = {
        'jupyter_serverproxy_servers': [
            'edigraf = jupyter_edigraf_proxy:setup_edigraf',
        ]
    },
    python_requires = '>=3.6',
    install_requires = ['jupyter-server-proxy>=3.1.0'],
    include_package_data = True,
    zip_safe = False
)
