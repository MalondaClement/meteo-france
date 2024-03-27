from setuptools import setup, find_packages

setup(
    name='meteo-france',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'python-dotenv>=0.18.0'
        'aiohttp==3.9.1'
        # Add any other dependencies your package requires
    ],
    # entry_points={
    #     'console_scripts': [
    #         'meteo-france-cli=meteo_france.commands:main'
    #         # Add any command-line scripts you want to install
    #     ],
    # },
    author='Clément Malonda',
    author_email='email@email.com',
    description='A Python package for interacting with Meteo France API',
    license='MIT',
    keywords='meteo france weather api',
    url='https://github.com/MalondaClement/meteo-france',  # URL to your package's repository
    project_urls={
        'Bug Tracker': 'https://github.com/MalondaClement/meteo-france/issues',
        'Source Code': 'https://github.com/MalondaClement/meteo-france',
    },
)
