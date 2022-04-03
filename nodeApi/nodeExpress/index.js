const express = require('express') // import of express librairy and his functions
const app = express() // instance of the express object which will contain our server and all methods we need to make it works!
const parkings = require('./parkings.json')
const reservations = require('./reservations.json')

app.use(express.json()) // middleware which will receive request post

app.get('/parkings', (req, res) => {
    res.status(200).json(parkings)
})

app.get('/parkings/:id', (req, res) => {
    const id = parseInt(req.params.id)
    const parking = parkings.find(parking => parking.id === id)
    res.status(200).json(parking)
})

app.get('/parkings/:id/reservations', (req, res) => {
    const id = parseInt(req.params.id)
    const reservation = reservations.filter(reservation => reservation.parkingId === id)
    res.status(200).json(reservation)
})

app.post('/parkings', (req, res) => {
    parkings.push(req.body)
    res.status(200).json(parkings)
})

app.post('/parkings/:id/reservations', (req, res) => {
    reservations.push(req.body)
    res.status(200).json(reservations)
})

app.put('/parkings/:id', (req, res) => {
    const id = parseInt(req.params.id)
    let parking = parkings.find(parking => parking.id === id)
    parking.name = req.body.name,
    parking.city = req.body.city,
    parking.type = req.body.type,
    res.status(200).json(parking)
})

app.patch('/parkings/:id/reservations/:number', (req, res) => {
    const id = parseInt(req.params.id)
    let reservation = reservations.filter(reservation => reservation.parkingId === id)
    const number = parseInt(req.params.number)
    let identite = reservations.find(idResa => idResa.id === number)
    identite.city = req.body.city,
    identite.clientName = req.body.clientName,
    identite.vehicle = req.body.vehicle,
    identite.licensePlate = req.body.licensePlate,
    identite.checkin = req.body.checkin,
    identite.checkout = req.body.checkout
    res.status(200).json(identite)
})

app.delete('/parkings/:id', (req, res) => {
    const id = parseInt(req.params.id)
    let parking = parkings.find(parking => parking.id === id)
    parkings.splice(parkings.indexOf(parking), 1)
    res.status(200).json(parkings)
})

app.listen(8080, () => {
    console.log("Serveur à l'écoute")
})