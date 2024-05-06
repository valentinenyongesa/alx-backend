// Import the required library
import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Define the function to send notification
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs in the queue
queue.process('push_notification_code', (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;
  
  // Call the sendNotification function
  sendNotification(phoneNumber, message);
  
  // Mark the job as done
  done();
});

console.log('Job processor is running...');
