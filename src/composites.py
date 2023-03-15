import ee

## Map over the years and create a monthly collection 
def monthly_Data (collection, years, months):
  monthly_data = []
  for year in years:
    for month in months:
      Monthly_data = collection.filter(ee.Filter.calendarRange(year, year, 'year')) \
                               .filter(ee.Filter.calendarRange(month, month, 'month')) \


      monthly_data.append (Monthly_data.mean() \
                                      .set({'month': month, 'year': year}))
      
  return ee.ImageCollection.fromImages(monthly_data)  
