import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from gitTogether.db import get_db

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/new', methods=('GET', 'POST'))
def new():
	if request.method == 'POST':
		text = request.form['text']
		db = get_db()
		error = None
		
		if not text:
			error = "Body is required."
		elif db.execute(
			'SELECT id FROM test WHERE text = ?', (text,)
		).fetchone() is not None:
			error = 'Body {} must be unique.'.format(text)
			
		if error is None:
			db.execute(
				'INSERT INTO test (text) VALUES (?)',
				(text)
			)
			db.commit()
			return redirect(url_for('test.new'))
			
		flash(error)
	return render_template('test/new.html')