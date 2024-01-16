from setuptools import setup

setup(
    name='Videocreate-projem',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Sukru',
    author_email='',
    description=''
    packages=find_packages(),
    package_data={'': ['*.yaml', '*.json']},    # This will include all yaml files in package

    install_requires=[
        'ffmpeg', 
        'python-dotenv', 
        'openai', 
        'opencv-python',
        'elevenlabs',
        'pydub',
        'numpy',
    ],

keywords=['python', 'video', 'content creation', 'AI', 'automation', 'editing', 'voiceover synthesis', 'video captions', 'asset sourcing', 'tinyDB'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)
