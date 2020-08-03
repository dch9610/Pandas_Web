from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import seaborn as sb
import folium

import matplotlib.pyplot as plt # 시각화 지원
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

app=Flask(__name__)

@app.route("/")
def rootFn():
    return "flask main"

@app.route("/cctv")
def cctvFn():
    df=pd.read_csv('data/CCTV_in_Seoul.csv')

    cctvTotal=df['소계'].sum()
    df[['기관명','소계']].plot(x='기관명',kind='bar')
    plt.savefig('static/image/a.jpg')
    plt.close()

    return render_template('CCTV.html',data=df.values,title=df.columns,cctvTotal=cctvTotal)

@app.route("/mapview")
def mapviewFn():
    map = folium.Map(location=[35.235332, 129.082705],zoom_start=14)

    mk=folium.Marker(location=[35.235332, 129.082705],popup='자연대')
    mk.add_to(map)
    mk=folium.Marker(location=[35.231571, 129.084065],popup='부산대 정문')
    mk.add_to(map)
    map.save('templates/map.html') # map.html을 생성하여 바로 저장
    return render_template('mapview.html')

@app.route("/map")
def mapFn():
    return render_template('map.html')


if __name__=='__main__':
    app.run(debug=True)
