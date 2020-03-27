from setuptools import setup


setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='html2png',
    url='',
    author='Marco Ian',
    author_email='marco.iannell4@gmail.com',
    # Needed to actually package something
    packages=['html2png'],
    # Needed for dependencies
    install_requires=['selenium', 'pyvirtualdisplay'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='Personal',
    description='make png files from html map',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)