const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');
import { expect } from 'chai';
const queue = kue.createQueue();

describe('the test for job creation', function (){
      before(() => {
        queue.testMode.enter();
      });
      afterEach(() => {
        queue.testMode.clear();
      });
      after(() => {
        queue.testMode.exit();
      });
      it('Testing Error Case', () => {
        const jobs = "Hello world";
        expect(() => createPushNotificationsJobs(jobs, queue)).to.throw('Jobs is not an array');
      });
        it('Testing right Case', () => {
        const jobs = [{ phoneNumber: '123567', message: 'Your one time pin is 1222' }];
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
        });
} 
