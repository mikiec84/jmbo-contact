from setuptools import setup, find_packages

setup(
    name='jmbo-contact',
    version='2.0.0',
    description='Jmbo contact form app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt International',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-contact',
    packages = find_packages(),
    install_requires = [
        'django-recaptcha',
        'jmbo>=2.0.0',
    ],
    tests_require = [
        'django-setuptest>=0.1.6',
        'psycopg2',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
