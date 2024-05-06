// Import the required library
import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// Handle the events for the job
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
