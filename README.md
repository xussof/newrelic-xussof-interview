# newrelic-xussof-interview

Idea read a file
Using split, diferenciate all words in the file
Create an array placing all groups of 3 words, we exclude symbols such as , ?, !...:
    Example: 
        Hello, how are you? Fine and how are you?
        We place in the first array the next string
        Hello how are
        In the second:
        how are you
        In the third
        are you Fine

Create another array on we read the previous array and decide which one has the most common 3 words

Executing script:


Execute:
pip install -r requirements.txt
python main.py
Place a file into app/txtfolder

docker-compose:
In order to execute using docker compose  run the next command:
docker-compose up
To force rebuild image:
docker-compose up --build
place a file in app/txtfolder



Sources: 
https://www.nltk.org/

https://stackoverflow.com/questions/49589974/how-to-get-most-common-phrases-or-words-in-python-or-r
https://thepythoncorner.com/posts/2019-01-13-how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/#step-1-import-some-stuff

