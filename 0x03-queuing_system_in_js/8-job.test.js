import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a new Kue queue and enter test mode
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    // Define a function that attempts to create jobs with invalid input
    const testInvalidInput = () => createPushNotificationsJobs('invalid', queue);

    // Expect an error to be thrown when invalid input is provided
    expect(testInvalidInput).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    // Define an array of jobs
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Get the list of jobs from the queue
    const jobIds = Object.keys(queue.testMode.jobs);

    // Expect two jobs to be created in the queue
    expect(jobIds).to.have.lengthOf(2);
  });
});
