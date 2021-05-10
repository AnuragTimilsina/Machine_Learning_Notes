![alt text](https://user-images.githubusercontent.com/33256063/108596120-155dc200-73ab-11eb-9331-81fa1b96fb50.png)


# Machine_Learning_Notes
This repo consists of jupyter notebooks and actual handwritten notes for machine learning and mathematics. 

* This project aims to create a disease diagnosis system by analysing medical images
* This perticular prototype aims to diagnose Tuberculosis using X-ray images
* We are using Tensorflow(Convolution neural networks) to predict Tuberculosis
* We used TBX11K(http://mmcheng.net/tb/) dataset to train this model
* We classify the result into healthy, sick(potential TB), and Active Tuberculosis
* We have deployed our model in Django and added some further functionalities
* We aim to extend it further by adding other diagnosis techniques and support for other diseases
* We aim to keep this project opensource to further extend this platform

# Files overview
* tb_diagnosis/Diagnosis_model_code.ipynb: The actual model code
* tb_diagnosis/Model_check.ipynb: Checking the deployed model
* tb_diagnosis/install.py: Run this python file to install dependencies and download the Deep learning model in required path

# Setup
**Run the script tb_diagnosis/install.py to install dependencies and download the Deep learning model in required path**
```console
foo@bar:~$ cd ./tb_diagnosis
foo@bar:~$ python3 install.py
```

 
