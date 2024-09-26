// server.js
const express = require('express');
const app = express();
const port = 5000;

// Middleware to parse JSON body
app.use(express.json());

// POST route to handle donations
app.post('/api/donations', (req, res) => {
  const { name, amount } = req.body;
  // Process the donation (e.g., store it in the database)
  res.json({ message: 'Donation received', data: { name, amount } });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
