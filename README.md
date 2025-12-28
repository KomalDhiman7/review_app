<h1>Review API (Flask + SQLite)</h1>

<p>
A backend REST API that allows users to register, add reviews for places,
search places by rating, and view detailed place information.
</p>

<hr/>

<h2>Tech Stack</h2>
<ul>
  <li>Python (Flask)</li>
  <li>SQLite</li>
</ul>

<hr/>

<h2>Features</h2>
<ul>
  <li>User registration with token-based authentication</li>
  <li>Add reviews for places (one review per user per place)</li>
  <li>Automatic place creation if not already present</li>
  <li>Search places by name (full / partial) and minimum rating</li>
  <li>View place details with average rating and ordered reviews</li>
  <li>Sample data seeding script</li>
</ul>

<hr/>

<h2>Setup</h2>

<pre>
pip install flask
python init_db.py
python seed_data.py
python app.py
</pre>

<hr/>

<h2>API Endpoints</h2>

<h3>Register User</h3>
<pre>
POST /register
</pre>
<pre>
{
  "name": "Komal",
  "phone": "9999999999"
}
</pre>

<h3>Add Review</h3>
<pre>
POST /reviews
Authorization: &lt;token&gt;
</pre>
<pre>
{
  "place_name": "Cafe ABC",
  "place_address": "Sector 18, Noida",
  "rating": 5,
  "text": "Loved it"
}
</pre>

<h3>Search Places</h3>
<pre>
GET /search?name=Cafe&min_rating=4
Authorization: &lt;token&gt;
</pre>

<h3>Place Details</h3>
<pre>
GET /places/&lt;place_id&gt;
Authorization: &lt;token&gt;
</pre>

<hr/>

<h2>Notes</h2>
<ul>
  <li>SQLite is used for simplicity and easy setup</li>
  <li>Database schema and queries are portable to MySQL</li>
  <li>Designed with clean separation of routes and models</li>
</ul>
