import random
from datacenter.models import Schoolkid, Chastisement, Mark, Commendation, Lesson
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

COMPLIMENTS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]

def get_schoolkid_by_name(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist:
        pass
    except MultipleObjectsReturned:
        pass


def create_commendation(child_name, subject_title):
    schoolkid = get_schoolkid_by_name(child_name)
    if schoolkid:
        lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_title
        ).order_by('-date').first()
        compliment = random.choice(COMPLIMENTS)
        commendation = Commendation.objects.create(
            text=compliment,
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
        )


def remove_chastisements(child_name):
    schoolkid = get_schoolkid_by_name(child_name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()


def fix_marks(child_name):
    schoolkid = get_schoolkid_by_name(child_name)  
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    bad_marks.update(points=5)



      
