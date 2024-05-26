// server.js
const express = require('express');
const bodyParser = require('body-parser');
const stripe = require('stripe')('your-secret-key-here');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/charge', async (req, res) => {
    const token = req.body.stripeToken;
    const amount = req.body.amount;

    try {
        let { status } = await stripe.charges.create({
            amount: amount,
            currency: 'usd',
            description: 'Token Purchase',
            source: token
        });

        res.json({ status });
    } catch (err) {
        res.status(500).end();
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const dots = document.getElementById('dots');
    const dropdown = document.getElementById('dropdown');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('close-btn');

    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    closeBtn.addEventListener('click', () => {
        sidebar.classList.remove('open');
    });

    dots.addEventListener('click', () => {
        dropdown.classList.toggle('show');
    });

    document.addEventListener('click', (event) => {
        if (!dots.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.classList.remove('show');
        }
    });
});
