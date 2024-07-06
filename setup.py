from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    author='wumao',
    author_email='zhoukyke@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    package=find_packages(),
)