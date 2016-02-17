from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import date
from django.db.models.functions import Substr
from itertools import groupby
from operator import itemgetter
from random import shuffle
import locale


class FacultyMember(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    phd = models.CharField(max_length=90)
    interest = models.TextField()
    email = models.EmailField()
    is_active = models.BooleanField()
    office = models.CharField(max_length=90)
    phone = models.CharField(max_length=50)
    bio = models.TextField()
    website = models.CharField(max_length=90, blank=True)
    chair = models.BooleanField()
    vice_chair = models.BooleanField()
    image = models.ImageField(blank=True, upload_to="img/profile")
    leave = models.BooleanField()
    visit = models.BooleanField()
    twitter = models.CharField(max_length=150, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)
    google_scholar = models.CharField(max_length=150, blank=True)
    DBLP = models.CharField(max_length=150, blank=True)
    CV = models.FileField(upload_to="cvs", blank=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def overview_by_three():
        # this extra sort line for turkish character issue
        locale.setlocale(locale.LC_ALL, "")
        faculty = list(FacultyMember.objects.filter(
            is_active=True).order_by('last_name').values(
            'id', 'first_name', 'middle_name', 'email', 'leave', 'last_name',
            'image', 'title', 'phd', 'interest', 'visit', 'chair').all())
        # this extra sort line for turkish character issue
        faculty = sorted(faculty, key=lambda x: x['last_name'],
                         cmp=locale.strcoll)
        return list_by_three(faculty)

    @staticmethod
    def by_fix_three():
        faculty = list(FacultyMember.objects.filter(
            is_active=True).order_by('last_name')
            .values('id', 'first_name', 'middle_name', 'email',
                    'leave', 'last_name', 'image', 'title',
                    'phd', 'interest', 'visit', 'chair').all())
        shuffle(faculty)
        return list_by_three(fix_to_three(faculty))

    @staticmethod
    def get_profile_information(id, first_name, last_name):
        return get_object_or_404(FacultyMember.objects.filter(
            pk=id,
            first_name=first_name,
            last_name=last_name
        ))

    @staticmethod
    def get_publications_grouped_by_year(faculty):
        pubs = faculty.publication_set.all()
        groubed_pubs = dict()
        for i in pubs:
            if i.year in groubed_pubs:
                groubed_pubs[i.year].append(i)
            else:
                groubed_pubs[i.year] = [i]
        return sorted(groubed_pubs.items(),
                      reverse=True,
                      key=lambda k: k[0])

    @staticmethod
    def get_publications_grouped_by_type(faculty):
        return {k: list(v) for k, v in
                groupby(faculty.publication_set.order_by('-type_of').all(),
                        lambda x: str(x.type_of))}


class Publication(models.Model):
    info = models.TextField()
    year = models.IntegerField()
    type_of = models.CharField(max_length=40)
    # Thanks to myself perfect spelling
    # correct that and migrate database
    citetion_count = models.IntegerField(default=0, null=True, blank=True)
    citetion_link = models.CharField(max_length='1000', blank=True)
    # end of thanks
    fetched_from_google_scholar = models.BooleanField(default=False)
    fetched_from_DBLP = models.BooleanField(default=False)
    author = models.ManyToManyField(FacultyMember, blank=True)

    def __unicode__(self):
        return self.info


class Project(models.Model):
    title = models.CharField(max_length=250)
    abstract = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.CharField(max_length=100)
    funding_institution = models.CharField(max_length=100)
    website = models.CharField(max_length=90, blank=True)
    poster = models.ImageField(blank=True, upload_to="img/project")
    in_spot_light = models.BooleanField()
    principal_investigator = models.ForeignKey(
        FacultyMember, related_name='investigator')
    researchers = models.ManyToManyField(FacultyMember, blank=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_project_in_slider():
        return Project.objects.filter(
            Q(in_spot_light=True) & Q(end_date__gt=date.today())
        ).order_by('-start_date').annotate(
            short_abstract=Substr('abstract', 1, 300)).values(
            'short_abstract', 'poster')

    @staticmethod
    def get_all_project_by_type():
        return {
            'ongoing': Project.objects.filter(
                end_date__gt=date.today()).order_by(
                '-start_date').select_related('principal_investigator'),
            'completed': Project.objects.filter(
                end_date__lt=date.today()).order_by(
                '-start_date').select_related('principal_investigator'),
        }


class ResearchGroup(models.Model):
    name = models.CharField(max_length=120)
    website = models.CharField(max_length=120, blank=True)
    logo = models.ImageField(blank=True, upload_to="img/logo")
    members = models.ManyToManyField(FacultyMember, blank=True)

    def __unicode__(self):
        return self.name


class NewsEvent(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    link = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    poster = models.ImageField(blank=True, upload_to="img/news")

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_last_six_by_three():
        return list_by_three(
            NewsEvent.objects.order_by('-date').values(
                'id', 'title', 'description', 'poster', 'date')[:6]
        )

    @staticmethod
    def overview_by_three():
        return list_by_three(
            NewsEvent.objects.order_by('-date').values(
                'id', 'title', 'description', 'poster', 'date'))


class Program(models.Model):
    title = models.CharField(max_length=50)
    type_of = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to="img/programs")

    def __unicode__(self):
        return self.title


class ProgramSubField(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    program = models.ForeignKey(Program, related_name='sub_set')

    def __unicode__(self):
        return self.title


class OtherText(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __unicode__(self):
        return self.title


class IndustrialRelations(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=120, blank=True)
    logo = models.ImageField(blank=True, upload_to="img/industrial")

    def __unicode__(self):
        return self.name

    @staticmethod
    def by_tree():
        return list_by_three(IndustrialRelations.objects.all())


# TODO: Put that function to better place


def list_by_three(li):
    three = []
    n_three = 0
    for i in range(len(li)):
        if i / 3 == n_three:
            three.append(list())
            n_three += 1
        three[i / 3].append(li[i])
    return three

# TODO: Hey me. You can do that with javascript when you don't feel lazy


def fix_to_three(li):
    if len(li) % 3 is not 0:
        li = li * 3
    return li


def to_three_col(li):
    div_num = (len(li) / 3)
    if len(li) % 3 == 1:
        div_num += 1
        return [
            li[0:div_num],
            li[div_num:(2 * div_num) - 1], li[(2 * div_num) - 1:]]
    elif len(li) % 3 == 2:
        div_num += 1
        return [li[0:div_num], li[div_num:2 * div_num], li[2 * div_num:]]
    return [li[0:div_num], li[div_num:2 * div_num], li[2 * div_num:]]
