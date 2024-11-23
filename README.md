# TF-Luna-micropython-library

This is a simple library that I wrote for TF-luna for my project in micropython.
I thought of sharing this code here.



### The simplest way to use is
```
from tfluna import TF_luna
from time import sleep

tf_object = TF_luna(0,4,5)    # i2c bus 1/0, sda pin, scl pin


while True:
  distance = tf_object.get_distance()   # here I am not considering the amp value and 
  print(distance)
  sleep(0.01)  #sleep is necessary , without sleep it would be stuck at one value


```


## Methods 

### factory_reset()
Reset to factory reset

### get_distance()
Returns distance in cm

### get_amp()
Returns the Amp value for checking how reliable the distance meausred is 
Amp <100 and Amp > 65535 not reliable at all

### enable_status()
Trun on the Tf luna sensor

### set_max_min_distance(max distance , min distance)
Set the maximum and minimum mesuring distance.
by default min is 0cm and max is 800cm 


### set_fps()
Set the frequency of distance measuring. It has to be like 500/n (n -> 2-500)
Meaning the max freq is 250




# Contributing
Feel free to fork this repository and contribute! If you find any issues or want to suggest new features, please open an issue or submit a pull request.


