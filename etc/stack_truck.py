def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.pop(0)
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


print(solution(2, 10, [7,4,5,6]))