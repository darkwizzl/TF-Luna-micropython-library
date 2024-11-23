from tfluna import TF_luna
from time import sleep

tf = TF_luna(0, 4, 5)
sleep(1)
#tf.factory_reset()

tf.enable_status(True)
tf.set_max_min_distance(900,0)
tf.set_fps(250)






while True:
    dis = tf.get_distance()
    print(dis)
    sleep(0.01)