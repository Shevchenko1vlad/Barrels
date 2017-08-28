from django.shortcuts import render, redirect

from barrelsite.barrels_file import *


def index(request):
    sect_id = request.GET.get('section_number')
    if request.GET.get('section_number'):
        return redirect(sect, sect_id)
    return render(request, 'barrelsite/index.html', {
        "enum_upper": mainFactory.getEnumUpper(),
        "enum_lower": mainFactory.getEnumLower()
    })


def sect(request, sect_id):
    set_id = request.GET.get('set_id')
    if set_id:
        return redirect(sett, sect_id=sect_id, set_id=set_id)
    return render(request, 'barrelsite/sect1.html', {
        'barrels': mainFactory.getSection(int(sect_id)).getSets(),

    })


def sett(request, sect_id, set_id):
    table_id = -1
    sel_bar = request.GET.get("selected_barrel")

    if sel_bar:
        table_id = int(sel_bar)
    return render(request, 'barrelsite/barrel_storey1.html', {
        "barrel_storey1": mainFactory.getSection(int(sect_id)).sets_l[int(set_id) - 1].getBarrels(),
        "table_id": table_id,
        "sect_id": sect_id,
        "set_id": set_id
    })
