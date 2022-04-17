from flask import Blueprint, render_template, request, redirect, session
# from flask_paginate import Pagination, get_page_parameter
import models.history as his

bp = Blueprint('history', __name__, url_prefix='/history')
history_service = his.HistoryService()


@bp.route('/')
def write_history():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        id = session['id']
        hist = history_service.getHistory(id)
        return render_template('history/list.html', hist=hist)


@bp.route('/add')
def add_form():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        stlst = history_service.getStationList()
        return render_template('history/add.html', stlst=stlst)


@bp.route('/add', methods=['POST'])
def add_history():
    member_id = session['id']
    rent_date = request.form['rent_date']
    rent_station = request.form['rent_station']
    return_station = request.form['return_station']
    rent_time = request.form['rent_time']
    return_time = request.form['return_time']
    distance = request.form['distance']

    h = his.History(member_id=member_id, rent_date=rent_date, rent_station=rent_station,
                    return_station=return_station, rent_time=rent_time, return_time=return_time, distance=distance)
    history_service.writeHistory(h)
    return redirect('/history')
