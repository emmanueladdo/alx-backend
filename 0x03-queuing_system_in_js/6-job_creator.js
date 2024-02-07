import kue from 'kue';

// Create a Kue queue named push_notification_code
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message!'
};

// Create a job and enqueue it
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating job:', err);
    }
  });

// Event listener for job completion
job.on('complete', () => {
  console.log('Notification job completed');
  process.exit(0);
});

// Event listener for job failure
job.on('failed', (errorMessage) => {
  console.error('Notification job failed:', errorMessage);
  process.exit(1);
});
