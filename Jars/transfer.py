target_capacity, target_liquid, source_capacity, source_liquid  = 0, 0, 0, 0

def transfer_Liquid(P_source_capacity, P_source_liquid, P_target_capacity, P_target_liquid):
    global target_capacity, target_liquid, source_capacity, source_liquid
    # source_capacity = int(input("Enter source capacity: "))
    # source_liquid = int(input("Enter source liquid: "))
    # target_capacity = int(input("Enter target capacity: "))
    # target_liquid = int(input("Enter target liquid: "))
    target_appatite = P_target_capacity - P_target_liquid
    target_capacity = P_target_capacity
    source_capacity = P_source_capacity
 #   global target_appatite, source_capacity, source_liquid, target_liquid, target_capacity
    if target_appatite >= P_source_liquid:
        target_liquid = P_target_liquid + P_source_liquid
        source_liquid = 0
    if target_appatite < P_source_liquid:
        target_liquid = P_target_capacity
        source_liquid = P_source_liquid - target_appatite



# count = 1
# while count <= 5:
#     count = count + 1
#     transfer_Liquid(source_capacity, source_liquid, target_capacity, target_liquid, target_appatite)
#     print(f'After Transfer source liquid :{source_liquid} and after transfer target liquid : {target_liquid}')
