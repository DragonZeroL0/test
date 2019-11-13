
import requests
from bs4 import BeautifulSoup
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
fb = open('XW.txt','a')
res =  requests.get('https://www.chinanews.com/')
res.encoding=('utf-8')
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.xwzxdd-xbt a'):
    fb.write(news.string)
    fb.write('\n')
for news in soup.select('.xwzxdd-dbt a'):
    fb.write(news.string)
    fb.write('\n')
for news in soup.select('._jsxwdiv li a'):
    fb.write(news.string)
    fb.write('\n')
for news in soup.select('.rank_right_ul a'):
    fb.write(news.string)
    fb.write('\n')
#爬虫部分结束，由于整个新闻网页分成了许多模块没找到一个新闻标题统一的特征，故只爬取了网站上的部分数据
fb.close()
Spider_file='XW.txt'
#读取文件内容
word_content=open(Spider_file,'r',encoding='utf-8').read().replace('\n','')#去除掉前面因美观加上的空格、回车
img_file='timg.jpg'#读取背景图片
mask_img=imread(img_file)#进行分词
word_cut=jieba.cut(word_content)#把分词用空格连起来
word_cut_join=" ".join(word_cut)#生成词云
wc=WordCloud(
             font_path='simsun.ttc',#设置字体成为与记事本字体相同的字体，否则会报错
             width=2000,
             height=1400,
             max_words=50,
             scale=2,#与width和height都说可以改变大小，可是我并没有发现有啥区别QAQ
             mask=mask_img,
             background_color='white'
             ).generate(word_cut_join)
plt.imshow(wc)#去掉坐标轴
plt.axis('off')
plt.savefig('homework.jpg')
plt.show()
