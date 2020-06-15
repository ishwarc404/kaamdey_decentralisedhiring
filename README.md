---


---

<h1 id="kaamdey---a-decentralised-c-to-c-sponsorship-and-hiring-service">Kaamdey - A decentralised c to c sponsorship and hiring service</h1>
<p>Kaamdey is a simple WhatsApp based hiring service which enables middle and upper class users to sponsor the lower working class, thus effectively giving them a platform through which other people can hire them.<br>
It is similar to classifieds but follows a different business model and is also seamlessly integrated as a WhatsaApp chat bot.</p>
<h1 id="code">Code</h1>
<p>There are a total of 3 different public facing servers. and Twilio APIs</p>
<ul>
<li>The first flask server powers the chat bot. Twilio reroutes all the messages it recives to this server via the first ngrox proxy.</li>
<li>The second server is the JSON Server which is effectively a database. The chatbot flask server pings the db via local host and the web application pings it via the second ngrok proxy.</li>
<li>The third is the VueJs web application, which is again publically exposed via ngrok.</li>
</ul>
<h1 id="execution">Execution</h1>
<p>Chatbot:</p>
<pre><code>cd chatbot
python3 chatbotserver.py
./ngrok http 5000
</code></pre>
<p>Database:</p>
<pre><code>cd database
json-server --watch --host '0.0.0.0' database.json
./ngrok http 3000
</code></pre>
<p>Web Application:</p>
<pre><code>cd kaamdey
npm run serve
./ngrok http 8080 -host-header="localhost:8080"
</code></pre>

