# Sorting_pkg
### Problem statement:
" Develop a Python node which subscribe to the /hello (std_msgs/String) topic, sort the letters and publish the result to the /sorted (std_msgs/String) topic. Also create a service which can be called to disable and enable the publisher"

## Compile
```
cd ~/catkin_ws
catkin_make
```
## Usage

### To start up the node:

```
rosrun sort_pkg sorting_node.py
```

To publish a string  open a terminal and type

```
rostopic pub /hello std_msgs/String "data: 'ragesh ramachandran'"
```
To echo the topic
```
rostopic echo /sort
```
### To start up the node with service :

```
rosrun sort_pkg sort_node_service.py

```
To call the service to enable or disbale the sorting process

```
rosservice call /enable_service std_msgs/String "data: '__ service_calls_here___'"

```
Possible service calls are: (case insensitive)
1. enable
2. disable
