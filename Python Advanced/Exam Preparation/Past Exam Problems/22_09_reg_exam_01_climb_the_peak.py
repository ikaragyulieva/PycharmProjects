# Alex is a vlogger and he wants to make videos of climbing the five highest peaks in Pirin mountain in just one week.
# He will take his video set, a tent, and his backpack to the mountain. The backpack fits food portions for one week,
# exactly. His daily stamina is also limited. Your task is to trace his adventure and create a post for his profile
# @alaroundtheworld, at the end of the journey.
# You will have to keep information for all the conquered peaks if any.
# Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
# First, you will be given a sequence of numbers, representing the quantities of the daily portions of food
# supplies in his backpack.
# Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he will
# have at his disposal for the next seven days.
# You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina. He will
# start climbing from the first peak in the table below to the last one.
# •	If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below,
# it means that the peak is conquered. In this case, you should remove both quantities from the sequences and
# continue with the next ones towards the next peak.
# •	If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak remains
# unconquered. You should remove both quantities from the sequences. Alex will have to sleep in his tent.
# On the next day, he will try the same peak once again.
# Alex will try to conquer as many peaks as he can in seven days.If he manages to climb all the peaks, the journey ends
# and the output is printed on the Console.
# Finally, print on the Console all the conquered peaks( in the order of climbing).
# Input
# •	On the first line, you will receive the food portions, separated by a comma and a single space (', ').
# •	On the second line, you will receive the stamina, separated by a comma and a single space (', ').
# Output
# •	On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
# o	If he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
# o	If he didn't manage to climb all peaks:
# "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
# •	Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
# "Conquered peaks:
# {peak1}
# {peak2}
# …
# {peakn}"
# o	If there are no concurred peaks, do NOT print this message.
# Constraints
# •	All given numbers will be valid integers in the range [0…100].

from collections import deque

daily_portions = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))
conquered_peaks = []
day = 1

peaks_difficulty = deque([('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not daily_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    current_portion = daily_portions.pop()
    current_stamina = stamina.popleft()
    daily_energy = current_stamina + current_portion
    current_peak = peaks_difficulty[0]
    if daily_energy >= current_peak[1]:
        conquered_peaks.append(current_peak[0])
        peaks_difficulty.popleft()

    day += 1
    # if daily_energy >= 100:
    #     conquered_peaks.append('Banski Suhodol')
    # elif daily_energy >= 90:
    #     conquered_peaks.append('Kutelo')
    # elif daily_energy >= 80:
    #     conquered_peaks.append('Vihren')
    # elif daily_energy >= 70:
    #     conquered_peaks.append('Kamenitza')
    # elif daily_energy >= 60:
    #     conquered_peaks.append('Polezhan')

# if len(conquered_peaks) == 5:
#     print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
# else:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")


if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))


# --- Tests: ---
# Test1:
# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2
#
# Test2:
# 10, 20, 34, 26, 12, 10, 45
# 30, 28, 17, 17, 13, 10, 10
#
# --- Outputs: ---
# Test1:
# Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
# Conquered peaks:
# Vihren
# Kutelo
# Banski Suhodol
# Polezhan
# Kamenitza
#
# Test2:
# Alex failed! He has to organize his journey better next time -> @PIRINWINS
