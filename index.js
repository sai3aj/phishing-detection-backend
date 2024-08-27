const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post('/detect-phishing', (req, res) => {
  const emailText = req.body.text;
  // Here you would integrate with the Python model, e.g., via a Python script or external API
  // For simplicity, we'll return a mocked response
  const isPhishing = emailText.includes('urgent') || emailText.includes('click here');
  res.json({ phishing: isPhishing });
});

app.listen(5000, () => {
  console.log('Server running on port 5000');
});
