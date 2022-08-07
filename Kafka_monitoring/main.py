from tkinter import *
import paramiko
from tkinter import messagebox

#-----------------------connect by ssh---------------------#
hostname = "192.168.73.162"
username = "ahmed"
password = "moon"
# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()
#-----------------------start zookeeper------------------------#
def start_zookeeper():
    commands ={
        "zookeeper": "sudo /home/ahmed/confluent-7.1.1/bin/zookeeper-server-start -daemon /home/ahmed/confluent-7.1.1/etc/kafka/zookeeper.properties",
        }
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        zookeeper_status.config(text="started",fg="green")
        if err:
            print(err)
#-----------------------start server0------------------------#
def start_server0():
    commands ={
        "broker0": "sudo /home/ahmed/confluent-7.1.1/bin/kafka-server-start -daemon /home/ahmed/confluent-7.1.1/etc/kafka/server0.properties",
}
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        server0_status.config(text="started",fg="green")
        if err:
            print(err)
#-----------------------start server1------------------------#
def start_server1():
    commands ={
        "broker1": "sudo /home/ahmed/confluent-7.1.1/bin/kafka-server-start -daemon /home/ahmed/confluent-7.1.1/etc/kafka/server1.properties",
}
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        server1_status.config(text="started",fg="green")
        if err:
            print(err)
#-----------------------start server2------------------------#
def start_server2():
    commands ={
        "broker2": "sudo /home/ahmed/confluent-7.1.1/bin/kafka-server-start -daemon /home/ahmed/confluent-7.1.1/etc/kafka/server2.properties",
}
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        server2_status.config(text="started",fg="green")
        if err:
            print(err)
#-----------------------start schema------------------------#
def start_schema():
    commands ={
        "schema-registry": "sudo /home/ahmed/confluent-7.1.1/bin/schema-registry-start -daemon /home/ahmed/confluent-7.1.1/etc/schema-registry/schema-registry.properties",
}
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        schema_status.config(text="started",fg="green")
        if err:
            print(err)
#-----------------------start kafka-connect------------------------#
def start_kafka_connect():
    commands ={
        "kafka-connect": "sudo /home/ahmed/confluent-7.1.1/bin/connect-standalone -daemon /home/ahmed/confluent-7.1.1/etc/kafka/connect-standalone.properties /home/ahmed/db/current-reading-sink-mysql-config.properties /home/ahmed/db/current-reading-source-mysql-metersdb2.properties /home/ahmed/db/mysql-config-meter.properties /home/ahmed/db/reading-history-sink-mysql-config.properties",
    }
    for key,command in commands.items():
        print("="*10,"starting", key, "="*10)
        stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
        stdin.write("moon\n")
        stdin.flush()
        #time.sleep(2)
        err = stderr.read().decode()
        kafka_connect_status.config(text="started",fg="green")
        if err:
            print(err)
#----------------------stop kafka--------------------------#
def stop_kafka():
    stop_commands={
        "stop-kafka": "sudo kill -9 $(pgrep java)"
    }
    for key,command in stop_commands.items():
        warning = messagebox.askokcancel(title="stopped services", message="you will stop all services \n Are you sure ?!!")
        if warning:
            print("=" * 10,key,"=" * 10)
            stdin, stdout, stderr = client.exec_command(command=command, get_pty=True)
            stdin.write("moon\n")
            stdin.flush()
            err = stderr.read().decode()
            zookeeper_status.config(text="stoped",fg="red")
            server0_status.config(text="stoped",fg="red")
            server1_status.config(text="stoped",fg="red")
            server2_status.config(text="stoped",fg="red")
            schema_status.config(text="stoped",fg="red")
            kafka_connect_status.config(text="stoped",fg="red")

            if err:
                print(err)
#-----------------------UI design--------------------------#
#start_kafka()
window=Tk()
window.title("kafka manager")
window.config(padx=15,pady=15)
window.iconbitmap("kafka_logo.ico")
image=PhotoImage(file="kafka-logo-thumb.png")
canvas=Canvas(width=500,height=210)
canvas.create_image(200,100,image=image)
canvas.grid(column=2,row=0,)
#---------------labels--------------------------#
zookeeper_label=Label(text="zookeeper service",font=("",20,"bold"))
zookeeper_label.grid(column=0,row=1,columnspan=2)

server0_label=Label(text="broker-0 service",font=("",20,"bold"))
server0_label.grid(column=0,row=2,columnspan=2)

server1_label=Label(text="broker-1 service",font=("",20,"bold"))
server1_label.grid(column=0,row=3,columnspan=2)

server2_label=Label(text="broker-2 service",font=("",20,"bold"))
server2_label.grid(column=0,row=4,columnspan=2)

schema_label=Label(text="shcema-registry service",font=("",20,"bold"))
schema_label.grid(column=0,row=5,columnspan=2)

connect_label=Label(text="kafka-connect service",font=("",20,"bold"))
connect_label.grid(column=0,row=6,columnspan=2)

#------------------------------------------------------------------------#

#------------------zookeeper start button---------------#
zookeeper_start_button=Button(text="start",command=start_zookeeper,width=20)
zookeeper_start_button.grid(column=3,row=1,columnspan=2)
#---------------------zookeeper status label-----------#
zookeeper_status=Label(text="status",font=("",20,"bold"))
zookeeper_status.grid(column=2,row=1,columnspan=2)
#-------------------------------------------------------------------------#

#------------------server0 start button---------------#
server0_start_button=Button(text="start",command=start_server0,width=20)
server0_start_button.grid(column=3,row=2,columnspan=2)
#---------------------server0 status label-----------#
server0_status=Label(text="status",font=("",20,"bold"))
server0_status.grid(column=2,row=2,columnspan=2)
#-------------------------------------------------------------------------#


#------------------server1 start button---------------#
server1_start_button=Button(text="start",command=start_server1,width=20)
server1_start_button.grid(column=3,row=3,columnspan=2)
#---------------------server1 status label-----------#
server1_status=Label(text="status",font=("",20,"bold"))
server1_status.grid(column=2,row=3,columnspan=2)
#-------------------------------------------------------------------------#

#------------------server2 start button---------------#
server2_start_button=Button(text="start",command=start_server2,width=20)
server2_start_button.grid(column=3,row=4,columnspan=2)
#---------------------server2 status label-----------#
server2_status=Label(text="status",font=("",20,"bold"))
server2_status.grid(column=2,row=4,columnspan=2)
#-------------------------------------------------------------------------#

#------------------schema start button---------------#
schema_start_button=Button(text="start",command=start_schema,width=20)
schema_start_button.grid(column=3,row=5,columnspan=2)
#---------------------schema status label-----------#
schema_status=Label(text="status",font=("",20,"bold"))
schema_status.grid(column=2,row=5,columnspan=2)
#-------------------------------------------------------------------------#

#------------------kafka-connect start button---------------#
kafka_connect_start_button=Button(text="start",command=start_kafka_connect,width=20)
kafka_connect_start_button.grid(column=3,row=6,columnspan=2)
#---------------------kafka-connect status label-----------#
kafka_connect_status=Label(text="status",font=("",20,"bold"))
kafka_connect_status.grid(column=2,row=6,columnspan=2)
#-------------------------------------------------------------------------#

# ------------------stop button---------------#
stop_button = Button(text="stop", command=stop_kafka,width=35,font=("",14,"bold"))
stop_button.grid(column=1, row=7,columnspan=5)

stop_label=Label(text="stop services",font=("",20,"bold"),fg="purple")
stop_label.grid(column=0,row=7)
window.mainloop()





















