import requests
from flask import render_template, flash, redirect,url_for,session,abort
from app import app
from .forms import SigninForm

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = SigninForm()
	resp=[]
	if form.validate_on_submit():
		username=form.idu.data
		v='<a class="repo-list-stat-item tooltipped tooltipped-s" href="/'+username+'/'
		url='https://github.com/'+username+'?tab=repositories' 
		r =requests.get(url)
		stored=[]
		count=""
		decode=r.text
		for i in decode:
			count+=i
			if i=='\n':
				stored.append(count)
				count=""
		for f in stored:
			if v in f:
				h=f.find("/stargazers")
				if f.find("/stargazers") == h and '/network' not in f: 			
					resp.append(f[(4+len(v)):h])
	return render_template('index.html',title='Home',form=form,resp=resp)
