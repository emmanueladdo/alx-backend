import redis from 'redis';

const subscriberClient = redis.createClient();

// Event listeners for connection status
subscriberClient.on('error', (err) => console.log('Redis client not connected to the server:', err));
subscriberClient.on('connect', () => console.log('Redis client connected to the server'));

// Subscribe to the "holberton school channel"
subscriberClient.subscribe('holberton school channel');

// Event listener for incoming messages
subscriberClient.on('message', (channel, message) => {
  console.log(message);

  // Unsubscribe and quit if message is "KILL_SERVER"
  if (message === 'KILL_SERVER') {
    subscriberClient.unsubscribe();
    subscriberClient.quit();
  }
});

// Close the Redis client when the script exits
process.on('SIGINT', () => {
  subscriberClient.unsubscribe();
  subscriberClient.quit();
});
