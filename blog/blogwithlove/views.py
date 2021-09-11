from django.shortcuts import render,redirect,HttpResponse
import pandas as pd
from .models import Year,Contact
import json
import chart_studio as py
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()

# Create your views here.
def index(request):
    yeara='2020'
    df = pd.read_csv('data')
    data = dict(type='choropleth',
                locations=df['Country Code'],
                colorscale=[[0.0, "rgb(165,0,38)"],
                [0.1111111111111111, "rgb(215,48,39)"],
                [0.2222222222222222, "rgb(244,109,67)"],
                [0.3333333333333333, "rgb(253,174,97)"],
                [0.4444444444444444, "rgb(254,224,144)"],
                [0.5555555555555556, "rgb(224,243,248)"],
                [0.6666666666666666, "rgb(171,217,233)"],
                [0.7777777777777778, "rgb(116,173,209)"],
                [0.8888888888888888, "rgb(69,117,180)"],
                [1.0, "rgb(49,54,149)"]],
                text=df['Country'],

                z=df[yeara],
                marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
                colorbar={'title': 'GDP'})
    layout = dict(title=f"World's GDP In {yeara}", autosize=True,
                  geo=dict(showframe=False, projection={'type': 'natural earth'}))
    chormap = go.Figure(data=[data], layout=layout)
    plt_div = plot(chormap, output_type='div')

    return render(request, 'index.html', {'plot_div': plt_div})


def about(request):
    return render(request, 'about.html')

def years(request):
    year = Year.objects.all()
    return render(request, 'years.html', {'years': year})
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get("email")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        return render(request,"success.html")
    else:
        return render(request, "contact.html")



def viewgdp(request):
    yeara = request.GET.get('year')
    if (yeara):
        df= pd.read_csv('data')
        data=dict(type = 'choropleth',
                  locations=df['Country Code'],
                  colorscale='Viridis',
                  text=df['Country'],

                  z=df[yeara],
                  marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
        colorbar={'title':'GDP'})
        layout = dict(title=f"World's GDP In {yeara}",autosize=True,
                      geo=dict(showframe=False,projection={'type':'natural earth'}))
        chormap = go.Figure(data=[data],layout=layout)
        plt_div=plot(chormap,output_type='div')

        return render(request,'viewgdp.html',{'plot_div':plt_div})
    else:
        return render(request, 'index.html')

def search(request):
        yearaa= request.GET.get('search')
        if (int(yearaa)>=1960 and int(yearaa)<=2020 ):
            df = pd.read_csv('data')
            data = dict(type='choropleth',
                        locations=df['Country Code'],
                        colorscale='rdbu',
                        text=df['Country'],
    
                        z=df[yearaa],
                        marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
                        colorbar={'title': 'GDP'})
            layout = dict(title=f"World's GDP In {yearaa}", autosize=True,
                          geo=dict(showframe=False, projection={'type': 'natural earth'}))
            chormap = go.Figure(data=[data], layout=layout)
            plt_div = plot(chormap, output_type='div')
            return render(request, 'search.html',{'plot_div':plt_div,'year':yearaa})
        else:
            return render(request, 'searcherror.html',{'year':yearaa})

