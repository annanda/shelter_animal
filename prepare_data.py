import csv


class Clean:
    '''
    Prepare the dataset. Clen up the data.
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
                    xi.append(self.get_outcome_subtype(row[2]))
                    xi.append(self.get_animal_type(row[3]))
                    xi.append(self.get_animal_sex(row[4]))
                    # xi.append(row[5])
                    # xi.append(row[6])
                    # xi.append(row[7])
                    self.y_.append(self.get_classification(row[1]))
                    self.x.append(xi)

    def get_classification(self, name):

        classifier = {
            'Return_to_owner': 0,
            'Euthanasia': 1,
            'Adoption': 2,
            'Transfer': 3,
            'Died': 4
        }
        y_i = [0, 0, 0, 0, 0]
        y_i[classifier[name]] = 1
        return y_i

    def get_outcome_subtype(self, name):

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
            '': 15
        }
        return classifier[name]

    def get_animal_type(self, name):

        classifier = {
            'Dog': 0,
            'Cat': 1
        }
        return classifier[name]

    def get_animal_sex(self, name):
        types = name.split()

        sex = {
            'Male': 0,
            'Female': 1,
            'Unknown': 3
        }

        type_classifier = {
            'Neutered': 0,
            'Spayed': 1,
            'Intact': 3,
            'Unknown': 4
        }
        classifier = [3, 4]
        for type in types:
            if type in sex:
                classifier[0] = sex[type]
            if type in type_classifier:
                classifier[1] = type_classifier[type]
        return classifier


cleaned = Clean('train.csv')
print(cleaned.x[:8])