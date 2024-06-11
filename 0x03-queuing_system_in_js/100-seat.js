import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const express = require('express');

const app = express();
const port = 1245;
const client = createClient();
const queue = createQueue();

let reservation = true;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const Async = promisify(client.get).bind(client);
  const available_seats = await Async('available_seats');
  return Number(available_seats);
}

app.get('/available_seats', async (req, res) => {
  const available_seats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: available_seats });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservation) {
    res.status(404).send({ status: 'Reservation are blocked' });
    return;
  }
  res.send({ status: 'Reservation in process' });
  const reserveSeatJob = queue.create('reserve_seat').save();
  reserveSeatJob.on('complete', () => {
    console.log(`Seat reservation job ${reserveSeatJob.id} completed`);
  });
  reserveSeatJob.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${reserveSeatJob.id} failed ${errorMessage}`);
  });
});

app.get('/process', (_req, res) => {
  queue.process('reserve_seat', async (_job, done) => {
    let available_seats = await getCurrentAvailableSeats();
    if (!available_seats) {
      done(new Error('Not enough seats available'));
      return;
    }
    available_seats -= 1;
    reserveSeat(available_seats);
    if (!available_seats) reservation = false;
    done();
  });
  res.status(200).send({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
