def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            else:
                values = [int(text) for text in line.split(',')]
                data.append(values)
    return data

def add_weighted_average(data, weight):
    for row in data:
        row.append(row[0]*weight[0] + row[1]*weight[1])

    
def analyze_data(data):
    mean = sum(data) / len(data)
    var = sum((i - mean) ** 2 for i in data) / len(data)
    data.sort()
    median = data[int(len(data)/2)]
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')

