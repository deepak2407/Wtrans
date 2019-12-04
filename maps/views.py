from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import gmplot
import simplejson
import json
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def buses(request):
    df = pd.read_csv("Transit_Windsor_Bus_Stops.csv", delimiter=",")
    df2 = pd.DataFrame(df, columns=['LATITUDE'])
    # lat = [list(x) for x in df2.values]
    latlist = df2.values.tolist()
    lata = []
    for sublist in latlist:
        for item in sublist:
            lata.append(float(item))

    #lat = df2.to_dict(orient='records')
    df3 = pd.DataFrame(df, columns=['LONGITUDE'])
    #longt = df3.to_dict(orient='records')
    # longt=[list(x) for x in df3.values]
    longtlist = df3.values.tolist()
    longta = []
    for sublist in longtlist:
        for item in sublist:
            longta.append(float(item))
    df2['LONGITUDE'] = df3
    #bcoords = [list(x) for x in df2.values]
    # coordsl = simplejson.dumps(coords)
    # print(coords)
    #tuples = [tuple(x) for x in df2.values]
    # # print(tuples)
    # import gmplot package
    #bus_lats, bus_lons = zip(*tuples)
    # #declare the center of the map, and how much we want the map zoomed in
    #gmap3 = gmplot.GoogleMapPlotter(42.3149, -83.0364, 13)
    # # Scatter map
    # gmap3.scatter( bus_lats, bus_lons, '#35B5E4',size = 14, marker = False )
    # # Plot method Draw a line in between given coordinates
    # #gmap3.plot(Charminar_top_attraction_lats, Charminar_top_attraction_lons, 'cornflowerblue', edge_width = 3.0)
    # #   save it to html
    # gmap3.draw("scatter.html")
    # return render(request,'buses.html', -83.065,42.30455)
    lat_list = simplejson.dumps(lata)
    long_list = simplejson.dumps(longta)
    return render(request, 'buses.html', {'lat': lat_list, 'longt': long_list})


def Route(request):
    if request.method == 'GET':
        froma = request.GET['fromi']
        toa = request.GET['toi']
        df = pd.read_csv("Transit_Windsor_Bus_Stops.csv", delimiter=",")
        dfb = pd.DataFrame(df, columns=['AT_STREET'])
        df2 = pd.DataFrame(df, columns=['LATITUDE'])
        # latlist = df2.values.tolist()
        # lata = []
        # for sublist in latlist:
        #     for item in sublist:
        #      lata.append(float(item))
        df3 = pd.DataFrame(df, columns=['LONGITUDE'])
        # longtlist = df3.values.tolist()
        # longta = []
        # for sublist in longtlist:
        #     for item in sublist:
        #       longta.append(float(item))
        df2['LONGITUDE'] = df3
        df2['Location'] = dfb
        df4 = df2
        df5 = df2
        locf = df4[df2.Location == froma]
        loct = df5[df2.Location == toa]
        print(locf)
        print(loct)
        froml = [tuple(x) for x in locf.values]
        tol = [tuple(x) for x in loct.values]
        # longt=df3.values.tolist()
        print(froml[0])
        
        fl = []
        tl = []
        #for sublist in froml[0]:
        #for item in froml[0]:
        #fl.append(item)
        tol = [tuple(x) for x in loct.values]
        # longt=df3.values.tolist()
        fl.append(froml[0][0])
        fl.append(tol[0][0])
        tl.append(froml[0][1])
        tl.append(tol[0][1])
        print(tol[0])
        #for sublist in tol[0]:
        #for item in tol[0]:
        #    tl.append(item)
        lat_ft = simplejson.dumps(fl)
        long_ft = simplejson.dumps(tl)
    return render(request, 'Route.html', {'from': lat_ft, 'to': long_ft})
