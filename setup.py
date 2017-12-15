from setuptools import setup

setup(
    name='wkhtmltopdf-pack',
    version='0.12.3.0.post1',
    url='https://github.com/illarra/wkhtmltopdf-pack',
    author='illarra',
    author_email='team@illarra.com',
    license='MIT',
    data_files=[('bin', ['bin/wkhtmltopdf-pack'])],
    description='wkhtmltopdf 0.12.3.0 for Python on Heroku buildpacks',
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
