# Youtube-Comments-Scrapy
Using google-api-python-client to scrapy specified youtube video.
e:comments and replies

## **爬虫油管指定视频的评论回复**。

国内用户需要代理，通过

```python
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10024'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10024'
```

修改为自己代理的接口就行。
## 安装环境

```python
pip install google-api-python-client
```

## 代码需要配置俩个变量：

## 设置api_key：

参考https://developers.google.com/youtube/v3/getting-started

## 设置video_id:
如：https://www.youtube.com/watch?v=wUoP_PXtOso

```python
video_id=wUoP_PXtOso
```
