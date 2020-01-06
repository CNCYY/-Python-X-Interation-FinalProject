# Python X Interation FinalProject

##### README:中文

#### 一.项目名及介绍：
本项目名称为《中国各省单身率与经济发展、男女比例、教育水平的关系》， 人口发展趋势一直都是现代经济决定性因素。人作为社会的主体，对国家的经济甚至是国家综合实力都有重大的影响。根据《中国统计年鉴2018》数据显示，中国的单身人口已经达到了2.49亿，是总人口的18%，相当于英国、法国和德国人口的总和。**我们这个项目旨在探讨为何中国的单身率越来越高，是否跟经济发展水平、男女比例不平衡和教育水平有关？**

#### 二.项目语言及使用的软件
本项目主要两部分构成，一是由17级提供的交互图，二则是由18级用python制作的flask项目。包含了HTML，CSS，JS语言，使用了pycharm搭建flask以及搭建了web前端。

#### 三.项目内容
本项目包括了四个内容。

一是中国从16-18年的单身人口总数，二是全中国男女人口数，三是16-18年中国各省的GDP的状况，四是中国六岁级以上大专以上学历水平状况，使用了地图，折线图，条形图，饼图。

#### 四技术文档说明
##### HTML文档
- 在python中包含了八个html文档，一个aap.py，八个html文档中有一个是基础页面（base.html），一个主页面(tntry.html)，以及六个跳转页面。五个为交互图+表格，一个为GDP+，目的是为了查看经济发达大城市的单身率，以及是否在经济发达的大城市中女性比男性更容易单身。

##### WEB动作描述
- 在首页中，即（entry.hteml）中，我们运用了两种方式进行页面跳转。
  - 一种是利用筛选按钮，筛选点击你想要了解的数据，进行页面跳转。
  ```
        <div id="wrapper">
  <div id="slider-wrap">
             <ul id="slider">
               <li >
                 <a href="/total_people" type='submit'><img class="i" src="static/entry/img/全国男女人口数对比.png" /></a>
               </li>
               <li>
                  <a href="/GDP" type="submit"><img class="i" src="static/entry/img/中国各省2016-2018年GDP情况.png" /></a>
               </li>
               <li >
               <a href="/unmarried_people" type="submit"><img class="i" src="static/entry/img/中国各省单身人口情况.png" /></a>
               </li>
               <li>
               <a href="/junior_college_people" type="submit"><img class="i" src="static/entry/img/2018年各省6岁及以上大专学历以上总人数.jpg" /></a>
               </li>
               <li>
               <a href="provice_people" type="submit"><img class="i" src="static/entry/img/各省总人口数男女人口数对比.png" /></a>
               </li>
            </ul>`
             <!--控制按钮-->
            <div class="btns" id="next"><i class="fa fa-arrow-right"><img src="static/entry/img/right.png" /></i></div>
            <div class="btns" id="previous"><img src="static/entry/img/left.png" /><i class="fa fa-arrow-left"></i></div>
            <div id="counter"></div>
            <div id="pagination-wrap">
              <ul>
              </ul>
            </div>
            <!--控制按钮-->
  			</div>
  	```
  	
  	- 第二种则是利用轮播图，以图片的方式直观的进行页面跳转。（轮播图的源码链接在文章底部）
  	![轮播图](-Python-X-Interation-FinalProject/lunbotu.png)
  
- 在所有的页面的右下角，我们都放置了一个返回首页的按钮。且在单身人口数，大专学历概况，单身男女人口数概况的页面中，都可以进行年份的筛选。

##### python档描述
- 在main.py文档中，引入了Flask,render_template,request，csv三个模块。

#### 五.使用说明
在首页上，我们交代了项目的背景及意义，在下方的轮播图中可点击你感兴趣的数据的图片，即可跳转到相关页面。在相关的页面中，上面为交互图，下部分为数据表格，有个筛选框，可选择年份进行筛选。

#### 六.贡献
由林梓仪提供交互图，罗冰楠和陈滢影负责python部分 FLASK框架部分。欢迎通过pullrequest向我们提供新的创意以及提出我们的错误。让我们的项目变得完善。

#### 七.参考
- [轮播图来源（jquery）](http://www.jq22.com/jquery-info17666)

#### 八.[GITHUB URL](https://github.com/CNCYY/-Python-X-Interation-FinalProject)

#### 九：[我的pythonanywhere](http://chanyi.pythonanywhere.com/)
