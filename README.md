<h2 align="center"> Smart Way Gate Monitoring System for Supermarket Due to the Covid-19 Period using AI- Live Streaming</h2>

<h3 align="left">Introduction</h3>

<p style= 'text-align: justify;'> Due to the COVID-19 restriction nowadays people have to carry baskets to enter the supermarket and they have to wear a mask so that they can enter the supermarket, this restriction is ensured by security. So, to make this process easier, I created a system where, first, it would find a man, and then it would find the mask and the basket. Also, this system will generate a warning based on sound and text if people do not carry a basket or without wearing a mask. Also, it will show the reliability value of the prediction in a live stream. So, if this project is integrated with the door opening system, we can control the automatic route of people for this Covid-19 time.</p>

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/123372102-46314c00-d583-11eb-9a6b-efc32d431d92.jpg">
</p> 

<h4 align="center"> <span style="color:green"> Rolling Basket Detection / Face Mask Detection / OpenCV / Keras / TensorFlow / Deep Learning / Computer Vision / Transfer Learning / SSD-Mobilenet-V1 / labelimg / GPU / Google Colab </span></h4>

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123372390-bfc93a00-d583-11eb-8a47-0a8d2b93613c.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123372387-be980d00-d583-11eb-9abb-f732651f7fd2.jpg">
  
</p> 

<h3 align="left">📁 Data Collection </h3>

<p style= 'text-align: justify;'>This project has done up to 60000 epochs with error 0.09 values.Futher, 3100 images were collected among them 1000 images are without mask, 1200 images are with mask and 900 images are basket.
  
                    * With Mask: 1200
  
                    * Without Mask: 1000
  
                    * Basket: 900
</p>

<h3 align="left"> Sample of basket images </h3>

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/123382231-fc039700-d591-11eb-94b6-fc362fe8ac7d.jpg">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/123382263-04f46880-d592-11eb-821e-3c8e60ecd45c.jpg">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/123382291-0c1b7680-d592-11eb-8fd6-398c31c8af39.jpg">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/123382312-12115780-d592-11eb-8f3b-77148ffd8602.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123382361-281f1800-d592-11eb-9a9b-d58fafa1194a.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123382395-31a88000-d592-11eb-9dbc-2e8ddb86c675.jpg">
</p> 


<h3 align="left">🔑 Prerequisites </h3>

* All the dependencies and required libraries are included in the file [requirements.txt](https://github.com/KrishArul26/Rolling-Basket-Mask-detection-for-Supermarket-using-SSD-MobilenetV1/blob/main/requirements.txt)

* Python 3.6

<h3 align="left">🚀 Installation For Smart gate Monitoring system for images</h3>

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

<h3 align="left"> 💡 Working </h3>

1. Open terminal. Go into the cloned project directory and type the following command:

```
cd Rolling_basket_Mask_Detection_image
```

```
python mask_basket_detection.py

```

<h3 align="left"> Testing-1 </h3>

<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375086-7c24ff00-d588-11eb-938c-7b9b6b841d2f.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375090-7cbd9580-d588-11eb-83f7-979ae050cdb2.jpg">
</p> 

<h3 align="left"> Testing-2 </h3>

<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375153-965edd00-d588-11eb-80c1-8e568c8f5ea8.jpg">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375149-95c64680-d588-11eb-8058-4363425766e4.jpg">
</p> 

<h3 align="left"> Testing-3 </h3>

<p align="left">
  <img width="400" src="https://user-images.githubusercontent.com/74568334/123375258-c1493100-d588-11eb-96f6-a69c3992d39a.jpg">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/123375260-c1493100-d588-11eb-8e85-5cd781ca9162.jpg">
</p> 

<h2 align="left">Project Circumstances</h2>

<p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/123377633-8cd77400-d58c-11eb-90ba-c72726623532.jpg">
</p> 


<p style= 'text-align: justify;'> In this project, I only collected 900 overall basket images, but in fact, we need to collect more basket images depend on the domain where to be implemented in the system as well as should  focus on different age categories.</p>

