from flask import Flask,render_template
from flask import render_template
from flask import request
import csv

app = Flask(__name__)

@app.route('/')
def base() -> 'html':
    return render_template('entry.html')

#2016年-2018年全国男女人口占比
@app.route('/total_people',methods=['GET'])
def total_people() -> 'html':
    title = "2016年-2018年全国男女人口占比"
    titles = ("年份","总人数","男性人数","女性人数","男性人数占比","女性人数占比"
)
    contents = []
    with open('China_total_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('China_total_people.html',
                           the_title = title,
                           the_row_titles = titles,
                           the_data = contents)

#2016-2018年各省总人口数和男女人口数对比
@app.route('/provice_people')
def provice_people() -> 'html':
    title = "2016-2018年各省总人口数和男女人口数对比"
    return render_template('provice-people.html',
                           the_title = title,
                          )
@app.route('/provice_people/2016')
def provice_people_2016() -> 'html':
    title = "2016年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('2016_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/provice_people/2017')
def provice_people_2017() -> 'html':
    title = "2017年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('2017_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/provice_people/2018')
def provice_people_2018() -> 'html':
    title = "2018年各省总人口数和男女人口数对比"
    titles = ("省份","总人口数","男性人口数","女性人口数"
)
    contents = []
    with open('2018_province_people.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-people.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

#GDP
@app.route('/GDP')
def GDP() -> 'html':
    title = "中国各省2016-2018年GDP情况"
    titles = ("省份","2018年","2017年","2016年")
    contents = []
    with open('China_GDP.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('GDP.html',
                           the_title = title,
                           the_row_titles = titles,
                           the_data = contents)

#中国各省单身人口情况
@app.route('/unmarried_people')
def provice_unmarried_people() -> 'html':
    title = "2016-2018年中国各省单身人口情况"
    return render_template('provice-unmarried.html',
                           the_title = title,
                          )
@app.route('/unmarried_people/2016')
def provice_unmarried_people_16() -> 'html':
    title = "2016年中国各省单身人口情况"
    titles = ("省份","总单身数","男性单身数","女性单身数"
)
    contents = []
    with open('16_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/unmarried_people/2017')
def provice_unmarried_people_17() -> 'html':
    title = "2017年中国各省单身人口情况"
    titles = ("省份", "总单身数", "男性单身数", "女性单身数")
    contents = []
    with open('17_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/unmarried_people/2018')
def provice_unmarried_people_18() -> 'html':
    title = "2018年中国各省单身人口情况"
    titles = ("省份", "总单身数", "男性单身数", "女性单身数")
    contents = []
    with open('18_unmarried.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('provice-unmarried.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )


#大专学历以上总人数和男女人数
@app.route('/junior_college_people')
def junior_college_people() -> 'html':
    title = "2016-2018年中国各省大专学历以上总人数和男女人数"
    return render_template('junior_college.html',
                           the_title = title,
                          )
@app.route('/junior_college_people/2016')
def junior_college_people_2016() -> 'html':
    title = "2016年中国各省大专学历以上总人数和男女人数"
    titles = ("省份","总人数","男性人数","女性人数")
    contents = []
    with open('16_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )

@app.route('/junior_college_people/2017')
def junior_college_people_2017() -> 'html':
    title = "2017年中国各省大专学历以上总人数和男女人数"
    titles = ("省份", "总人数", "男性人数", "女性人数")
    contents = []
    with open('17_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )
@app.route('/junior_college_people/2018')
def junior_college_people_2018() -> 'html':
    title = "2018年中国各省大专学历以上总人数和男女人数"
    titles = ("省份", "总人数", "男性人数", "女性人数")
    contents = []
    with open('18_junior_college.csv') as csv:
        for line in csv:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(item)
    return render_template('junior_college.html',
                           the_title=title,
                           the_row_titles=titles,
                           the_data=contents
                           )


@app.route('/GDP+',methods=['GET'])
def GDPUNMARRIED():
    with open('Chian_GDP_line.csv')as df:
        GS=df.loc[1:21]
    return render_template('GDP+.html')



if __name__ == '__main__':
    app.run()