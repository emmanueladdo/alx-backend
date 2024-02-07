import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

// Event listeners for connection status
client.on('error', (err) => console.log("Redis client not connected to the server:", err));
client.on('connect', () => console.log("Redis client connected to the server"));

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// New function to set a value for a given key
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Updated function to display the value for a given key using async/await
const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(`Value for ${schoolName}:`, reply);
  } catch (err) {
    console.error(`Error retrieving value for key ${schoolName}:`, err);
  }
};

// Call the functions to demonstrate their usage
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
