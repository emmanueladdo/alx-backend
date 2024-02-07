import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for key ${schoolName}:`, err);
    } else {
      console.log(`Value for ${schoolName}:`, reply);
    }
  });
};

// Function cal
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
