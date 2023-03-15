def maskS2clouds(image):
  qa = image.select('QA60');

  #Bits 10 and 11 are clouds and cirrus, respectively.
  cloudBitMask = 1 << 10;
  cirrusBitMask = 1 << 11;

  # Both flags should be set to zero, indicating clear conditions.
  mask = (qa.bitwiseAnd(cloudBitMask).eq(0)).And(qa.bitwiseAnd(cirrusBitMask).eq(0));

  return image.updateMask(mask)\
              .divide(10000)\
              .copyProperties(image, ["system:time_start"]);



def maskL89sr (image) :
  qa = image.select(['QA_PIXEL']);
  
  # Bits 3, 4, and 5 are cloud, cloud shadow and, snow respectively.
  cloudsBitMask = 1 << 3
  cloudShadowBitMask = 1 << 4   
  snowBitMask = 1 << 5
  
  # All flags should be set to zero, indicating clear conditions.
  mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0)\
           .And(qa.bitwiseAnd(cloudsBitMask).eq(0))\
           .And(qa.bitwiseAnd(snowBitMask).eq(0));
          
  # Return the masked image, scaled to TOA reflectance, without the QA bands.
  return image.updateMask(mask)\
              .select('SR_B.').multiply(0.0000275).add(-0.2)\
              .copyProperties(image, ["system:time_start"]);


def maskL57sr (image) :
  qa = image.select('QA_PIXEL'); 
  
  # Bits 3, 4, and 5 are cloud, cloud shadow and, snow respectively.
  cloudsBitMask = 1 << 3; 
  cloudShadowBitMask = 1 << 4;   
  snowBitMask = 1 << 5;
                 
  # All flags should be set to zero, indicating clear conditions.
  mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0) \
               .And(qa.bitwiseAnd(cloudsBitMask).eq(0)) \
               .And(qa.bitwiseAnd(snowBitMask).eq(0));
               
               
  # Return the masked image, scaled to TOA reflectance, without the QA bands.
  return image.updateMask(mask) \
              .select('SR_B.').multiply(0.0000275).add(-0.2) \
              .copyProperties(image, ["system:time_start"]);