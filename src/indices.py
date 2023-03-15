def compute_ndwi(image):
  return image.addBands(image.expression('(NIR-MIR)/(NIR+MIR)',{
      'NIR':image.select('B8'),
      'MIR':image.select('B12')
    }).rename('NDWI'))\
      .copyProperties(image, ["system:time_start"])

def compute_ndvi(image):
  return image.addBands(image.expression('(NIR-RED)/(NIR+RED)',{
      'NIR':image.select('B8'),
      'RED':image.select('B4')
    }).rename('NDVI'))\
      .copyProperties(image, ["system:time_start"])

def compute_msavi2(image):
    return image.addBands(image.expression('(2 * NIR + 1 - ( (2 * NIR + 1)**2 - 8 * (NIR - RED) )**(1/2) ) / 2',{
      'NIR':image.select('B8'),
      'RED':image.select('B4')
    }).rename('MSAVI2'))\
      .copyProperties(image, ["system:time_start"])


def compute_savi(image):
    return image.addBands(image.expression('((NIR - RED) / (NIR + RED + 0.5)) * (1 + 0.5)',{
      'NIR':image.select('B8'),
      'RED':image.select('B4')
    }).rename('SAVI'))\
      .copyProperties(image, ["system:time_start"])
