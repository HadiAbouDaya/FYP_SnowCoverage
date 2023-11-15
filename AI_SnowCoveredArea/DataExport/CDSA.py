import cdsapi

c = cdsapi.Client()
years = ['1993', '1994', '1995', '1996', '1997', '1998', '1999',"2000","2001", '2002', '2003', '2004', '2005','2006',"2007","2008","2009","2010","2011","2012"
                ,"2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"]

months = ['11', '12', '1', '2', '3','4','5','6','7']

for year in years:
    for month in months:
        c.retrieve(
            'reanalysis-era5-land',
            {
                'variable': 'snow_depth',
                'year': year,
                'month': month,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                ],
                'time': '10:00',
                #north west south east
                'area': [34.6, 35.25, 33,36.50],
                'format': 'netcdf.zip',
            },
            './RawData/LebanonSnowData_{}.netcdf.zip'.format('month_' + month +"year_" + year))
