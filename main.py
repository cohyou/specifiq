import uuid
import subprocess
import io
from flask import Flask, request, render_template, redirect
from model import query_db

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/actors')
def actors():
    sql = 'SELECT * FROM actors;'
    actors = [r['label'] for r in query_db(sql)]
    return render_template('actors.html', actors=actors)

@app.route('/actors', methods=['POST'])
def add_actor():

    sql = 'INSERT INTO actors (label) VALUES (?);'
    print(request.form)
    query_db(sql, (request.form['label'],))
    return redirect('actors')

@app.route('/requirements')
def requirements():
    sql = 'SELECT * FROM requirements;'
    requirements = [r['note'] for r in query_db(sql)]
    return render_template('requirements.html', requirements=requirements)

@app.route('/sample_plantuml/<image_file_name>', methods=['GET', 'POST'])
def get_sample_plantuml(image_file_name):

    image_name = image_file_name + '.png'
    token = str(uuid.uuid4())

    if not 'view_only' in request.args or request.args['view_only'] != "1":

        # 試しにアクター一覧を出してみる
        sql = 'SELECT * FROM actors;'
        actors = [f"actor {r['label']}\n" for r in query_db(sql)]
        actors_txt = ''
        for actor in actors:
            actors_txt += actor

        if image_file_name == 'sample':
            # PlantUML動作確認用のテキスト
            src_path = 'plantuml/sample.pu'
        else:
            src_template = f'''
            @startuml
            left to right direction
            {actors_txt}
            @enduml
            '''
            src_path = 'plantuml/'+image_file_name+'.pu'
            with open(src_path, 'w') as f:
                f.write(src_template)

        in_txt = open(src_path, 'r')

        with open('static/images/' + image_name, 'w') as b:
            popen = subprocess.Popen(['plantuml', '-p'], stdin=in_txt, stdout=b)
            stdout_data, stderr_data = popen.communicate()

    return render_template('image.html', imagename=image_name, token=token)


app.run()
