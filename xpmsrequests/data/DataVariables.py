
#*************************Variables*********************
TimeOut = 60
PollTime = 5
#*************************CogX URLs*********************

CmsImage = 'CMS1500_1.png'

JpgImage = 'cms_1.jpg'

CogXBaseUrl = 'http://devintkapi.apps.xpms.io/'

#CogXBaseUrl = 'http://apigw-dev.ranger.xpms.ai/apidocs'

Image = 'image'

JobIdUrl = 'http://devintkapi.apps.xpms.io/job/'

UploadUrl = CogXBaseUrl+'upload'+'/'

MimeTypeClassifierUrl = CogXBaseUrl + Image + '/' + 'mimeTypeClassifier'

ClassifyUrl = CogXBaseUrl + Image + '/' +'classify'

PreProcessUrl = CogXBaseUrl + Image + '/'+'preProcess'

SliceURL = CogXBaseUrl + Image + '/'+'slice'

OcrURL = CogXBaseUrl + Image + '/'+'ocr'

#************************jsonfiles************************

TempJson = 'temp.json'

SliceJson = 'slicejson.json'

OcrJson = 'ocrjson.json'

PreProcessJson = 'preprocess.json'

#*************************DataVariables*******************
tempData = 'Family Plan 6'

tempDataJpg = 'DIAGNOSIS POINTER_4'

classifier = 'csf'