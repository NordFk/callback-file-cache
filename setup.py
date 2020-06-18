from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='cache',
      version='0.1',
      description='Callback file cache',
      long_description=readme(),
      url='http://bitbucket.org/nordfk/callback-file-cache',
      author='Joakim Platbarzdis',
      author_email='joakim.platbarzdis@nordfk.se',
      packages=[
          'cache',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
