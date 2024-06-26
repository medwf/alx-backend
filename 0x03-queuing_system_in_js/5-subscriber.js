import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) =>
  console.error('Redis client not connected to the server:', err)
);

client.on('connect', (err) =>
  console.error('Redis client connected to the server')
);

client.subscribe('holberton school channel');

client.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
