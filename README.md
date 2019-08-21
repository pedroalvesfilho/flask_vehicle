2019-07-22
----------

Original work from:
git clone https://github.com/ruiblaese/udacity-fsnd-project-item-catalog


### flask_vehicle
https://github.com/pedroalvesfilho/flask_vehicle.git


- [Create a new repository on GitHub](https://help.github.com/en/articles/creating-a-new-repository). 

1. [Create New Repository](https://help.github.com/en/articles/creating-a-new-repository) 
   drop-down: + ***top right corner***
https://github.com/pedroalvesfilho/flask_vehicle.git

### From github
…or create a new repository on the command line
echo "# flask_vehicle" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/pedroalvesfilho/flask_vehicle.git
git push -u origin master
--
git add --all
git commit -m "2019-08-21 20:00"
git push origin master
  
…or push an existing repository from the command line
git remote add origin https://github.com/pedroalvesfilho/flask_vehicle.git
git push -u origin master

…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

---

After created repository:
2. Open Git Bash

3. cd flask_vehicle

4. Initialize the local directory as a Git repository.
$ git init

5. Add the files in your new local repository. This stages them for the first commit.
$ git add .
# Adds the files in the local repository and stages them for commit. 
  To unstage a file, use 'git reset HEAD YOUR-FILE'.
  $ git reset HEAD README-orig.md   # To no commit ?!

6. Commit the files that you've staged in your local repository.
$ git commit -m "First commit"
# Commits the tracked changes and prepares them to be pushed to a remote repository.
  To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

7. At the top of your GitHub repository's "Quick Setup" page, click <= to copy the remote repository URL.
   https://github.com/pedroalvesfilho/flask_vehicle.git

8. In the Command prompt, [add the URL for the remote repository](https://help.github.com/en/articles/adding-a-remote) 
   where your local repository will be pushed.
$ git remote add origin <remote repository URL> <=  https://github.com/pedroalvesfilho/flask_vehicle.git
# Sets the new remote
$ git remote -v
# Verifies the new remote URL


9. [Push the changes](https://help.github.com/en/articles/pushing-commits-to-a-remote-repository/) in your local 
   repository to GitHub.
$ git push origin master
# Pushes the changes in your local repository up to the remote repository you specified as the origin


---


https://flask.palletsprojects.com/en/1.1.x/cli/
Use:
$ export FLASK_APP=application.py
$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

$ export FLASK_RUN_PORT=8000   # 
Setting Command Options
Click is configured to load default values for command options from environment variables. 
The variables use the pattern FLASK_COMMAND_OPTION. For example, to set the port for the run command, 
instead of flask run --port 8000:

$ export FLASK_RUN_PORT=8000
$ flask run
 * Running on http://127.0.0.1:8000/
These can be added to the .flaskenv file just like FLASK_APP to control default command options.

  

Or,
$ python application.py

-------------------

Create database on PostgreSQL:

(venv2) flask_vehicle $
(venv2) flask_vehicle $ psql -U postgres -W
Senha para usuário postgres:
psql (10.9)
AVISO: página de código do Console (850) difere da página de código do Windows (1252)
         caracteres de 8 bits podem não funcionar corretamente. Veja página de
         referência do psql "Notes for Windows users" para obter detalhes.
Digite "help" para ajuda.

postgres=# CREATE DATABASE  catalog WITH OWNER pedro;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE catalog TO pedro;
GRANT
postgres=#
postgres=#
postgres=# \c catalog
AVISO: página de código do Console (850) difere da página de código do Windows (1252)
         caracteres de 8 bits podem não funcionar corretamente. Veja página de
         referência do psql "Notes for Windows users" para obter detalhes.
Você está conectado agora ao banco de dados "catalog" como usuário "postgres".
catalog=#
catalog=#  REVOKE ALL ON SCHEMA public FROM public;
REVOKE
catalog=#
catalog=# GRANT ALL ON SCHEMA public TO pedro;
GRANT
--------------------
(venv2) flask_vehicle $ python catalog.wsgi
Database file created...
Populated database with some rows...
(venv2) flask_vehicle $
----
