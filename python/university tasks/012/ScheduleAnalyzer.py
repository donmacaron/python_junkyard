import datetime as dt
import re



class ScheduleItem:
    def __init__(self, day_name, time, subject, prof):
        self.day_name = day_name
        self.time = time
        self.subject = subject
        self.prof = prof
    def __str__(self):
        return '%s\n%s\n%s\n%s\n' % (self.day_name, self.time,
                                     self.subject, self.prof)


with open('schedule.txt', 'r') as myfile:
    data = myfile.read()

def data_preparation(data):
    days = re.split('MON|TUE|WED|THU|FRI|SAT', data)
    day_names= ('', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
    prof = set() # список преподавателей
    subjects = set() # список предметов
    schedule = []
    # Заполняем информацией списки преподавалей и предметов
    i = 0
    for day in days:
        for x in re.findall(r'\b[a-z]+\s*[a-z]+', day):
            subjects.add(x)
        for x in re.findall(r'\b[A-Z][a-z]*\s[A-Z].[A-Z].', day):
            prof.add(x)
        lesson_data = []
        lesson_data.append(re.split(r'\n', day))
        for x in lesson_data:
            for y in x:
                yy = y.split('\t')
                if len(yy) == 3:
                    schedule.append(ScheduleItem(day_names[i], yy[0], yy[1], yy[2]))
        # day = day_names[i] + day
        if i <= len(day_names):
            i += 1
    return {'schedule':schedule, 'prof':prof, 'subjects':subjects}

def calc_time(schedule, task=1):
    hours = []
    day_name = []
    for i in schedule:
        data = i.time.split('-')

        # start of the lesson
        start_time = dt.datetime.strptime(data[0], '%H:%M')
        # end of the lesson
        end_time = dt.datetime.strptime(data[1], '%H:%M')

        hours.append(end_time - start_time)
        day_name.append(i.day_name)
    if task == 1:
        return {'hours': hours, 'days': day_name}
    elif not task == 1:
        return hours


def total_time(schedule, show = 0):
    total_hours = {}
    temp = calc_time(schedule, 1)
    hours = temp['hours']
    day = temp['days']
    j = 0
    for i in schedule:
        if day[j] in total_hours:
            total_hours[day[j]] = total_hours[day[j]] + hours[j]
        else:
            total_hours[day[j]] = hours[j]
        j += 1

    if show:
        print('-==### Total hours of lessons  ###==-')
        for x, y in total_hours.items():
            print('\t   %s: %s' % (x, y))
        print('-==### Total hours of lessons  ###==-\n')
    return total_hours


def subject_time(schedule, show = 0):
    subjects_hours = {}
    hours = calc_time(schedule, 2)
    j = 0
    for i in schedule:
        if i.subject in subjects_hours:
            subjects_hours[i.subject] += hours[j]
        else:
            subjects_hours[i.subject] = hours[j]
        j += 1
    if show:
        print('-==### Total hours of subjects ###==-')
        for k, v in sorted(subjects_hours.items(), key=lambda p: p[1], reverse=True):
            print('\t %s: %s' % (k, v))
        print('-==### Total hours of subjects ###==-\n')

def prof_time(schedule, show = 0):
    prof_hours = {}
    hours = calc_time(schedule, 2)
    j = 0
    for i in schedule:
        if i.prof in prof_hours:
            prof_hours[i.prof] += hours[j]
        else:
            prof_hours[i.prof] = hours[j]
        j += 1
    if show:
        print('-==## Total hours of professeur ##==-')
        for k, v in sorted(prof_hours.items(), key=lambda p: p[0], reverse=False):
            print('\t %s: %s' % (k, v))
        print('-==## Total hours of professeur ##==-')



# prof = data_preparation(data)['prof']
# subj = data_preparation(data)['subjects']

schedule = data_preparation(data)['schedule']
# for x in schedule:
#     print(x)

total_time(schedule, 1)

subject_time(schedule, 1)

prof_time(schedule, 1)
# for x in schedule:
#     print(x)
