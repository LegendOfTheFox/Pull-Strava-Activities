<h1>Overview</h1>

<p>A quick few scripts to help out some fellow athletes pull their data from Strava for further analysis.</p>

<h1>Prerequisites</h1>

<ul>
  <li>Python 3</li>
  <li>Requests</li>
</ul>

<h1>Instructions</h1>

<h2>Step 1</h2>
<p>Get Client ID & Client Secret from Strava Athlete Page on Strava.com</p>

![image](https://user-images.githubusercontent.com/8893098/148694933-0928cfb1-f312-4e66-b08d-ea786bf6c3f3.png)

<h2>Step 2</h2>
<p>Get Auth Code From, auth the App, and grab the code entry that appears in the URI.
"http://www.strava.com/oauth/authorize?client_id=46575&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read,activity:read"</p>
![image](https://user-images.githubusercontent.com/8893098/148694966-70c2bb00-4705-4824-b3f0-c34d3d1c4f79.png)

<h2>Step 3</h2>
<p>Paste that code on auth.py into the auth_code variable and run auth.py</p>

<h2>Step 4</h2>
<p>grab the Access Token that is printed and pasted into activities.py into the access_token variable</p>

<h2>Step 5</h2> 
<p>Run activities.py, note that we are just printing the raw activities as JSON, you can take this JSON and dump it into a file or drop it into a database, etc</p>
