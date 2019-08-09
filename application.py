from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalogappdb_setup import Base, Team, Player

app = Flask(__name__)       # create instance of class with name of application

engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/teams/') #url for teams and latest handful of players added
def get_teams():
    #teams = session.query(Team)
    #latest_players = session.query(Player).fetchmany(5)
    return 'This route will return all teams and latest players'

@app.route('/teams/<team_name>/')
def get_team_name(team_name):
    # team = session.query(Team).filter_by(name=team_name).one()
    return 'This route will return specific team with brief bio and players when name provided.'

@app.route('/teams/<int:team_id>/')
def get_team(team_id):
    #team = session.query(Team).filter_by(id=team_id).one()
    #latest_players = session.query(Player).fetchmany(5)
    return 'This route will return specific team with brief bio and players when id provided.'
    #return render_template('teams.html', teams=teams, latest_players=latest_players)

@app.route('/teams/<team_name>/<int:player_id>/')
@app.route('/teams/<team_name>/<player_name>/')
def get_player(player_id, player_name):
    return 'This route will return specific player photo and bio when name or id provided.'

if __name__ == '__main__':
    app.secret_key = 'no_password'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
