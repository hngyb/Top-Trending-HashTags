from setuptools import setup, find_packages

setup(
    name='Top-Trending-HashTags',
    version='0.0.1',
    description='Twitter Streaming API, Kafka, Spark를 활용한 실시간 Top Trend HashTag 분석',
    author='Hongyeob, Gyubok',
    author_email='hngyb2585@gmail.com',
    url='https://github.com/hngyb/Top-Trending-HashTags',
    packages=find_packages(exclude=())
)