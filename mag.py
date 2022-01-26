from asyncio.windows_events import NULL


def listen_magnetometer():
    import matplotlib.pyplot as plt
    import socket
    import csv

    # Get host from Wireless LAN adapter wi-fi ipv4.
    HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
    PORT = 65436  # Port to listen on (non-privileged ports are > 1023)
    print("Listening on " + str(HOST) + ":" + str(PORT))

    #x_arr, y_arr, z_arr = [], [], []
    x_gyro_arr, y_gyro_arr, z_gyro_arr = [], [], []
    x_mag_arr, y_mag_arr, z_mag_arr = [], [], []
    x_acc_arr, y_acc_arr, z_acc_arr = [], [], []
    
    #To create ONE figure
    plt.figure(1)
    

    #To open TCP Port, create a server to listen to
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept() 

        with conn:
            print('Connected by my phone with ip address: ', addr)
            while True:
                data = conn.recv(1024) #receive binary data
                if data.decode() != "":   #decode the binary data from my phone
                    data = data.decode('utf-8') 
                    print(data) 

                    split = data.replace(")", "").replace("(","").replace("'","").replace(" ","").split(",")
                    print(len(split))
                    print(split[0]) # split[0] == 'magnet' or 'gyro' or? 'acc' AND sometimes split[4] != "" but split[4] == 'acc' or? 'magnet' or 'gyro'
                    # if split[0] == 'magnet' then x_mag = split[1]
                    
                    x_mag, y_mag, z_mag, x_gyro, y_gyro, z_gyro, x_acc, y_acc, z_acc = float(split[1]), float(split[2]), float(split[3]), float(split[5]), float(split[6]), float(split[7]), float(split[9]), float(split[10]), float(split[11])
                    '''
                    if split[0]=='magnet':
                        try:
                            x_mag, y_mag, z_mag = float(split[1]), float(split[2]), float(split[3])
                            print('it is magnet')
                        except:
                            continue
                    elif split[0]=='acc':
                        try:
                            x_acc, y_acc, z_acc = float(split[1]), float(split[2]), float(split[3])
                        except:
                            continue
                    elif split[0]=='gyro':
                        try:
                            x_gyro, y_gyro, z_gyro = float(split[1]), float(split[2]), float(split[3])
                        except:
                            continue
                    if len(split)>4:
                        print('it is longer than 4')
                        print(split[4])
                        if split[4]=='magnet':
                            try:
                                x_mag, y_mag, z_mag = float(split[5]), float(split[6]), float(split[7])
                            except:
                                continue
                        elif split[4]=='acc':
                            try:
                                x_acc, y_acc, z_acc = float(split[5]), float(split[6]), float(split[7])
                            except:
                                continue
                        elif split[4]=='gyro':
                            try:
                                x_gyro, y_gyro, z_gyro = float(split[5]), float(split[6]), float(split[7])
                                print('it is gyro')
                            except:
                                continue
                    if len(split)>8:
                        if split[8]=='magnet':
                            try:
                                x_mag, y_mag, z_mag = float(split[9]), float(split[10]), float(split[11])
                            except:
                                continue
                        elif split[8]=='acc':
                            try:
                                x_acc, y_acc, z_acc = float(split[9]), float(split[10]), float(split[11])
                                print('it is acc')
                            except:
                                continue
                        elif split[8]=='gyro':
                            try:
                                x_gyro, y_gyro, z_gyro = float(split[9]), float(split[10]), float(split[11])
                            except:
                                continue
                    '''

                    
                    #write data to CSV file
                    file=open('C:/Users/m31st/Desktop/measurement/m01.csv', 'a', newline= '')
                    #create the CSV writer
                    writer=csv.writer(file)
                    #write a row to the CSV file
                    #for row in data:
                    writer.writerow(['mag:', x_mag, y_mag, z_mag, 'gyro:', x_gyro, y_gyro, z_gyro, 'acc:', x_acc, y_acc, z_acc])
                        #writer.writerow({'mag:',  z_mag, 'gyro:',  z_gyro, 'acc:',  z_acc})

                    #close the file
                    print(['written','mag:', x_mag, y_mag, z_mag, 'gyro:', x_gyro, y_gyro, z_gyro, 'acc:', x_acc, y_acc, z_acc])
                    file.close()
                    
                    
                    if len(x_acc_arr) > 20:
                        x_acc_arr.pop(0)
                    x_acc_arr.append(x_acc)
                    if len(y_acc_arr) > 20:
                        y_acc_arr.pop(0)
                    y_acc_arr.append(y_acc)
                    if len(z_acc_arr) > 20:
                        z_acc_arr.pop(0)
                    z_acc_arr.append(z_acc)
                    if len(x_mag_arr) > 20:
                        x_mag_arr.pop(0)
                    x_mag_arr.append(x_mag)
                    if len(y_mag_arr) > 20:
                        y_mag_arr.pop(0)
                    y_mag_arr.append(y_mag)
                    if len(z_mag_arr) > 20:
                        z_mag_arr.pop(0)
                    z_mag_arr.append(z_mag)
                    if len(x_gyro_arr) > 20:
                        x_gyro_arr.pop(0)
                    x_gyro_arr.append(x_gyro)
                    if len(y_gyro_arr) > 20:
                        y_gyro_arr.pop(0)
                    y_gyro_arr.append(y_gyro)
                    if len(z_gyro_arr) > 20:
                        z_gyro_arr.pop(0)
                    z_gyro_arr.append(z_gyro)
                    
                    i = list(range(len(x_acc_arr)))
                    j = list(range(len(x_mag_arr)))
                    k = list(range(len(x_gyro_arr)))
                    plt.clf()
                    
                    # Limit the gyro values to max of +/- 1 because we don't want to destroy the wheel
                    if y_gyro < -1:
                        y_gyro = -1
                    if y_gyro > 1:
                        y_gyro = 1
                    if z_gyro < -1:
                        z_gyro = -1
                    if z_gyro > 1:
                        z_gyro = 1
                    line = ""
                    if y_gyro <= 0:
                        line += "ACCELERATE %.2f\t"%abs(y_gyro)
                    if y_gyro > 0:
                        line += "BREAK      %.2f\t"%y_gyro
                    if z_gyro <= 0:
                        line += "RIGHT %.2f"%z_gyro
                    if z_gyro > 0:
                        line += "LEFT  %.2f"%abs(z_gyro)
                        
                    print(line)    
                    
                    #ax1.plot(i, y_acc_arr)
                    #ax1.plot(i, z_acc_arr)
                    #ax2.plot(j, y_mag_arr)
                    #ax2.plot(j, z_mag_arr)
                    #ax3.plot(k, y_gyro_arr)
                    #ax3.plot(k, z_gyro_arr)   
                    plt.subplot(311)
                    plt.plot(i, y_acc_arr, label='Accelerometer_Y')
                    plt.plot(i, z_acc_arr, label='Accelerometer_Z')
                    plt.title('Accelerometer')
                    plt.legend()
                    plt.subplot(312)
                    plt.plot(j, y_mag_arr, label='Magnetometer_Y')
                    plt.plot(j, z_mag_arr, label='Magnetometer_Z')
                    plt.legend()
                    plt.title('Magnetometer')
                    plt.subplot(313)
                    plt.plot(k, y_gyro_arr, label='Gyroscope_Y')
                    plt.plot(k, z_gyro_arr, label='Gyroscope_Z')
                    plt.title('Gyroscope')
                    plt.legend()


                    #increase space between subplots to avoid overlap
                    plt.subplots_adjust(hspace=.5)
                    #update every 0.2 second
                    plt.pause(.2)


if __name__ == "__main__":
    listen_magnetometer()