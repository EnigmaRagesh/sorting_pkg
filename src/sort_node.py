#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sorting_pkg.srv import select_service
# initialization
sort_pub = rospy.Publisher("/sort",String,queue_size=1)

# callback to sort the subsscribed messages
def sort_messages_CB(data):
	message = data.data
	Sorted = ''.join(sorted(message.lower()))
	print "\n\tSorted message:", Sorted
	sort_pub.publish(Sorted)

def main():
    rospy.init_node('sort_node')
    rospy.Subscriber("/hello",
    				String, 
    				sort_messages_CB)
    rospy.spin()

if __name__ == '__main__':
    main()  