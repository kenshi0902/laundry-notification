from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

import numpy as np
import matplotlib.pyplot as plt

def plot_loop():
    # センサーデータ取得
    temp = "%4.1f" % sensor.get_temp()
    gyro_data = sensor.get_gyro_data()
    accel_data = sensor.get_accel_data()
    
    fig, (ax_temp, ax_gyro, ax_accel) = plt.subplots(ncols=3, figsize=(10,7))
    
    # X座標
    sec = np.arange(-np.pi, np.pi, 0.1)
    
    # 温度のY座標
    temp_list = np.zeros(63)
    temp_list[0] = temp
    line_temp, = ax_temp.plot(sec, temp_list, color="red")
    ax_temp.set_title("temperature")
    ax_temp.set_ylim(-10, 40)
    ax_temp.set_xticks([]) # X軸のメモリ非表示

    # 角速度のY座標
    # ロール軸(x)
    gyro_list_x = np.zeros(63)
    gyro_list_x[0] = "%6.3f" % gyro_data['x']
    gyro_x_lines, = ax_gyro.plot(sec, gyro_list_x, color="red", label="x")

    # ピッチ軸(y)
    gyro_list_y = np.zeros(63)
    gyro_list_y[0] = "%6.3f" % gyro_data['y']
    gyro_y_lines, = ax_gyro.plot(sec, gyro_list_y, color="blue", label="y")
    
    # ヨー軸(z)
    gyro_list_z = np.zeros(63)
    gyro_list_z[0] = "%6.3f" % gyro_data['z']
    gyro_z_lines, = ax_gyro.plot(sec, gyro_list_z, color="green", label="z")
    
    ax_gyro.legend() # ラベル描画
    ax_gyro.set_title("gyro")
    ax_gyro.set_ylim(-300, 300)
    ax_gyro.set_xticks([]) # X軸のメモリ非表示

    # 加速度のY座標
    # ロール軸(x)
    accel_list_x = np.zeros(63)
    accel_list_x[0] = "%6.3f" % accel_data['x']
    accel_x_lines, = ax_accel.plot(sec, accel_list_x, color="red", label="x")

    # ピッチ軸(y)
    accel_list_y = np.zeros(63)
    accel_list_y[0] = "%6.3f" % accel_data['y']
    accel_y_lines, = ax_accel.plot(sec, accel_list_y, color="blue", label="y")
    
    # ヨー軸(z)
    accel_list_z = np.zeros(63)
    accel_list_z[0] = "%6.3f" % accel_data['z']
    accel_z_lines, = ax_accel.plot(sec, accel_list_z, color="green", label="z")
        
    ax_accel.legend() # ラベル描画
    ax_accel.set_title("accel")
    ax_accel.set_ylim(-30, 30)
    ax_accel.set_xticks([]) # X軸のメモリ非表示

    # plotし続ける
    while True:
        # センサーデータ取得
        temp = "%4.1f" % sensor.get_temp()
        gyro_data = sensor.get_gyro_data()
        accel_data = sensor.get_accel_data()
        
        # データの更新
        sec += 0.1
        
        temp_list = np.roll(temp_list, 1)
        temp_list[0] = temp

        gyro_list_x = np.roll(gyro_list_x, 1)
        gyro_list_x[0] = "%6.3f" % gyro_data['x']
        gyro_list_y = np.roll(gyro_list_y, 1)
        gyro_list_y[0] = "%6.3f" % gyro_data['y']
        gyro_list_z = np.roll(gyro_list_z, 1)
        gyro_list_z[0] = "%6.3f" % gyro_data['z']

        accel_list_x = np.roll(accel_list_x, 1)
        accel_list_x[0] = "%6.3f" % accel_data['x']
        accel_list_y = np.roll(accel_list_y, 1)
        accel_list_y[0] = "%6.3f" % accel_data['y']
        accel_list_z = np.roll(accel_list_z, 1)
        accel_list_z[0] = "%6.3f" % accel_data['z']

        # グラフへデータの再セット
        line_temp.set_data(sec, temp_list)
        line_temp.set_data(sec, temp_list)
        
        gyro_x_lines.set_data(sec, gyro_list_x)
        gyro_y_lines.set_data(sec, gyro_list_y)
        gyro_z_lines.set_data(sec, gyro_list_z)

        accel_x_lines.set_data(sec, accel_list_x)
        accel_y_lines.set_data(sec, accel_list_y)
        accel_z_lines.set_data(sec, accel_list_z)

        # X軸の更新
        ax_temp.set_xlim((sec.min(), sec.max()))
        ax_gyro.set_xlim((sec.min(), sec.max()))
        ax_accel.set_xlim((sec.min(), sec.max()))

        print("【温度】" + temp + "℃")
        print("【角速度】 x:" + "%6.3f" % gyro_data['x'] + " y:" + "%6.3f" % gyro_data['y'] + " z:" + "%6.3f" % gyro_data['z'])
        print("【加速度】 x:" + "%6.3f" % accel_data['x'] + " y:" + "%6.3f" % accel_data['y'] + " z:" + "%6.3f" % accel_data['z'])

        plt.pause(0.1) # sleep時間（秒）

if __name__ == "__main__":
    plot_loop()