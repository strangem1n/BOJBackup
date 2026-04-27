money = int(input())
tank_power, tank_fee, dps_power, dps_fee = map(int, input().split())

max_tank = money // tank_fee
rest_money = money % tank_fee
additional_dps = rest_money // dps_fee
power = max_tank * tank_power + additional_dps * dps_power
result_tank = max_tank
result_dps = additional_dps
for tank in range(max_tank, -1, -1):
    tank_num = tank
    rest_money = money - tank_num * tank_fee
    dps_num = rest_money // dps_fee
    new_power = tank_num * tank_power + dps_num * dps_power
    if new_power > power:
        power = new_power
        result_tank = tank_num
        result_dps = dps_num

print(result_tank, result_dps)