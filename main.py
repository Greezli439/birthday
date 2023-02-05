from datetime import datetime, timedelta

USERS = [{'name': 'Gianna Ross', 'birthday': '2023-02-23'}, {'name': 'Heidi King', 'birthday': '2023-02-25'}, {'name': 'Arabella Powell', 'birthday': '2023-02-26'}, {'name': 'Malia Perez', 'birthday': '2023-02-11'}, {'name': 'Selena Sanders', 'birthday': '2023-02-03'}, {'name': 'Winnefred Watson', 'birthday': '2023-03-01'}, {'name': 'Rosa Powell', 'birthday': '2023-02-12'}, {'name': 'Yasmeen Martin', 'birthday': '2023-02-18'}, {'name': 'Zayna Wright', 'birthday': '2023-02-18'}, {'name': 'Xiomara King', 'birthday': '2023-02-09'}, {'name': 'Hellen Thomas', 'birthday': '2023-02-20'}, {'name': 'Ulrika James', 'birthday': '2023-02-17'}, {'name': 'Noelle Foster', 'birthday': '2023-02-16'}, {'name': 'Victoria Howard', 'birthday': '2023-02-21'}, {'name': 'Susan Scott', 'birthday': '2023-02-07'}, {'name': 'Helen Anderson', 'birthday': '2023-02-28'}, {'name': 'Harlie Carter', 'birthday': '2023-02-07'}, {'name': 'Helen Brooks', 'birthday': '2023-02-04'}, {'name': 'Callie Green', 'birthday': '2023-02-10'}, {'name': 'Alexandra King', 'birthday': '2023-02-02'}, {'name': 'Oleen White', 'birthday': '2023-02-13'}, {'name': 'Reina Butler', 'birthday': '2023-02-09'}, {'name': 'Patience Jackson', 'birthday': '2023-02-04'}, {'name': 'Margaret Gonzales', 'birthday': '2023-02-25'}, {'name': 'Dania Wood', 'birthday': '2023-02-02'}, {'name': 'Remington Walker', 'birthday': '2023-02-07'}, {'name': 'Iver Hall', 'birthday': '2023-02-02'}, {'name': 'Grady Gonzales', 'birthday': '2023-02-04'}, {'name': 'Quang Bailey', 'birthday': '2023-02-02'}, {'name': 'Nathaniel Reed', 'birthday': '2023-02-24'}, {'name': 'Thaddeus Thompson', 'birthday': '2023-02-27'}, {'name': 'Elijah Green', 'birthday': '2023-02-03'}, {'name': 'Donovan White', 'birthday': '2023-02-22'}, {'name': 'Emery James', 'birthday': '2023-02-13'}, {'name': 'Xandros Rogers', 'birthday': '2023-02-05'}, {'name': 'Zahir Alexander', 'birthday': '2023-02-16'}, {'name': 'Levi Jones', 'birthday': '2023-02-12'}, {'name': 'Qasim Jackson', 'birthday': '2023-02-08'}, {'name': 'Wayne Reed', 'birthday': '2023-02-12'}, {'name': 'Ismael Richardson', 'birthday': '2023-02-15'}, {'name': 'Declan Wood', 'birthday': '2023-02-27'}, {'name': 'Caiden Gonzalez', 'birthday': '2023-02-05'}, {'name': 'Ulyses Jones', 'birthday': '2023-02-15'}, {'name': 'Robert Barnes', 'birthday': '2023-02-28'}, {'name': 'Cayden Long', 'birthday': '2023-02-28'}, {'name': 'Cullen Morgan', 'birthday': '2023-02-24'}, {'name': 'Marcos Bell', 'birthday': '2023-02-25'}, {'name': 'Lewis Young', 'birthday': '2023-02-26'}, {'name': 'Zack Coleman', 'birthday': '2023-02-17'}, {'name': 'Selah Martinez', 'birthday': '2023-02-03'}]


def get_birthdays_per_week():
    today = datetime.now().date()
    end_day = today + timedelta(weeks=1)
    im = {}
    for i in range(7):
        im[today + timedelta(days=i)] = []
    for i in USERS:
        j = i['birthday'].split('-')
        id = datetime(year=int(j[0]), month=int(j[1]), day=int(j[2])).date()
        if today <= id < end_day:
             im[id].append(i['name'])

    kkk = ''
    for i, (k, v) in enumerate(im.items()):
        if k.strftime('%A') == 'Saturday':
            if 0 <= i < 5:
                im[k + timedelta(days=2)].append(', '.join(v))
        elif k.strftime('%A') == 'Sunday':
            if 0 <= i < 5:
                im[k + timedelta(days=1)].append(', '.join(v))
        else:
            kkk = ', '.join(v)
            print(f'{k.strftime("%A")}: {kkk}')


if __name__ == '__main__':
    get_birthdays_per_week()
