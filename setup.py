from setuptools import setup, find_packages


setup(
    app=['__main__.py'],
    options={
        'p2app': {
            'iconfile': './clean.icns',
            'includes': 'sortfiles',
            'packages': 'sortfiles',
            'argv_emulation': True
        }
    },
    name='DirectoryCleaner',
    version='1.0',
    install_requires=[
        'sortfiles'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
