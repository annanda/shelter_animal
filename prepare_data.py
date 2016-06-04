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

            outcome_subtype = []
            for i, row in enumerate(exemples):
                if i != 0:
                    xi = []
                    xi.append(outcome_subtype(row[2]))
                    # xi.append(row[3])
                    # xi.append(row[4])
                    # xi.append(row[5])
                    # xi.append(row[6])
                    # xi.append(row[7])
                    self.y.append(self.get_classification(row[1]))
                    # self.x.append(xi)

    def get_classification(self, name):

        classifier = {
            'Return_to_owner': 0,
            'Euthanasia': 1,
            'Adoption': 2,
            'Transfer': 3,
            'Died': 4
        }
        return classifier[name]

    def outcome_subtype(self, name):

        classifier = {
            'Suffering': 0,
            'Foster': 1,
            'In Foster': 1,
            'Partner': 2,
            'Offsite': 3,
            'SCRP': 4,
            'Aggressive': 5,
            'Behavior': 6,
            'Medical': 7,
            'Rabies Risk': 8,
            'In Kennel': 9,
            'Enroute': 10,
            'At Vet': 11,
            'In Surgery': 12,
            'Barn': 13,
            'Court/Investigation': 14,
        }
        return classifier[name]


cleaned = Clean('train.csv')