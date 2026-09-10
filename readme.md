
.....still missing endpoints


to instal the program run the following commends in this specific order 

git clone https://github.com/ikubi2020-sketch/city_weather.git

backend setup : go to backend dir and run the following

python -m venv .venv
.venv\Scripts\activate
pip install -r  Requirements.txt

to run program backend use => uvicorn main:app --reload 

frontend setup : go to frontend dir and run the following

npm i

to run program frontend use => npm run dev



THE PREPUCE OF THE PROGRAM IS AS FOLLOW :

    in general an app that gives people the ability to get the wether and specific details about requested cites or compare between tow cites 
    the program requesting a uniq user name which alow to respond immediately  with a default city details 
    it also allow to maintain a list of favorite cites and present there current details 

STRUCTURE :
    the program is divided to frontEnd  and and backEnd
    the frontEnd is build with "react" and "TypeScript"
    it contains 7 screens . which show and request the required details 
    it also contains the use name in storage 
    the back is build using "python" 
    it contains 4 layers , server middleware routes and service.
    information of favorite cites is being store in local file
    information is being requested from Open-Meteo 




