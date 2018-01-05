/*
 * Simple AI: Blood type identification test
 * Developed by Fadhiil Rachman <fadhiilrachman@gmail.com>
 * 5 Jan 2018
 */

const express = require('express')
const bodyparser = require('body-parser')
const app = express()

app.set('view engine', 'pug')
app.use(bodyparser.urlencoded({ extended: false }))
app.use(bodyparser.json())

// default port is 3001
let port=3001;
let app_name='Golongan Darah';

let runPy = function(pilihan) {
	return new Promise(function(resolve, reject) {

		const { spawn } = require('child_process');
		const pyprog = spawn('python', ['process.py', pilihan]);

		pyprog.stdout.on('data', function(data) {
			resolve(data);
		});
		pyprog.stderr.on('data', (data) => {
			reject(data);
		});
	});
}

app.use('/assets', express.static(__dirname + '/assets'));

app.get('/', (req, res) => {
	res.status(200).render('index', { app_name: app_name, page_title: 'Beranda - ' + app_name });
})

app.get('/about-us', (req, res) => {
	res.status(200).render('about-us', { app_name: app_name, page_title: 'Tentang Kami - ' + app_name });
})

app.post('/json/process', (req, res) => {
	res.setHeader('Content-Type', 'application/json');
	if (!(req.body.p)) {
		res.status(400).json({ error: 'Pilihan tidak ditemukan' });
	}
	req_p = req.body.p;
	runPy(req_p).then(function(fromRunPy) {
		var data = fromRunPy.toString();
		data = data.replace("\r\n", "");
		data = JSON.parse(data);
		res.status(200).json(data);
	});
})

app.listen(port, () => console.log('[ai-goldar]', 'App listening to port ' + port))