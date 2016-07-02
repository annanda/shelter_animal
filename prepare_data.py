import csv


class Clean:
    '''
    Prepare the dataset. Clen up the data.
    xi = [outcome subtype, animal type, animal sex, castration]
    '''

    x = []
    y_ = []

    def __init__(self, file_path):
        self.read_csv(file_path)

    def read_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            examples = csv.reader(csv_file, delimiter=',')

            #outcome_subtype = []
            for i, row in enumerate(examples):
                if i != 0: # ignore header
                    xi = []
                    xi.append(self.get_outcome_subtype(row[2]))
                    xi.append(self.get_animal_type(row[3]))
                    types = self.get_animal_sex(row[4])
                    # spliting the field SexuponOutcome in two
                    # one with the animal sex and other with type
                    for type in types:
                        xi.append(type)
                    xi.append(self.get_animal_age(row[5]))
                    # xi.append(row[6])
                    # xi.append(row[7])
                    self.y_.append(self.get_classification(row[1]))
                    self.x.append(xi)
        #     p = []
        #     for i, row in enumerate(examples):
        #         if i != 0 and row[5] != '': # ignore header
                    
        #     print(p)
        # exit();

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
        return classifier[name]

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
        castration, _, sex = name.partition(' ')
        
        sexCode = {
            'Male': 0,
            'Female': 1
        }.get(sex, 3);

        castrationCode = {
            'Neutered': 0,
            'Spayed': 1,
            'Intact': 3
        }.get(castration, 4)

        return [sexCode, castrationCode]

    def get_animal_age(self, name):
        if name == '': return -1
        
        how_many, period = name.split()
                    
        how_many = int(how_many)
         # remove plural
        period = period[:-1] if period.endswith('s') else period
        
        daysInPeriod = {
            'year' : 365,
            'month': 31,
            'week' : 7,
            'day'  : 1
        }.get(period)
        
        return how_many * daysInPeriod


# cleaned = Clean('train.csv')
# print(cleaned.x[:8])