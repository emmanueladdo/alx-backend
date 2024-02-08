import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const queue = kue.createQueue();

// Reserve seat functions
const reserveSeat = (number) => client.set('available_seats', number);
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats) : 0;
};

// Initialization
reserveSeat(50);
let reservationEnabled = true;

// Server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Routes
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats > 0) {
      reserveSeat(currentAvailableSeats - 1);

      if (currentAvailableSeats - 1 === 0) {
        reservationEnabled = false;
      }

      done();
    } else {
      done(Error('Not enough seats available'));
    }
  });
});
