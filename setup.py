from setuptools import setup
long_description = open('README.rst').read()

setup(
    name='django-bitbucket-hook',
    version='1.0.2',
    packages=['django_bitbucket_hook', 'django_bitbucket_hook.migrations'],
    url='https://github.com/Kras4ooo/django-bitbucket-hook',
    license='Apache License Version 2.0',
    author='Krasimir',
    author_email='krasimir.nikolov1994@gmail.com',
    long_description=long_description,
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='Django module',
    test_suite='tests'
)
