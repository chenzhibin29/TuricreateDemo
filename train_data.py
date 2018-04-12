import turicreate as tc
path1='/home/chen/Desktop/demo-python-image-classification-master/image/test'
data=tc.image_analysis.load_images(path1,with_path=True)
#file label
def ju(path):
    if 'compter' in path:
        return 'compter'
    elif 'wheel' in path:
        return 'wheel'
    else:
        return 'dianji'
data['label']=data['path'].apply(ju)
data
data.save('test.sframe')
train_data,test_data=data.random_split(0.8,seed=2)
#load data
data=tc.load_sframe('test.sframe')
#training data
train_data, test_data = data.random_split(0.8, seed=2)
model = tc.image_classifier.create(train_data, target='label')
#save model
model.save('mymodel2')
#test train_data
predictions=model.predict(test_data)
predictions
#print accuracy
metrics=model.evaluate(test_data)
print(metrics['accuracy'])

#look train_data
test_data['label']
#look false pictures
test_data[test_data['label']!=predictions]
wrong_pred_img_path=test_data[predictions!=test_data['label']][0]['path']
img=tc.Image(wrong_pred_img_path)
img.show()
#test own pictures,pictures is saved in 'computer' file
image2='/home/chen/Desktop/demo-python-image-classification-master/image/computer'
data3 = tc.image_analysis.load_images(image2, with_path=True)
metrics=model.evaluate(data3)
prediction1=model.predict(data3)
prediction1
