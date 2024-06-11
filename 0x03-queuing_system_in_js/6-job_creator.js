const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '00124578',
  message: 'Hello world',
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
}).on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.save();
