// Import the required library
import kue from 'kue';

// Define the array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the progress of the job
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error message
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track the progress to 50%
  job.progress(50, 100);

  // Log sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
};

// Create a queue with Kue
const queue = kue.createQueue({
  redis: {
    port: 6379,
    host: '127.0.0.1',
  },
});

// Process jobs of the queue push_notification_code_2 with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');
