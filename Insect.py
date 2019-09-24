import time


class Insect:
    comparison_counter = 0
    swap_counter = 0

    def __init__(self, name, speed, weight):
        self.name = name
        self.speed = speed
        self.weight = weight

    def __del__(self):
        pass

    def __str__(self):
        return ('Name of insect ' + self.name + ', speed = {0} metres per second, weight = {1} grams.').format(
            self.speed, self.weight)



def insertion_sort_decrease_speed(insects):
    comparison_counter = 0
    swap_counter = 0
    for number in range(1, len(insects)):
        current_insect = insects[number]
        previous_number = number - 1
        comparison_counter += 1
        while previous_number >= 0 and current_insect > insects[previous_number]:
            comparison_counter += 1
            insects[previous_number + 1] = insects[previous_number]
            previous_number -= 1
        insects[previous_number + 1] = current_insect
        swap_counter += 1
    print('Comparisons : %i' % comparison_counter)
    print('Swaps: %i' % swap_counter)
    return insects

comparison_counter = 0
swap_counter = 0

def partition(insects, start, last):
    lower = start
    bigger = last
    pivot = insects[last]
    for number in range(start, last):
        Insect.comparison_counter += 1
        if insects[number] > pivot:
            Insect.comparison_counter += 1
            insects[lower], insects[number] = insects[number], insects[lower]
            Insect.swap_counter += 1
            lower += 1
        if insects[number] < pivot:
            Insect.comparison_counter += 1
            insects[number], insects[bigger] = insects[bigger], insects[number]
            Insect.swap_counter += 1
            bigger -= 1
    if lower == bigger:
        Insect.comparison_counter += 1
        pivot = lower
    return pivot


def quick_sort_decrease_weight(insects, start, end):
    pivot = partition(insects, start, end)
    Insect.comparison_counter += 1
    if start < end:
        quick_sort_decrease_weight(insects, start, pivot - 1)
        quick_sort_decrease_weight(insects, pivot + 1, end)
    return insects


def print_info(insects):
    for number in range(0, len(insects) - 1):
        print(str(insects[number]))


ant = Insect('Ant', 0.7, 170)
bee = Insect('Bee', 0.2, 250)
beetle = Insect('Beetle', 0.3, 220)
butterfly = Insect('Butterfly', 0.4, 300)
ladybug = Insect('Ladybug', 0.1, 200)
mosquito = Insect('Mosquito', 2, 180)
insects = [ant, bee, beetle, butterfly, ladybug, mosquito]
print('Unsorted insects:')
print()
print_info(insects)
print()
insects_speed = [ant.speed, bee.speed, beetle.speed, butterfly.speed, ladybug.speed, mosquito.speed]
print('Insects sorted by speed(decrease) -- insertion sort')
print()
start_insertion = time.perf_counter()
print(insertion_sort_decrease_speed(insects_speed))
end_insertion = time.perf_counter()
time_insertion = (end_insertion - start_insertion)
print('Time for insertion sort(ns):')
print(time_insertion)
print()
print_info(insects)
print()
insects_weight = [ant.weight, bee.weight, beetle.weight, butterfly.weight, ladybug.weight, mosquito.weight]
print('Insects sorted be weight(decrease) -- quick sort')
print()
start_quick = time.perf_counter()
print(quick_sort_decrease_weight(insects_weight, 0, len(insects_weight) - 1))
end_quick = time.perf_counter()
time_quick = (end_quick - start_quick)
print('Time for quick sort(ns):')
print(time_quick)
print('Comparisons : %i' % Insect.comparison_counter)
print('Swaps: %i' % Insect.swap_counter)
print()
print_info(insects)
