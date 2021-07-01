<br />
<p align="center">
<strong>Attendance Using Face Recognition</strong>
  <p align="center">
    A website built for the ease of a teacher to view and save the attendance of students enabled by face recognition!
    <br />
    <a href="https://github.com/SaakshiShah25/Face_recognition"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    View Demo
    ·
    <a href="https://github.com/SaakshiShah25/Face_recognition/issues">Report Bug</a>
    ·
    <a href="https://github.com/SaakshiShah25/Face_recognition/issues">Request Feature</a>
  </p>
</p>

## Team
* <a href="https://github.com/SaakshiShah25"><b>Saakshi Shah</b></a> - Full Stack 
* <a href="https://github.com/sanket1703"><b>Sanket Shah</b></a> - Model Training,Face Detection & Face Recognition
 

## About the Project
<p align="center">
<img style="margin:1em" src="https://imgur.com/PaHU03B.gif" width="100%"/>
</p>

### Pages
* Login
* Sign Up
* Home
* Teacher Details
* Attendance Table
* CSV File





## Usage 

### Step 1 - Extract embeddings

> Once the face detector detects a face we need to get information of the image to pass it forward to train the model. Here we extract 128 features 
from the image, this gives a matrix having 128 features of the image. 

> Run the following code in your console after keeping the images of the faces you want to train in the dataset folder

```shell
python extract_embeddings.py --dataset dataset \
	--embeddings output/embeddings.pickle \
	--detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7
```

### Step 2 - Train Model

> To train the model with the new dataset, run the following commands 

```shell
python train_model.py --embeddings output/embeddings.pickle \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle
```

### Step 3.a - Recognize faces from Video

> Run the python file - recognize_video.py

### Step 3.b - Recognize faces from an Image

> Run the following commands, and add the input image name in place of {image name comes here}

```shell
python recognize.py --detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7 \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle \
	--image images/{image name comes here}.jpg  #be sure to keep it in the image folder
```

### Features

##### Options for selection of teacher details
A simple form allowing teacher to select their respective subject to be taught in a particular class along with the year and division of class.

##### Detailed attendance table
Table displaying all students present in the class along with the teaching faculty's details.

##### Saving data in CSV
The data of the attendance table is saved into CSV enabling easy access and storage of data for the teacher.



### Built Using
* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [OpenCV](https://opencv.org/) - Real-time computer vision
* [dbsqlite3](https://sqlitebrowser.org/) - Database connectivity
### Built On
* [Visual Studio Code](https://code.visualstudio.com/) - Code Editor
