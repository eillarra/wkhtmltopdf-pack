from setuptools import setup

setup(
    name='wkhtmltopdf-pack',
    version='0.12.2.1',
    url='https://github.com/illarra/wkhtmltopdf-pack',
    author='illarra',
    author_email='team@illarra.com',
    license='MIT',
    scripts=['bin/wkhtmltopdf-pack'],
    description='wkhtmltopdf for Python on Heroku/cloudControl buildpacks',
    long_description=open('README.rst').read(),
    keywords='pdf wkhtmltopdf paas heroku cloudcontrol buildpack',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False
)
