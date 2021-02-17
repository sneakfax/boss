from setuptools import setup

setup(
   name='boss',
   version='0.2',
   description='A very simple sms-spammer',
   packages=['boss', 'boss.asyncRequestSender'],  #same as name
   package_dir={'boss': 'src/boss'},
   package_data={'boss': ['data/*.json']},
   include_package_data=True,
   entry_points={'console_scripts': [ 'boss=boss.start:asyncMain']},
   # function to call on $ python my.egg
   py_modules=['boss.start:asyncMain'],
   license="MPL 2.0",
   install_requires=['asyncio', 'aiohttp==3.7.3', "requests", "colorama","urllib3"], #external packages as dependencies
)
