from distutils.core import setup

setup(name='jdommer',
      version='1.1',
      description='snooper the websites',
      author='Pankaj Kumar',
      packages=['jdommer'],
      install_requires=['browsermob-proxy==0.8.0','Flask==1.1.2','psycopg2-binary==2.8.5','waitress==1.4.4'],
      entry_points ={'console_scripts': ['jsdom = snooper.app:runsnooper']}
     )