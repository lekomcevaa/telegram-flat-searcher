from setuptools import setup, find_packages

setup(
    name='telegram_flat_searcher',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'telethon',
        'python-dotenv'
    ],
    author='Andrey Lekomtsev',
    author_email='lekomcevaa2000@gmail.com',
    description='Библиотека для чтения сообщений из Telegram и их сохранения в базу данных MySQL/MariaDB.',
classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
        url='https://github.com/andreylekomtsev/telegram-flat-searcher',
        project_urls={
        'Bug Reports': 'https://github.com/andreylekomtsev/telegram-flat-searcher/issues',
        'Source': 'https://github.com/andreylekomtsev/telegram-flat-searcher',
        },
        keywords='telegram, reader, database',
        python_requires='>=3.6',
    )  # Add a comma here