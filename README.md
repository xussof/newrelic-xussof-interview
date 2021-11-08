# newrelic-xussof-interview

<h2 p align="left">Project Description</p></h1>

A tool used to read files placed on app/txtfolder, to retrieve the 100 most used 3 word sentence, see next example:

    Example text:
    Hello how are you?
    Fine thank you
    How are you?

    Result:
    how are you, 2
    fine thank you, 1
    Idea read a file

#### How it works:

We use the whatchdog library in order to notify when a new file has been placed, and also to notify when the file has been removed once the code has found the common words.

In order to avoid repositing a text test file, we autogenerate a file while doing test. And we include random words using random_work library into the text so we can easily diferenciate between the correct lines

#### Executing script:

##### Execute on command line:
pip install -r requirements.txt
python main.py
Place a file into app/txtfolder

##### docker-compose:
In order to execute using docker compose  run the next command:
docker-compose up
To force rebuild image:
docker-compose up --build
place a file in app/txtfolder

##### To deploy using helm:
kubectl create namespace common-words
cd helm
helm upgrade common-words-app . -i -n common-words

#### Work to do in the future:
- Create a frontend on which I could upload files in order to trigger the observer and return the list of words.
- Place some restrictions in order to only allow certain types of files
- Settup a better deployment chart in order to set Hardware capacities

### Sources: 
https://www.nltk.org/

https://stackoverflow.com/questions/49589974/how-to-get-most-common-phrases-or-words-in-python-or-r

https://thepythoncorner.com/posts/2019-01-13-how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/#step-1-import-some-stuff

**Sergi Cañas**

- [Profile](https://github.com/xussof "Sergi Cañas")
- [Email](mailto:xussof@gmail.com?subject=Hi% "Hi!")
- [Website](https://cloudsolute.net "Welcome")