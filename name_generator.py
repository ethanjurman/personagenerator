import random

def read_names(name_file):
    return [name_line.split()[0] for name_line in open(name_file, 'r')]

SURNAMES = read_names('dist.all.last.txt')
MALE_NAMES = read_names('dist.male.first.txt')
FEMALE_NAMES = read_names('dist.female.first.txt')

# returns tuple of first and last name
def get_name(gender=None):
    if gender not in {'male', 'female'}:
        gender = 'male' if random.random() > 0.5 else 'female'
    return (
        get_random(MALE_NAMES if gender == 'male' else FEMALE_NAMES),
        get_random(SURNAMES)
    )

def get_random(array):
    return array[int(len(array)*random.random())]

print(get_name())
print(get_name())
print(get_name('male'))
print(get_name('female'))
