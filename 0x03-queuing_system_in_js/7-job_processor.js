import kue from 'kue';

// Create a Kue queue named push_notification_code_2
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the progress of the job from 0 to 100
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed(errorMessage);
    done(new Error(errorMessage));
  } else {
    // Track the progress to 50%
    job.progress(50, 100);

    // Log the notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simulate asynchronous task completion
    setTimeout(() => {
      // Mark the job as completed
      job.complete();
      done();
    }, 1000);
  }
};

// Create a queue processor that will process two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the function to send the notification
  sendNotification(phoneNumber, message, job, done);
});

// Close the Redis client when the script exits
process.on('SIGINT', () => {
  queue.shutdown(5000, (err) => {
    console.log('Kue shutdown: ', err || 'OK');
    process.exit(0);
  });
});
