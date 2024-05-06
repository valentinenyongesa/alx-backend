// Import the required library
import kue from 'kue';

// Define the array of jobs
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' }
];

// Create a queue with Kue
const queue = kue.createQueue();

// Loop through the array of jobs
jobs.forEach((jobData, index) => {
  // Create a new job for each object in the array
  const job = queue.create('push_notification_code_2', jobData);

  // Handle successful creation of the job
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Handle failure of the job
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Handle progress of the job
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save the job to the queue
  job.save((err) => {
    if (err) {
      console.error(`Error creating job ${index + 1}: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });
});

console.log('Job creator is running...');
