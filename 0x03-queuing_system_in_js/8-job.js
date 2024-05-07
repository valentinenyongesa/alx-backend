// Import the required library
import kue from 'kue';

// Define the function to create push notification jobs
const createPushNotificationsJobs = (jobs, queue) => {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job in the jobs array
  jobs.forEach((jobData) => {
    // Create a new job in the queue push_notification_code_3
    const job = queue.create('push_notification_code_3', jobData);

    // When a job is created
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // When a job is complete
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // When a job is failed
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // When a job is making progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
};

export default createPushNotificationsJobs;
