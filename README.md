<h2 align="center"> Rolling-Basket & Mask-detection-for-Supermarketin Live-Stream-Mask-SSD-Mobilenet-V1</h2>

<h4 align="left">Introduction
  
  
Due to covid-19  restriction nowadays peoples have to carry basket as well as they have to wear a mask then only then can enter the inside the supermarket also, this restriction makes sure by the secrurity. So, If we make this process automated way then It will be easy. So, I built a system that will generate an alert in terms of sound and text. Also, it will show the confidence value of the prediction in a live stream. So, If this project integrated with the door opening system then we can control the peoples' automated way to this Covid-19 time..</h4>

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/123372102-46314c00-d583-11eb-9a6b-efc32d431d92.jpg">
</p> 

<h2 align="center"> <span style="color:green">Rolling Basket & Face Mask Detection system built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts like SSD-Mobilenet-V1 in order to detect Rolling basket & face masks in real-time video streams.</span></h2>

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123372390-bfc93a00-d583-11eb-8a47-0a8d2b93613c.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123372387-be980d00-d583-11eb-9abb-f732651f7fd2.jpg">
  
</p> 

### 📁 Data Collection

This project has done up to 60000 epochs with error 0.09 values.Futher, 3100 images were collected among them 1000 images are without mask, 1200 images are with mask and 900 images are basket.
* With Mask: 1200
* Without Mask: 1000
* Basket: 900

### 🔑 Prerequisites
* All the dependencies and required libraries are included in the file [requirements.txt]https://github.com/KrishArul26/Rolling-Basket-Mask-detection-for-Supermarket-using-SSD-MobilenetV1/blob/main/requirements.txt)

* Python 3.6

### 🚀 Installation For Mask Detection for images

1. Clone the repo

```
git clone https://github.com/KrishArul26/Rolling-Basket-Mask-detection-for-Supermarket-using-SSD-MobilenetV1.git

```

2. Change your directory to the cloned repo

```
cd Rolling-Basket-Mask-detection-for-Supermarket-using-SSD-MobilenetV1
```

3. Create a Python 3.6 version of  virtual environment named 'mask' and activate it

 ``` 
pip install virtualenv

 ```

* Create virtual environmental

```
virtualenv basket

```
* Activate that environmental

```
basket\Scripts\activate

```

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required

```
pip install -r requirements.txt

```
### 💡 Working

1. Open terminal. Go into the cloned project directory and type the following command:

```
cd Rolling_basket_Mask_Detection_image
```

```
python mask_basket_detection.py

```
### 🔑 Results 

#### Testing-1


<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375086-7c24ff00-d588-11eb-938c-7b9b6b841d2f.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375090-7cbd9580-d588-11eb-83f7-979ae050cdb2.jpg">
</p> 

#### Testing-2



<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375153-965edd00-d588-11eb-80c1-8e568c8f5ea8.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375149-95c64680-d588-11eb-8058-4363425766e4.jpg">
</p> 


#### Testing-3


<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375258-c1493100-d588-11eb-96f6-a69c3992d39a.jpg">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/123375260-c1493100-d588-11eb-8e85-5cd781ca9162.jpg">
</p> 


<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/123377633-8cd77400-d58c-11eb-90ba-c72726623532.jpg">
</p> 

<h4 align="left">Project Circumstances
  

In this project, I just collected only 900 overall basket images but in the real, we have to collect more images in the particular domain where we are going to implement this project like Lidl or Aldi So on. Also, focus on different age categories. 
</h4>
