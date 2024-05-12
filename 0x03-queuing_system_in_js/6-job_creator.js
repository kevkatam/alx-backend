const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0746646637',
  message: 'Verifying your account',
}

const job = queue.create('push_notification_job', jobData)
  .save( function(err) {
    if ( !err ) {
      console.log(`Notification job created: ${job.id}`);
    }
   });
job.on('complete', function(result) {
  console.log(`Notification job completed`);
}).on('failed', function(err) {
  console.log(`Notification job failed`);
});
