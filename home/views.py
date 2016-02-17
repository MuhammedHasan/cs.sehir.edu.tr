from django.shortcuts import render, get_object_or_404
from home.models import *
from counter import Countur


def index(request):
    return render(request, 'index.html',
                  {
                      'slider': Project.get_project_in_slider(),
                      'faculty': FacultyMember.by_fix_three(),
                      'news': NewsEvent.get_last_six_by_three(),
                      'numbers': OtherText.objects.get(title='cs in numbers'),
                      'program': Program.objects.all()
                  })


def about(request):
    return render(request, 'about.html', {
        'other': OtherText.objects.get(title='About')
    })


def people(request):
    return render(request, 'people.html', {
        'faculty': FacultyMember.overview_by_three()
    })


def profile(request, id, first_name, last_name):
    faculty = FacultyMember.get_profile_information(id, first_name, last_name)
    return render(request, 'profile.html', {
        'faculty': faculty,
        'inves_projects': faculty.investigator.order_by('-end_date').all(),
        'research_projects': faculty.project_set.order_by('-end_date').all(),
        'flat_pub': faculty.publication_set.order_by('-year').all(),
        'citetion_pub': faculty.publication_set.order_by(
            '-citetion_count').all(),
        'year_pub': FacultyMember.get_publications_grouped_by_year(faculty),
        'type_pub': FacultyMember.get_publications_grouped_by_type(faculty),
        'counter': Countur()
    })


def programs_overview(request):
    return render(request, 'programsOverview.html', {
        'graduate': Program.objects.filter(type_of="Graduate").all(),
        'undergraduate': Program.objects.filter(type_of="Undergraduate").all()
    })


def research(request):
    return render(request, 'research.html', Project.get_all_project_by_type())


def research_group(request):
    return render(request, 'researchGroup.html', {
        'group': ResearchGroup.objects.order_by('name').all()
    })


def news_events_overview(request):
    return render(request, 'newsEventsOverview.html', {
        'news': NewsEvent.overview_by_three()
    })


def news_event(request, id):
    return render(request, 'newsEvent.html', {
        'news': get_object_or_404(NewsEvent, id=id)
    })


def industrial_relations(request):
    return render(request, 'industrial.html', {
        'industrial': IndustrialRelations.by_tree()
    })
