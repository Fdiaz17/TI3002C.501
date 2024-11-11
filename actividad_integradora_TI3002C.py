import pandas as pd
#import plotly.express as px
import streamlit as st
#import numpy as np
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown("<h1 style= 'text-align: center;color: #F2F9FF;'>Police Department of San Francisco Crime Reports</h1>", unsafe_allow_html=True)
st.markdown("---")


df = pd.read_csv("Policev1.csv")

df=df.drop(['Report Datetime', 'Row ID', 'Incident ID',
       'Incident Number', 'CAD Number', 'Report Type Code',
       'Report Type Description', 'Filed Online', 'Incident Code','Incident Subcategory', 'Incident Description',
       'Intersection', 'CNN','Analysis Neighborhood', 'Supervisor District','point', 'SF Find Neighborhoods', 'Current Police Districts',
       'Current Supervisor Districts', 'Analysis Neighborhoods',
       'HSOC Zones as of 2018-06-05', 'OWED Public Spaces','Central Market/Tenderloin Boundary Polygon - Updated',
       'Parks Alliance CPSI (27+TL sites)', 'ESNCAG - Boundary File','Areas of Vulnerability, 2016'],axis=1)
df['Incident Date'] = pd.to_datetime(df['Incident Date']).dt.normalize()
df=df.dropna(axis=0,how='any') 
df
#----------------------------------------------
#--- FILTROS ---
#st.sidebar.header("Filtering Options")
#Year = st.sidebar.selectbox("Year:",('2018','2019','2020'))
  
#Dist = st.sidebar.selectbox("District:",('Out of SF', 'Park', 'Bayview', 'Mission', 'Southern', 'Taraval',
#       'Northern', 'Central', 'Ingleside', 'Richmond', 'Tenderloin')
#)
#----------------------------------------------
#--- CONTENEDORES ---
#mapa_metricas= st.container()
#barrasypastel=st.container()

#----------------------------------------------

#with mapa_metricas:
#    col1,col2=st.columns(2)
#    df2=df[df['Incident Date'].dt.year==int(Year)]
#    df2=df2[df2['Police District']==Dist]
#    mapa=pd.DataFrame()
#    mapa['lat']=df2['Latitude']
#    mapa['lon']=df2['Longitude']
#    mapa=mapa.dropna()
#    col1.markdown("<h4 style= 'color: #F2F9FF;'>Crime Map</h4>", unsafe_allow_html=True)
#    col1.map(mapa)
    #------------------------------
    #--- PIE CHART ---
'''result=df2['Resolution'].value_counts()
    pie_resul=pd.DataFrame()
    pie_resul['Resolution']=result.index
    r=[]
    for i in range(len(result)):
        r.append(result[i])
    pie_resul['Total']=r
    fig3=go.Figure(data=[go.Pie(labels=pie_resul['Resolution'], values=pie_resul['Total'], pull=[0,0.1,0.08,0.12],hole=.5)])
    fig3.update_layout(margin=dict(l=5,r=5,b=10,t=10))
    fig3.update_traces(marker=dict(colors=['#0B3954','#E72323','#BFD7EA','#ECD444']))
    col2.markdown("<h4 style= 'color: #F2F9FF;'>Resolution</h4>", unsafe_allow_html=True)
    col2.write(fig3)

with barrasypastel:
    col1,col2,col3=st.columns(3)
    df2=df[df['Incident Date'].dt.year==int(Year)]
    df2=df2[df2['Police District']==Dist]
    dias=df2['Incident Day of Week'].value_counts()
    bar_dias=pd.DataFrame()
    bar_dias['Day Of Week']=dias.index
    d=[]
    for i in range(len(dias)):
        d.append(dias[i])
    bar_dias['Crimes Reported']=d
    fig1=px.bar(bar_dias,x='Day Of Week',y='Crimes Reported',color='Crimes Reported',color_continuous_scale=['#BFD7EA','#0B3954','#E72323'])
    fig1.update_layout(margin=dict(l=5,r=5,b=10,t=10))
    fig1.update(layout_coloraxis_showscale=False)
    col1.markdown("<h4 style= 'text-align: center ;color: #F2F9FF;'>Most Crimes Reported by Day of Week</h4>", unsafe_allow_html=True)
    col1.write(fig1)
    time=df2['Incident Time'].value_counts()
    bar_time=pd.DataFrame()
    #bar_time['Hour of the Day']=time.index
    h=[]
    top_hr=st.sidebar.slider("Top # Hours with most Crimes",min_value=1,max_value=10,value=5)
    for i in range(top_hr):
        #bar_time['Hour of the Day']=time.index[i]
        h.append(time[i])
    bar_time['Hour of the Day']=time.index[:top_hr]
    bar_time['Crimes Reported']=h
    bar_time = bar_time.sort_values('Crimes Reported', ascending=True)
    fig2=px.bar(bar_time,x='Crimes Reported',y='Hour of the Day',color='Crimes Reported',color_continuous_scale=['#BFD7EA','#0B3954','#E72323'])
    fig2.update_layout(margin=dict(l=5,r=5,b=10,t=10))
    fig2.update(layout_coloraxis_showscale=False)
    col3.markdown("<h4 style= 'text-align: center;color: #F2F9FF;'>Top Crime Schedule</h4>", unsafe_allow_html=True)
    col3.write(fig2)
    #-------------------------------
    #--- TABLA ---
    num=df2['Incident Category'].value_counts()
    tabla=pd.DataFrame()
    tabla['Incident']=num.index
    t=[]
    for i in range(len(num)):
        t.append(num[i])
    tabla['Quantity']=t
    tabla=tabla.sort_values('Quantity',ascending=False)
    fig=go.Figure(data=go.Table(
            header=dict(values=list(tabla[['Incident','Quantity']].columns),
            fill_color='#0B3954',
            line_color='#0E1117'),
            cells=dict(values=[tabla.Incident,tabla.Quantity],
            fill_color='#6B9AC4',
            line_color='#0E1117')
        ))
    fig.update_layout(margin=dict(l=5,r=5,b=10,t=10))
    col2.markdown("<h4 style= 'text-align: center ;color: #F2F9FF;'>Incidents</h4>", unsafe_allow_html=True)
    col2.write(fig) '''
