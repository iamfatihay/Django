from .models import Path, Student
from faker import Faker
def run():
    '''
        pip install Faker
        python manage.py shell

        from student_api.faker import run
        run()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    fake = Faker()
    # fake = Faker(["tr_TR"])

    paths = (
        "FullStack",
        "DataScience",
        "AwsDevops",
        "CyberSec",
    )
    for path in paths:
        new_path = Path.objects.create(path_name = path)
        for _ in range(100):
            Student.objects.create(path = new_path, first_name = fake.first_name(), last_name = fake.last_name(), number = fake.pyint())
    print('OK')