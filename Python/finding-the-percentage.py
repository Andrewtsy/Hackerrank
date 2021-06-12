if __name__ == '__main__':
    from statistics import mean
    
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = round(mean(student_marks[query_name]), 2)
    print('%.2f'%average)
    
