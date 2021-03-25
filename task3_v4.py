def has_overlap(A_start, A_end, B_start, B_end): #вычисляем есть ли пересечение таймстампов двух входных интервалов
    latest_start = max(A_start, B_start)
    earliest_end = min(A_end, B_end)
    return latest_start <= earliest_end


def tested(times1): #рекурсивная проверка на перекрытие интервалов и их объединение(конец больше следующего начала)
    times2 = []
    
    for i in range((len(times1)-1) // 2):
        if times1[i*2+1] > times1[i*2+2]:
            times2.append(times1[i*2])
            times2.append(times1[i*2+3])
    
    return tested(times2) if times2 != [] else times1


def calc_overlaps(times1, times2): #вычисляем пересечение двух входных интервалов
    times3 = []
    
    for l1 in range(len(times1) // 2):
        for t1 in range(len(times2) // 2):
            
            if has_overlap(times1[l1*2], times1[l1*2+1],
                           times2[t1*2], times2[t1*2+1]):
                
                times3.append(max(times1[l1*2], times2[t1*2]))
                times3.append(min(times1[l1*2+1], times2[t1*2+1]))
    return times3


def appearance(intervals): #результирующая ф-я 
    
    new1 = calc_overlaps(calc_overlaps(tested(intervals['lesson']), 
                                       tested(intervals['tutor'])), 
                         tested(intervals['pupil']))
    
    sum = 0
    for n1 in range(len(new1)//2): #вычисляем продолжительность общего присутствия
        sum = sum + (new1[n1*2+1] - new1[n1*2])
        
    return sum
    

tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(tests[i]['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    