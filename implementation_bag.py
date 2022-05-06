import rosbag

bag_initial = rosbag.Bag('initial.bag')
bag_one_step_mapping = rosbag.Bag('one_step_mapping.bag')
is_running_mapping = bool(1)

for topic, msg, t in bag_initial.read_messages(topics=['bebop']):
    print(msg)
bag_initial.close()

while is_running_mapping:
    for topic, msg, t in bag_one_step_mapping.read_messages(topics=['bebop']):
        print(msg)
    is_Defined_continue = bool(0)
    while not is_Defined_continue:  
    
        option_continue = str(raw_input("Do you want map a next lateral step? (S/N)."))
        print(option_continue)
        if option_continue == "S":
            is_Defined_continue = bool(1)
            print("Mapping next lateral step")
        if option_continue == "N":
            is_Defined_continue = bool(1)
            is_running_mapping = bool(0)
            print("Exit!")
bag_one_step_mapping.close()


