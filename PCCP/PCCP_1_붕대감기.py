def attack(health, damage, max_health):
    """공격을 받으면 체력 감소, 연속 성공 카운트 초기화"""
    health -= damage
    if health <= 0:
        return -1, 0  # 체력이 0 이하가 되면 즉시 사망
    return health, 0  # 체력 감소 후 연속 성공 횟수 초기화


def recover(health, count, bandage, max_health):
    """공격이 없을 때 체력 회복 및 연속 성공 횟수 증가"""
    health += bandage[1]  # 초당 회복량 적용
    count += 1  # 연속 성공 횟수 증가

    if count == bandage[0]:  # 연속 성공 시 추가 회복
        health += bandage[2]
        count = 0  # 연속 성공 횟수 초기화

    health = min(health, max_health)  # 최대 체력 초과 방지
    return health, count


def solution(bandage, health, attacks):
    max_health = health  # 최대 체력 저장
    count = 0  # 연속 붕대 감기 성공 횟수
    attack_index = 0  # 공격 리스트 인덱스
    time = 1  # 현재 시간 (1초부터 시작)

    while time <= attacks[-1][0]:  # 마지막 공격 시간까지 반복
        if attack_index < len(attacks) and attacks[attack_index][0] == time:
            # 공격 시간이 오면 attack() 호출
            health, count = attack(health, attacks[attack_index][1], max_health)
            attack_index += 1  # 다음 공격으로 이동

            if health == -1:  # 체력이 0 이하이면 즉시 종료
                return -1
        else:
            # 공격이 없으면 recover() 호출
            health, count = recover(health, count, bandage, max_health)

        time += 1  # 시간 증가

    return health  # 모든 공격이 끝난 후 남은 체력 반환


# def attack(health, attacks, time):
#     for attack in attacks:
#         if health - attack[1] <= 0:
#             health = 0
#             return health, -1
#         health -= attack[1]  # 공격 데미지
#
#     return health, time + 1
#
#
# def recover(health, bandage, max_health, time, count):
#     if health == max_health:
#         return health, time + 1
#     if count == bandage[0]:
#         health += bandage[2]
#     health += bandage[1]
#     count += 1
#
#     return health, time + 1
#
#
# def solution(bandage, health, attacks):
#     playtime = attacks[-1][0]
#     max_health = health
#     time = 0
#
#     for i in range(playtime):
#         time += 1
#         for a in attacks:
#             if health <= 0:
#                 return -1
#             if a[0] == time:
#                 health, time = attack(health, attacks, time)
#             else:
#                 health, time = recover(health, bandage, max_health, time, count=0)
#     return health