import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midtm_kr = [midtm for (midtm, _) in class_kr]
    final_kr = [final for (_, final) in class_kr]
    total_kr = [40 / 125 * midtm + 60 / 100 * final for (midtm, final) in class_kr]
    midtm_en = [midtm for (midtm, _) in class_en]
    final_en = [final for (_, final) in class_en]
    total_en = [40 / 125 * midtm + 60 / 100 * final for (midtm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.scatter(midtm_kr, final_kr, color='red', label='Korean' )
    plt.scatter(midtm_en, final_en, color='blue', label='English', marker='+')
    plt.grid(True)
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.xlabel("Midterm scores")
    plt.ylabel("Final scores")
    plt.legend()
    plt.savefig('C:/Users/user/Desktop/class_score_scatter.png')
    plt.show()

    # TODO) Plot total scores as a histogram
    plt.hist(total_kr,bins=20, range=(0,100), label='Korean', color='red', alpha=0.3)
    plt.hist(total_en,bins=20, range=(0,100), label='English', color='blue', alpha=0.3)
    plt.xlim([0, 100])
    plt.xlabel("Total scores")
    plt.ylabel("The number of students")
    plt.legend()
    plt.savefig('C:/Users/user/Desktop/class_score_hist.png')
    plt.show()