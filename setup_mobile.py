from setuptools import setup

setup(
   name='boss',
   version='0.2 mobile',
   description='A very simple sms-spammer',
   packages=['boss', 'boss.requestSender'],  #same as name
   package_dir={'boss': 'src/boss'},
   package_data={'boss': ['data/*.json']},
   include_package_data=True,
   entry_points={'console_scripts': [ 'boss=boss.start:main']},
   # function to call on $ python my.egg
   py_modules=['boss.start:main'],
   license="MPL 2.0",
   install_requires=[ "requests", "colorama","urllib3"], #external packages as dependencies
)
