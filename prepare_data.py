import csv


class Clean:
    '''
    Prepere the dataset. Clening up the data.
    '''

    x = []
    y_ = []

    def __init__(self, file_path):
        self.read_csv(file_path)

    def read_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            exemples = csv.reader(csv_file, delimiter=',')

            for i, row in enumerate(exemples):
                if i != 0 and i < 10:
                    xi = []
                    xi.append(row[2])
                    xi.append(row[3])
                    xi.append(row[4])
                    xi.append(row[5])
                    xi.append(row[6])
                    xi.append(row[7])
                    self.y.append(self.get_classification(row[1]))
                    self.x.append(xi)

    def get_classification(self, name):

        classifier = {
            'Return_to_owner': 0,
            'Euthanasia': 1,
            'Adoption': 2,
            'Transfer': 3,
            'Died': 4
        }
        return classifier[name]


cleaned = Clean('train.csv')