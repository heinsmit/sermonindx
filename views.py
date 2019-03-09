from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import render
from django.views import generic

from .models import SermonIndxSermons, SermonIndxSeries, SermonIndxSpeakers, SermonIndxTopics

# Create your views here.
def sermon_list_view(request):
    """
    View that displays a list of all the sermons.
    """
    sermons_list = SermonIndxSermons.objects.all().order_by("-si_date")
    paginator = Paginator(sermons_list, 5)

    page = request.GET.get('page')
    try:
        sermons = paginator.page(page)
    except InvalidPage:
        sermons = paginator.page(1)
    
    return render(
        request,
        'sermonindx/index.html',
        context={'sermons': sermons, 'num_pages': range(sermons.paginator.num_pages)},
    )

def sermon_detail_view(request, slug):
    sermon = SermonIndxSermons.objects.get(si_slug=slug)
    # speaker = SermonIndxSpeakers.objects.get(speaker_slug=sermon.si_speaker)

    return render(
        request,
        'sermonindx/sermon.html',
        context={'sermon': sermon},
    )

def speaker_list_view(request, slug):
    """
    View that displays a list of all the sermons of a speaker.
    """
    speaker = SermonIndxSpeakers.objects.get(speaker_slug=slug)
    sermons_list = SermonIndxSermons.objects.filter(si_speaker__exact=speaker.id).order_by("-si_date")

    paginator = Paginator(sermons_list, 5)

    page = request.GET.get('page')
    try:
        sermons = paginator.page(page)
    except InvalidPage:
        sermons = paginator.page(1)

    return render(
        request,
        'sermonindx/speaker_sermons_list.html',
        context={'speaker': speaker, 'sermons': sermons, 'num_pages': range(sermons.paginator.num_pages)},
    )

def sermons_by_topic_view(request, slug):
    """
    View that displays a list of sermons by topic
    """
    topic = SermonIndxTopics.objects.get(topic_slug=slug)
    sermons_list = SermonIndxSermons.objects.filter(si_topic__exact=topic.id)

    paginator = Paginator(sermons_list, 5)

    page = request.GET.get('page')
    try:
        sermons = paginator.page(page)
    except InvalidPage:
        sermons = paginator.page(1)

    return render(
        request,
        'sermonindx/topic_sermons_list.html',
        context={'topic': topic, 'sermons': sermons, 'num_pages': range(sermons.paginator.num_pages)},
    )

def series_sermons_view(request, slug):
    """
    View for displaying all the sermons in a series
    """
    series = SermonIndxSeries.objects.get(series_slug=slug)
    sermons_list = SermonIndxSermons.objects.filter(si_series__exact=series.id).order_by('-si_date')

    paginator = Paginator(sermons_list, 5)

    page = request.GET.get('page')
    try:
        sermons = paginator.page(page)
    except InvalidPage:
        sermons = paginator.page(1)

    return render(
        request,
        'sermonindx/series_sermons_list.html',
        context={'series': series, 'sermons': sermons, 'num_pages': range(sermons.paginator.num_pages)}
    )